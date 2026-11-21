from datetime import datetime


def ler_inteiro(pergunta="Qual Seu numero: "):
    while True:
        numero = input(pergunta)
        numero = numero.strip()
        try:
            numero = int(numero)#try pra ver se o usuario digitou numero msm
        except ValueError:
            print("Numero Errado")
            continue

        return numero


def ler_float(pergunta="Qual Seu Numero: ", minimo=-999999):
    while True:
        numero = input(pergunta)
        numero = numero.strip().replace(",", ".")
        try:
            numero = float(numero)
        except ValueError:
            print("Numero Errado")
            continue
        if numero < minimo:
            print(f"O valor deve ser no minimo {minimo}")
            continue

        return numero


def ler_mensagem(pergunta):
    while True:
        mensagem = input(pergunta)
        mensagem = mensagem.strip()#ler string
        if mensagem == "":
            print("Mensagem Vazia")
            continue

        return mensagem


def ler_opcao(pergunta, opcoes_validas):
    opcoes = []
    for opcao in opcoes_validas:
        opcoes.append(opcao.upper())
    while True:
        opcao = input(pergunta)
        opcao = opcao.strip().upper() #validar opcao do menus
        if opcao not in opcoes:
            print("Opcao Errada")
            continue

        return opcao


def validar_codigo_item(codigo): #validar o codigo do item que o usuario fornece
    partes = codigo.split("-")#coisa errada retorna false
    if len(partes) != 2:
        return False
    if partes[0] not in ["PA", "SA", "MP"]:
        return False
    if not partes[1].isdigit():
        return False

    return True


def ler_codigo_item(pergunta="Codigo do item: "):#achar codigo do item pesquisado
    while True:
        codigo = input(pergunta)
        codigo = codigo.strip().upper()
        if not validar_codigo_item(codigo):
            print("Codigo Errado (use Tipo-Numero, ex: PA-001)")
            continue

        return codigo


def ler_data(pergunta="Data (DD/MM/AAAA) [ENTER para hoje]: "):#salvar data nos arquivos
    while True:
        data = input(pergunta)
        data = data.strip()
        if data == "":
            return datetime.now().strftime("%d/%m/%Y")
        try:
            datetime.strptime(data, "%d/%m/%Y")
        except ValueError:
            print("Data Errada")
            continue

        return data


def formatar_moeda(valor):#saida de valor monetario pradronizado
    texto = f"{valor:,.2f}"
    texto = texto.replace(",", "X").replace(".", ",").replace("X", ".")
    return f"R$ {texto}"


def exibir_cabecalho(titulo):#saida padronizada
    print("=" * 50)
    print(titulo.upper())
    print("=" * 50)