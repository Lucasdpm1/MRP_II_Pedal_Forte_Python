import ordens
def ordenar_itens_por_tipo(dados):
    resultado=[]
    for tipo in ["PA","SA","MP"]:
        for codigo in dados["itens"]:
            if(dados["itens"][codigo]["tipo"]==tipo):
                resultado.append(codigo)

    return resultado


def obter_recebimentos_programados(dados, item):
    recibimento = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    for ordem in dados["ordens"]:
        if(ordem["item"]==item):
            if(ordem["status"]=="FIRME" or ordem["status"]=="LIBERADA"):
                semana=ordem["entregar"]
                if semana>=1 and semana<=8:
                    recibimento[semana]=recibimento[semana]+ordem["qtd"]

    return recibimento


def calcular_necessidade_bruta(dados, item, liberacoes):
    necessidade = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    if dados["itens"][item]["tipo"]=="PA":
        if item in dados["mps"]:
            for semana in range(1,9):
                necessidade[semana]=dados["mps"][item][str(semana)]

    else:
        for pai in dados["estrutura"]:
            for comp in dados["estrutura"][pai]:
                if comp["componente"]==item:
                    for semana in range(1,9):
                        necessidade[semana]=necessidade[semana]+liberacoes[pai][semana]*comp["qtd"]


    return necessidade


def calcular_registro_item(dados,item,liberacoes):
    dados_item = dados["itens"][item]
    seguranca = dados_item["estoque_seg"]
    lote = dados_item["lote_minimo"]
    lead_time = dados_item["lead_time"]
    bruta = calcular_necessidade_bruta(dados, item, liberacoes)
    programado = obter_recebimentos_programados(dados, item)
    liquida = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    planejado = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    projetado = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    liberacao = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    projetado_anterior = dados["estoque"][item]             
    for semana in range(1, 9):
        liquida[semana] = max(0, bruta[semana] + seguranca - (projetado_anterior + programado[semana]))
        if liquida[semana] > 0:
            planejado[semana] = max(liquida[semana], lote)
        projetado[semana] = projetado_anterior + programado[semana] + planejado[semana] - bruta[semana]
        projetado_anterior = projetado[semana]
        if planejado[semana] > 0:
            liberar = semana - lead_time
            if liberar < 1:
                atrasada = True
            else:
                atrasada = False
                liberacao[liberar] = liberacao[liberar] + planejado[semana]
            if dados_item["tipo"] == "MP":
                tipo_ordem = "OC"
            else:
                tipo_ordem = "OP"
            ordens.criar_ordem(dados, tipo_ordem, item, planejado[semana], liberar, semana, atrasada)
    liberacoes[item] = liberacao                     
    dados["mrp"][item] = {"bruta": bruta, "programado": programado, "projetado": projetado, "liquida": liquida, "planejado": planejado, "liberacao": liberacao}


def executar_mrp(dados):
    ordens_mantidas=[]
    for ordem in dados["ordens"]:
        if ordem["status"]!="PLANEJADA":
            ordens_mantidas.append(ordem)

    dados["ordens"]=ordens_mantidas
    dados["mrp"]={}
    liberacoes={}
    for item in ordenar_itens_por_tipo(dados):
        calcular_registro_item(dados,item,liberacoes)
    import persistencia
    persistencia.salvar_tudo(dados)
    atrasadas=0
    for ordem in dados["ordens"]:
        if(ordem["atrasada"]):
            atrasadas=atrasadas+1
    print("MRP executado.", atrasadas, "mensagens de excecao")


def imprimir_linha(titulo, lista):
    texto = f"{titulo:<22}"                             
    for semana in range(1, 9):
        texto = texto + f"{lista[semana]:>7.1f}"          
    print(texto)


def exibir_registro_mrp(dados, item):
    if item not in dados.get("mrp", {}):
        print("Execute o MRP antes")
        return
    registro = dados["mrp"][item]
    dados_item = dados["itens"][item]
    print("REGISTRO MRP -", item, dados_item["descricao"])
    print("Lead time:", dados_item["lead_time"], "| Est. seguranca:", dados_item["estoque_seg"], "| Lote min.:", dados_item["lote_minimo"], "| Estoque:", dados["estoque"][item])
    print("Semana", [0, 1, 2, 3, 4, 5, 6, 7, 8])
    print("Necessidade bruta", registro["bruta"])
    print("Receb. programados", registro["programado"])
    print("Estoque projetado", registro["projetado"])
    print("Necessidade liquida", registro["liquida"])
    print("Receb. planejados", registro["planejado"])
    print("Liberacao planejada", registro["liberacao"])