import utils

def calcular_custo_padrao(dados, codigo):
    item = dados["itens"][codigo]
    if item["tipo"] == "MP":
        return item["custo"]                                           
    total = 0                                                              
    for  comp in dados["estrutura"].get(codigo, []):                 
        custo_filho = calcular_custo_padrao(dados, comp["componente"])
        total = total + comp["qtd"] * custo_filho
    if codigo in dados["roteiros"]:
        roteiro = dados["roteiros"][codigo]
        custo_hora = dados["centros"][roteiro["centro"]]["custo_hora"]
        total = total + roteiro["tempo"] * custo_hora
    return total

def exibir_custo(dados,codigo):
    if codigo not in dados["itens"]:
        print("Item não encontrado.")
        return

    utils.exibir_cabecalho("Custo Padrão: "+codigo)
    for comp in dados["estrutura"].get(codigo,[]):
        codigo_filho=comp["componente"]
        custo_unitario=calcular_custo_padrao(dados,codigo_filho)
        total_linha=comp["qtd"]*custo_unitario
        print(f"{codigo_filho} {dados['itens'][codigo_filho]['descricao']} {comp['qtd']} {custo_unitario:.2f} {total_linha:.2f}")

    if codigo in dados["roteiros"]:
        roteiro=dados["roteiros"][codigo]
        custo_hora=dados["centros"][roteiro["centro"]]["custo_hora"]
        print(f"Mao de obra {roteiro['centro']} {roteiro['tempo']} h {custo_hora:.2f} {roteiro['tempo'] * custo_hora:.2f}")
    total = calcular_custo_padrao(dados, codigo)
    print("Custo Total: " , utils.formatar_moeda(total))