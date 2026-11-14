from datetime import datetime


def ler_inteiro(pergunta="Qual Seu numero: "):
    while True:
        numero = input(pergunta)
        numero = numero.strip()
        try:
            numero = int(numero)
        except ValueError:
            print("Numero Errado")
            continue

        return numero


def ler_float(pergunta="Qual Seu Numero: ", minimo=None):
    while True:
        numero = input(pergunta)
        numero = numero.strip().replace(",", ".")
        try:
            numero = float(numero)
        except ValueError:
            print("Numero Errado")
            continue
        if minimo is not None and numero < minimo:
            print(f"O valor deve ser no minimo {minimo}")
            continue

        return numero


def ler_mensagem(pergunta):
    while True:
        mensagem = input(pergunta)
        mensagem = mensagem.strip()
        if mensagem == "":
            print("Mensagem Vazia")
            continue

        return mensagem


def ler_opcao(pergunta, opcoes_validas):
    opcoes = [op.upper() for op in opcoes_validas]
    while True:
        opcao = input(pergunta)
        opcao = opcao.strip().upper()
        if opcao not in opcoes:
            print("Opcao Errada")
            continue

        return opcao


def validar_codigo_item(codigo):
    partes = codigo.split("-")
    if len(partes) != 2:
        return False
    if partes[0] not in ["PA", "SA", "MP"]:
        return False
    if not partes[1].isdigit():
        return False

    return True


def ler_codigo_item(pergunta="Codigo do item: "):
    while True:
        codigo = input(pergunta)
        codigo = codigo.strip().upper()
        if not validar_codigo_item(codigo):
            print("Codigo Errado (use Tipo-Numero, ex: PA-001)")
            continue

        return codigo


def ler_data(pergunta="Data (DD/MM/AAAA) [ENTER para hoje]: "):
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


def formatar_moeda(valor):
    texto = f"{valor:,.2f}"
    texto = texto.replace(",", "X").replace(".", ",").replace("X", ".")
    return f"R$ {texto}"


def exibir_cabecalho(titulo):
    print("=" * 50)
    print(titulo.upper())
    print("=" * 50)