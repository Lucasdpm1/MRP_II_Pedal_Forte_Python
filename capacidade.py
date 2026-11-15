import utils
import persistencia

def cadastrar_centro(dados):
    codigo = utils.ler_mensagem("Codigo do centro (ex: CT-01): ").upper()
    if codigo in dados["centros"]:
        print("codigo ja cadastrado. ")
        return

    nome=utils.ler_mensagem("Nome do Centro: ")
    capacidade=utils.ler_float("Capacidade Horas por Semana: ",1)
    custo_hora=utils.ler_float("Custo por Hora",0)
    dados["centros"][codigo]={"nome":nome,
                              "capacidade":capacidade,
                              "custo_hora":custo_hora
                              }
    persistencia.salvar_tudo(dados)
    print ("Centro Cadastrado")



def listar_centros(dados):
    utils.exibir_cabecalho("Centro De Trabalho")
    for codigo in sorted(dados["centros"]):
        centro=dados["centros"][codigo]
        print(f"Codigo:{codigo}  {centro['nome']}   {centro['capacidade']}  {centro['custo_hora']}")



def definir_roteiro(dados):
    item=utils.ler_codigo_item()
    if item not in dados["itens"]:
        print("item não encontrado")
        return
    if dados["itens"][item]["tipo"]=="MP":
        print("MP é comprada não tem roteiro")
        return
    centro=utils.ler_mensagem("Centro: ").upper()
    if centro not in dados["centros"]:
        print("Centro não encontrado")
        return

    tempo=utils.ler_float("Tempo Unidade(horas): ",0.01)
    dados["roteiros"][item]={"centro":centro,"tempo":tempo}
    persistencia.salvar_tudo(dados)
    print("Roteiro Salvo")