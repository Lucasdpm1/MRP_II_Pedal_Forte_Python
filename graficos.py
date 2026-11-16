import os
import matplotlib.pyplot as plt
import capacidade

def grafico_posicao_estoque(dados):
    os.makedirs("graficos",exist_ok=True)
    codigos=[]
    saldos=[]
    segurancas=[]
    for codigo in dados["itens"]:
        codigos.append(codigo)
        saldos.append(dados["estoque"][codigo])
        segurancas.append(dados["itens"][codigo]["estoque_seg"])

    if len(codigos)==0:
        print("Nenhum item cadastrado")
        return

    pos_saldo=[]
    pos_seguranca=[]
    for i in range(len(codigos)):
        pos_saldo.append(i-0.2)
        pos_seguranca.append(i+0.2)

    plt.bar(pos_saldo,saldos,width=0.4,label="Saldo")
    plt.bar(pos_seguranca,segurancas,width=0.4,label="Seguranca")
    plt.xticks(range(len(codigos)),codigos,rotation=90)
    plt.title("Posicao de estoque")
    plt.legend()
    plt.tight_layout()
    plt.savefig("graficos/posicao_estoque.png")
    plt.show()
    plt.close()


def grafico_estoque_projetado(dados,item):
    os.makedirs("graficos",exist_ok=True)
    if item not in dados.get("mrp",{}):
        print("Execute o MRP antes")
        return

    ep=dados["mrp"][item]["projetado"]
    seguranca=dados["itens"][item]["estoque_seg"]
    semanas=[1,2,3,4,5,6,7,8]
    plt.plot(semanas,ep[1:],marker="o",label="Estoque projetado")
    plt.axhline(seguranca,color="red",linestyle="--",label="Seguranca")
    plt.title("Estoque projetado - "+item)
    plt.xlabel("Semana")
    plt.legend()
    plt.savefig("graficos/estoque_projetado_"+item+".png")
    plt.show()
    plt.close()


def grafico_ordens_por_semana(dados):
    os.makedirs("graficos",exist_ok=True)
    op=[0,0,0,0,0,0,0,0,0]
    oc=[0,0,0,0,0,0,0,0,0]
    for ordem in dados["ordens"]:
        semana=ordem["entregar"]
        if semana<1 or semana>8:
            continue
        if ordem["tipo"]=="OP":
            op[semana]=op[semana]+ordem["qtd"]
        else:
            oc[semana]=oc[semana]+ordem["qtd"]

    semanas=[1,2,3,4,5,6,7,8]
    plt.bar(semanas,op[1:],label="OP")
    plt.bar(semanas,oc[1:],bottom=op[1:],label="OC")
    plt.title("Ordens por semana de entrega")
    plt.xlabel("Semana")
    plt.legend()
    plt.savefig("graficos/ordens_por_semana.png")
    plt.show()
    plt.close()


def grafico_carga_capacidade(dados,centro):
    os.makedirs("graficos",exist_ok=True)
    if centro not in dados["centros"]:
        print("Centro nao encontrado")
        return

    capacidade_centro=dados["centros"][centro]["capacidade"]
    carga=capacidade.calcular_carga(dados,centro)
    cores=[]
    for semana in range(1,9):
        if carga[semana]>capacidade_centro:
            cores.append("red")
        else:
            cores.append("blue")

    semanas=[1,2,3,4,5,6,7,8]
    plt.bar(semanas,carga[1:],color=cores)
    plt.axhline(capacidade_centro,color="black",linestyle="--",label="Capacidade")
    plt.title("Carga x capacidade - "+centro)
    plt.xlabel("Semana")
    plt.ylabel("Horas")
    plt.legend()
    plt.savefig("graficos/carga_"+centro+".png")
    plt.show()
    plt.close()