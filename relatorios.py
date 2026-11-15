import persistencia
import utils
def exportar_estoque_csv(dados):
    linhas=[]
    for codigo in dados["itens"]:
        item=dados["itens"][codigo]
        saldo=dados["estoque"][codigo]
        seguranca=item["estoque_seg"]

        if saldo<seguranca:
            situacao="ABAIXO"
        else:
            situacao="OK"

        linha={"codigo":codigo,"descricao":item["descricao"],"saldo":saldo,"estoque_seg":seguranca,"situacao":situacao}
        linhas.append(linha)

    colunas=["codigo","descricao","saldo","estoque_seg","situacao"]
    persistencia.salvar_csv("estoque.csv",linhas,colunas)
    print("Arquivo Estoque.csv gerado")


def exportar_ordens_csv(dados):
    colunas=["numero","tipo","item","qtd","liberar","entregar","status","atrasada"]
    persistencia.salvar_csv("ordens.csv",dados["ordens"],colunas)
    print("Arquivo Ordens.csv gerado")
