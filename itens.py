import utils
import persistencia
def buscar_item(dados,codigo):
    return  (dados["itens"].get(codigo))#procura o item no dicionario com base no codigo dele

def cadastrar_item(dados): #cadastra o item que o usuario digita e salva no arquivo de itens.json
    codigo=utils.ler_codigo_item()
    if(codigo in dados["itens"]):
        print("Codigo ja cadastrado. ")
        return

    tipo=codigo[:2]#informacoes
    descricao=utils.ler_mensagem("Descrição: ")
    unidade=utils.ler_mensagem("Unidade (un,m,L): ")
    custo=utils.ler_float("Custo: ",0)
    lead_time=utils.ler_inteiro("Lead Time (semanas/tempo de producao): ")
    if(lead_time<0):
        print("Tempo Negativo.")
        return
    estoque_seg = utils.ler_float("Estoque de seguranca: ", 0)
    lote_minimo =utils.ler_float("Lote minimo: ", 0)
    dados["itens"][codigo] = dicionario={#dicionario do itens que fica dentro do dados
        "descricao": descricao, #chave do dicionario item é o codigo do item numerico
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


def listar_dados(dados):#lista os dados do dicionario e printa tudo
    utils.exibir_cabecalho("Itens")
    print(f"{'Codigo':<9}{'Descricao':<28}{'Tipo':<6}{'Unid':<6}{'Custo':<10}{'Lead Time':<11}{'Est.Seg':<9}{'Lote Min'}")
    for codigo in sorted(dados["itens"]):
        item=dados["itens"][codigo]
        print(f"{codigo:<9}{item['descricao']:<28}{item['tipo']:<6}{item['unidade']:<6}{item['custo']:<10}{item['lead_time']:<11}{item['estoque_seg']:<9}{item['lote_minimo']}")


def alterar_item(dados):#alterar algo de item codigo do item e tipo nao podem ser alterados
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
    if len(novo)!=6:
        print("Digite os 6 valores separados por ;")
        return
    try:
        custo=float(novo[2].replace(",","."))
        lead_time=int(novo[3])
        estoque_seg=float(novo[4].replace(",","."))
        lote_minimo=float(novo[5].replace(",","."))
    except ValueError:
        print("Valor Errado")
        return
    if custo<0 or lead_time<0 or estoque_seg<0 or lote_minimo<0:
        print("Valor Negativo")
        return
    item['descricao']=novo[0]
    item['unidade']=novo[1]
    item['custo']=custo
    item['lead_time']=lead_time
    item['estoque_seg']=estoque_seg
    item['lote_minimo']=lote_minimo
    persistencia.salvar_tudo(dados)
    print("Item alterado")

#mp = materia prima
#pa=produto acabado
#sa=semi acabado