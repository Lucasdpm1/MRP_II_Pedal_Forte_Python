import utils
import persistencia
def validar_componente(dados, pai, filho):
    tipo_pai=dados["itens"][pai]["tipo"]
    tipo_filho=dados["itens"][filho]["tipo"]

    if(tipo_pai=="MP"):
        print("MP não possui estrutura")
        return False
    if (tipo_pai=="SA" and tipo_filho!="MP"):
        print("SA aceita Apenas MP")
        return False

    if (tipo_pai=="PA" and tipo_filho=="PA"):
        print("PA não pode ter PA")
        return False

    return True

def adicionar_componente(dados):
    pai =utils.ler_codigo_item("Item pai: ")
    filho =utils.ler_codigo_item("Componente: ")
    if(pai not in dados["itens"] or filho not in dados["itens"]):
        print("Item não encontrado")
        return
    if not validar_componente(dados, pai, filho):
        return
    qtd =utils.ler_float("Quantidade por unidade: ", 0.01)
    if pai not in dados["estrutura"]:
        dados["estrutura"][pai] = []
    for comp in dados["estrutura"][pai]:
        if comp["componente"] == filho:
            print("Componente ja existe")
            return
    dados["estrutura"][pai].append({"componente": filho, "qtd": qtd})
    persistencia.salvar_tudo(dados)
    print("Componente adicionado")




def listar_componentes(dados,pai):
    for componente in dados["estrutura"].get(pai,[]):
        codigo=componente["componente"]
        print (codigo)
        print (dados["itens"][codigo]["descricao"])
        print (componente["qtd"])



def exibir_estrutura(dados, codigo, nivel, qtd):
    item=dados["itens"][codigo]
    recuo="     " * nivel
    print(f"{recuo}{codigo} {item['descricao']} ... {qtd} {item['unidade']}")
    for comp in dados["estrutura"].get(codigo, []):
        exibir_estrutura(dados, comp["componente"], nivel + 1, comp["qtd"])