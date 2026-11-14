import utils
import persistencia
def buscar_item(dados,codigo):
    return  (dados["itens"].get(codigo))

def cadastrar_item(dados):
    codigo=utils.ler_codigo_item()
    if(codigo in dados["itens"]):
        print("Codigo ja cadastrado. ")
        return

    tipo=codigo[:2]
    descricao=utils.ler_mensagem("Descrição: ")
    unidade=utils.ler_mensagem("Unidade (un,m,L): ")
    custo=utils.ler_float("Custo: ",0)
    lead_time=utils.ler_inteiro("Lead Time (semanas): ")
    if(lead_time<0):
        print("Tempo Negativo.")
        return
    estoque_seg = utils.ler_float("Estoque de seguranca: ", 0)
    lote_minimo =utils.ler_float("Lote minimo: ", 0)
    dados["itens"][codigo] = dicionario={
        "descricao": descricao,
        "tipo": tipo,
        "unidade": unidade,
        "custo": custo,
        "lead_time": lead_time,
        "estoque_seg": estoque_seg,
        "lote_minimo": lote_minimo,
    }
    dados["estoque"][codigo] = 0
    persistencia.salvar_tudo(dados)
    print("Item cadastrado")


def listar_dados(dados):
    utils.exibir_cabecalho("Itens")
    for codigo in sorted(dados["itens"]):
        item=dados["itens"][codigo]
        print(f"{codigo} {item['descricao']} {item['tipo']} {item['unidade']} {item['custo']} {item['lead_time']} {item['estoque_seg']} {item['lote_minimo']}")
        print("\n")


def alterar_item(dados):
    codigo=utils.ler_codigo_item()
    item=buscar_item(dados,codigo)
    if item==None:
        print("Item não Encontrado")
        return

    print(f"{codigo} {item['descricao']} {item['unidade']} {item['custo']} {item['lead_time']} {item['estoque_seg']} {item['lote_minimo']}")
    novo=input("Digite os Valores Que Deseja Mudar na ordem Mostrada (separados por ;): ").strip()
    if novo=="":
        return

    novo=novo.split(";")
    item['descricao']=novo[0]
    item['unidade']=novo[1]
    item['custo']=float(novo[2])
    item['lead_time']=int(novo[3])
    item['estoque_seg']=float(novo[4])
    item['lote_minimo']=float(novo[5])
    persistencia.salvar_tudo(dados)