import utils
import persistencia
#capacidade=horas que a maquina trabalha por semana
#crp compara capacidade da maquina com a carga de producao necessaria semanal que as ordens pedem
def cadastrar_centro(dados):
    codigo = utils.ler_mensagem("Codigo do centro (ex: CT-01): ").upper()
    if not codigo.replace("-", "").isalnum():
        print("Codigo invalido")
        return
    if codigo in dados["centros"]:
        print("codigo ja cadastrado. ")
        return
    #cadastra o centro de trabalho
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
    for codigo in sorted(dados["centros"]):#lista os centros
        centro=dados["centros"][codigo]
        print(f"Codigo:{codigo}  {centro['nome']}   {centro['capacidade']}  {centro['custo_hora']}")



def definir_roteiro(dados):#roteiro liga um item a um centro de producao
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



def calcular_carga(dados,centro): #calcula a carga de trabalho necessaria em cada semana
    carga = [0, 0, 0, 0, 0, 0, 0, 0, 0]                                     
    for  ordem in dados["ordens"]:
        if ordem["tipo"] != "OP":
            continue                                                        
        if ordem["item"] not in dados["roteiros"]:
            continue
        roteiro = dados["roteiros"][ordem["item"]]
        if roteiro["centro"] != centro:
            continue
        semana = ordem["liberar"]
        if semana < 1 or semana > 8:
            continue
        carga[semana] = carga[semana] + ordem["qtd"] * roteiro["tempo"]
    return carga


def exibir_crp(dados,centro):#confere se o centro suporta a carga necessaria para cada semana e libera a saida
    if centro not in dados["centros"]:
        print("Centro nao encontrado")
        return
    capacidade = dados["centros"][centro]["capacidade"]
    carga = calcular_carga(dados, centro)
    utils.exibir_cabecalho("Carga x capacidade " + centro)
    semanas_ruins = []                                                     
    for  semana in range(1, 9):                                       
        uso = carga[semana] / capacidade * 100
        barra = "#" * int(uso / 10)                                        
        if carga[semana] > capacidade:
            aviso = "SOBRECARGA"
            semanas_ruins.append(semana)
        else:
            aviso = ""
        print(f"{semana} {carga[semana]:.1f} {uso:.0f}% {barra} {aviso}")
    if len(semanas_ruins) > 0:                                              
        print("Sugestao: antecipar OPs ou programar hora extra nas semanas", semanas_ruins)