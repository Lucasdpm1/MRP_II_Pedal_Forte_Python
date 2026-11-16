import utils
import persistencia
def consultar_saldo(dados, codigo):
    return dados["estoque"][codigo]

def verificar_alerta(dados, codigo):
    saldo=dados["estoque"][codigo]
    seguranca=dados["itens"][codigo]["estoque_seg"]
    if saldo<seguranca:
        print(f"Alerta: Saldo {saldo} abaixo do estoque de segurança {seguranca}")

def registrar_movimento(dados, codigo, tipo, qtd, documento, data):
    saldo=dados["estoque"][codigo]

    if(tipo=="E"):
        novo_saldo=saldo+qtd

    if(tipo=="S"):
        if qtd>saldo:
            print("Saldo insuficiente (saldo atual:",saldo,")")
            return False
        novo_saldo=saldo-qtd

    if(tipo=="A"):
        novo_saldo=saldo+qtd
        if novo_saldo<0:
            print("Novo Saldo Negativo/Invalido")
            return False
    dados["estoque"][codigo] = novo_saldo
    dados["movimentos"].append({"data": data, "item": codigo, "tipo": tipo, "qtd": qtd, "saldo": novo_saldo, "documento": documento})
    return True


def menu_movimentar(dados):
    codigo=utils.ler_codigo_item()
    if(codigo not in dados["itens"]):
        print("Codigo não esta no dicionario principal")
        return

    tipo=utils.ler_opcao("Tipo [E]ntrada [S]aida [A]juste: ", ["E", "S", "A"])
    if tipo=="A":
        qtd=utils.ler_float("Quantidade: ")
    else:
        qtd=utils.ler_float("Quantidade: ", 0.01)
    documento=utils.ler_mensagem("Documento/motivo: ")
    data=utils.ler_data()
    resultado=registrar_movimento(dados,codigo,tipo,qtd,documento,data)
    if(resultado==False):
        print("Operação não Realizada")
    else:
        verificar_alerta(dados,codigo)
        persistencia.salvar_tudo(dados)


def exibir_historico(dados,codigo):
    print(f"HISTORICO - {codigo} {dados['itens'][codigo]['descricao']}")
    print("Data Tipo Qtde Saldo Documento")
    for m in dados["movimentos"]:
        if m["item"]==codigo:
            qtd=m["qtd"]
            if m["tipo"]=="S":
                qtd=-qtd
            print(f"{m['data']} {m['tipo']} {qtd} {m['saldo']} {m['documento']}")
    verificar_alerta(dados,codigo)