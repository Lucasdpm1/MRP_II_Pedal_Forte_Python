from pathlib import Path
import json
import csv

PASTA_DATA = Path(__file__).parent / "data"
COLUNAS_MOVIMENTOS = ["data", "item", "tipo", "qtd", "saldo", "documento"]


def caminho_arquivo(nome):
    PASTA_DATA.mkdir(exist_ok=True)
    return PASTA_DATA / nome


def carregar_json(nome, padrao):
    caminho = caminho_arquivo(nome)
    try:
        with open(caminho, "r", encoding="utf-8") as arquivo:
            conteudo = json.load(arquivo)
        return conteudo

    except FileNotFoundError:
        return padrao

    except json.JSONDecodeError:
        print("Arquivo Quebrado")
        return padrao


def salvar_json(nome, conteudo):
    caminho = caminho_arquivo(nome)
    with open(caminho, "w", encoding="utf-8") as arquivo:
        json.dump(conteudo, arquivo, indent=4, ensure_ascii=False)


def carregar_csv(nome):
    caminho = caminho_arquivo(nome)
    if not caminho.exists():
        return []
    with open(caminho, "r", newline="", encoding="utf-8") as arquivo:
        leitor = csv.DictReader(arquivo)
        linhas = list(leitor)
    for linha in linhas:
        linha["qtd"] = float(linha["qtd"])
        linha["saldo"] = float(linha["saldo"])
    return linhas


def salvar_csv(nome, linhas, colunas):
    caminho = caminho_arquivo(nome)
    with open(caminho, "w", newline="", encoding="utf-8") as arquivo:
        escritor = csv.DictWriter(arquivo, fieldnames=colunas)
        escritor.writeheader()
        escritor.writerows(linhas)


def carregar_tudo():
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


def salvar_tudo(dados):
    salvar_json("itens.json", dados["itens"])
    salvar_json("estrutura.json", dados["estrutura"])
    salvar_json("estoque.json", dados["estoque"])
    salvar_csv("movimentos.csv", dados["movimentos"], COLUNAS_MOVIMENTOS)
    salvar_json("centros.json", dados["centros"])
    salvar_json("roteiros.json", dados["roteiros"])
    salvar_json("mps.json", dados["mps"])
    salvar_json("ordens.json", dados["ordens"])