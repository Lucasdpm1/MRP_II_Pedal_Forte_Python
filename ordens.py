import utils
import estoque
import persistencia

def buscar_ordem(dados, numero):#bsuca a ordem no sistema
    for ordem in dados["ordens"]:
        if ordem["numero"]==numero:
            return ordem

    return None


def gerar_numero_ordem(dados, tipo):
    maior=0#gera o numero da ordem
    for ordem in dados["ordens"]:
        if ordem["tipo"]==tipo:
            numero=int(ordem["numero"][3:])
            if numero>maior:
                maior=numero
    return f"{tipo}-{maior+1:04d}"


def criar_ordem(dados, tipo, item, qtd, liberar, entregar, atrasada):
    numero=gerar_numero_ordem(dados,tipo)
    ordem={"numero":numero,#cria a ordem no sistema chamando numero
           "tipo":tipo,#cria a ordem como PLANEJADA
           "item":item,
           "qtd":qtd,
           "liberar":liberar,
           "entregar":entregar,
           "status":"PLANEJADA",
            "atrasada":atrasada
           }
    dados["ordens"].append(ordem)


def listar_ordem(dados):# lista as ordemns
    utils.exibir_cabecalho("Ordens")
    atrasadas=0
    for ordem in dados["ordens"]:
        texto=f"{ordem['numero']}  {ordem['tipo']}  {ordem['item']}  {ordem['qtd']} {ordem['liberar']}  {ordem['entregar']} {ordem['status']}"
        if (ordem["atrasada"]):
            texto=texto+" ATRASADA"
            atrasadas=atrasadas+1
        print(texto)


    print("Atrasadas:",atrasadas)


def mudar_status(dados, numero, status_atual, status_novo):#mudanca do status pra evitar erros
    ordem=buscar_ordem(dados,numero)
    if ordem==None:
        print("Ordem não encontrada.")
        return

    if ordem["status"]!=status_atual:
        print("Status Está Invalido.")
        return

    ordem["status"]=status_novo
    persistencia.salvar_tudo(dados)
    print("Ordem " , numero , " agora esta " , status_novo)

def firmar_ordem(dados,numero):#firma a ordem no sistema
    mudar_status(dados,numero,"PLANEJADA","FIRME")

def liberar_ordem(dados,numero):
    mudar_status(dados,numero,"FIRME","LIBERADA")#libera a ordem no sistema

def encerrar_ordem(dados,numero):
    mudar_status(dados,numero,"LIBERADA","ENCERRADA")#encerra a ordem


def apontar_producao(dados,numero):
    ordem=buscar_ordem(dados,numero)
    if ordem==None:#salva as ordens no sistema
        print("Ordem não encontrada.");
        return

    if ordem["tipo"]!="OP" or ordem["status"]!="LIBERADA":
        print("So OP liberada pode ser apontada")
        return

    for  comp in dados["estrutura"].get(ordem["item"], []):
        necessario = ordem["qtd"] * comp["qtd"]
        if dados["estoque"][comp["componente"]] < necessario:
            print("Falta componente: " + comp["componente"])
            return

    data = utils.ler_data()
    for  comp in dados["estrutura"].get(ordem["item"], []):
        necessario = ordem["qtd"] * comp["qtd"]
        estoque.registrar_movimento(dados, comp["componente"], "S", necessario, numero, data)
    estoque.registrar_movimento(dados, ordem["item"], "E", ordem["qtd"], numero, data)
    ordem["status"] = "ENCERRADA"
    persistencia.salvar_tudo(dados)
    print("Producao apontada");