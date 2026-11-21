import utils
import persistencia#plano de producao 
def cadastrar_demanda(dados):
    codigo=utils.ler_codigo_item()
    if (codigo not in dados["itens"]):
        print("Item não encontrado. ")
        return
    if(dados["itens"][codigo]["tipo"]!="PA"):
        print("So PA tem demanda")
        return

    if(codigo not in dados["mps"]):#salva as demandas semanais
        dados["mps"][codigo] = {}
        for semana in range(1,9):
            dados["mps"][codigo][str(semana)]=0

    semana=utils.ler_inteiro("Semana( 1 a 8): ")
    if(semana<1 or semana>8):
        print("Semana Invalida")
        return
    qtd=utils.ler_float("Quantidade: ", 0)
    dados["mps"][codigo][str(semana)]=qtd
    persistencia.salvar_tudo(dados)


def exibir_mps(dados):
    utils.exibir_cabecalho("Plano Mestre De Produção")
    for codigo in dados["mps"]:
        print(codigo)
        for semana in range (1,9):
            print(f"Semana {semana}: {dados['mps'][codigo][str(semana)]}")