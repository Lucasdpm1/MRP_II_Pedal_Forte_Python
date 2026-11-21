import os
import json
import csv

COLUNAS_MOVIMENTOS = ["data", "item", "tipo", "qtd", "saldo", "documento"]
#coluna sempre igual pros arquivos data, item, tipo, qtd, saldo, documento.

def caminho_arquivo(nome):  #caminho do arquivo
    if not os.path.exists("data"):
        os.mkdir("data")
    return "data/" + nome


def carregar_json(nome, padrao): #carregar o arquivo json 
    caminho = caminho_arquivo(nome)
    try:
        with open(caminho, "r", encoding="utf-8") as arquivo:
            conteudo = json.load(arquivo)
        return conteudo

    except FileNotFoundError:
        return padrao

    except json.JSONDecodeError:
        print("Arquivo Quebrado")
        os.rename(caminho, caminho + ".quebrado")
        return padrao


def salvar_json(nome, conteudo):
    caminho = caminho_arquivo(nome)
    with open(caminho, "w", encoding="utf-8") as arquivo:
        json.dump(conteudo, arquivo, indent=4, ensure_ascii=False)


def carregar_csv(nome):#abre o csv
    caminho = caminho_arquivo(nome)
    if not os.path.exists(caminho):
        return []
    with open(caminho, "r", newline="", encoding="utf-8") as arquivo:
        separador = ","
        if ";" in arquivo.readline():
            separador = ";"
        arquivo.seek(0)
        leitor = csv.DictReader(arquivo, delimiter=separador)
        linhas = list(leitor)
    validas = []
    for linha in linhas:
        try:
            linha["qtd"] = float(linha["qtd"])
            linha["saldo"] = float(linha["saldo"])
            validas.append(linha)
        except (ValueError, KeyError, TypeError):
            print("Linha invalida ignorada em", nome)
    return validas


def salvar_csv(nome, linhas, colunas):
    caminho = caminho_arquivo(nome)
    with open(caminho, "w", newline="", encoding="utf-8") as arquivo:
        escritor = csv.DictWriter(arquivo, fieldnames=colunas)
        escritor.writeheader()
        escritor.writerows(linhas)#salva o csv


def carregar_tudo():  # carrega todos os arquivos de uma vez pra montar o dicionario dados principal
    dados = {}
    dados["itens"] = carregar_json("itens.json", {})
    dados["estrutura"] = carregar_json("estrutura.json", {})
    dados["estoque"] = carregar_json("estoque.json", {})
    dados["movimentos"] = carregar_csv("movimentos.csv")
    dados["centros"] = carregar_json("centros.json", {})
    dados["roteiros"] = carregar_json("roteiros.json", {})
    dados["mps"] = carregar_json("mps.json", {})
    dados["ordens"] = carregar_json("ordens.json", [])
    return dados


def salvar_tudo(dados): #pega o dicionario dados e atualiza cada arquivo
    salvar_json("itens.json", dados["itens"])
    salvar_json("estrutura.json", dados["estrutura"])
    salvar_json("estoque.json", dados["estoque"])
    salvar_csv("movimentos.csv", dados["movimentos"], COLUNAS_MOVIMENTOS)
    salvar_json("centros.json", dados["centros"])
    salvar_json("roteiros.json", dados["roteiros"])
    salvar_json("mps.json", dados["mps"])
    salvar_json("ordens.json", dados["ordens"])