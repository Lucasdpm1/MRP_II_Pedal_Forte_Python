from pathlib import Path
import json
import csv

PASTA_DATA = Path(__file__).parent / "data"

def caminho_arquivo(nome):
    PASTA_DATA.mkdir(exist_ok=True)
    return PASTA_DATA / nome

def carregar_json(nome):
    caminho=caminho_arquivo(nome)
    try:
        arquivo=open(caminho,"r",encoding="utf-8")
        conteudo=json.load(arquivo)
        return conteudo

    except FileNotFoundError:
        print("Fila Não Encontrada")
        return

    except json.JSONDecodeError:
        print("Fila Quebrada")
        return

def salvar_json(nome,conteudo):
    caminho=caminho_arquivo(nome)
    arquivo=open(caminho,"w",encoding="utf-8")
    json.dump(conteudo, arquivo, indent=4, ensure_ascii=False)


def carregar_csv(nome):
    caminho=caminho_arquivo(nome)
    if(caminho==None):
        return []
    arquivo=open(caminho,"r",newline="",encoding="utf-8")
    leitor=[(csv.DictReader(arquivo))]
    linhas=list(leitor)
    for linha in linhas:
        linha=linha(int)
    return linhas


def salvar_csv(nome, linhas, colunas):
    caminho=caminho_arquivo(nome)
    arquivo=[open(caminho, "w", newline="", encoding="utf-8")]
    escritor=csv.DictReader(arquivo,fieldnames=colunas)
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