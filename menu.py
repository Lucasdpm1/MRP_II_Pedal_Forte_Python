def menu():
    print("==================================================")
    print("MRP II - PEDAL FORTE BICICLETAS")
    print("==================================================")
    print("1. Cadastros (itens, estrutura, centros, roteiros)")
    print("2. Estoque (movimentar, saldo, kardex)")
    print("3. Plano Mestre de Producao (MPS)")
    print("4. Executar MRP")
    print("5. Ordens de producao e de compra")
    print("6. Carga x capacidade (CRP)")
    print("7. Custo padrao dos produtos")
    print("8. Relatorios (exportar CSV)")
    print("0. Sair")

def menu_cadastros():
    print("1. Cadastrar item")
    print("2. Listar itens")
    print("3. Alterar item")
    print("4. Adicionar componente na estrutura")
    print("5. Listar componentes de um item")
    print("6. Exibir estrutura do produto")
    print("7. Cadastrar centro de trabalho")
    print("8. Listar centros")
    print("9. Definir roteiro")
    print("0. Voltar")

def menu_estoque():
    print("1. Movimentar estoque")
    print("2. Consultar saldo")
    print("3. Historico (kardex) do item")
    print("0. Voltar")

def menu_mps():
    print("1. Cadastrar demanda")
    print("2. Exibir MPS")
    print("0. Voltar")

def menu_mrp():
    print("1. Executar MRP")
    print("2. Exibir registro MRP de um item")
    print("0. Voltar")

def menu_ordens():
    print("1. Listar ordens")
    print("2. Firmar ordem")
    print("3. Liberar ordem")
    print("4. Apontar producao")
    print("5. Encerrar ordem")
    print("0. Voltar")

def menu_crp():
    print("1. Exibir carga x capacidade de um centro")
    print("0. Voltar")

def menu_custos():
    print("1. Exibir custo padrao de um item")
    print("0. Voltar")

def menu_relatorios():
    print("1. Exportar estoque (CSV)")
    print("2. Exportar ordens (CSV)")
    print("3. Grafico: posicao de estoque")
    print("4. Grafico: estoque projetado de um item")
    print("5. Grafico: ordens por semana")
    print("6. Grafico: carga x capacidade de um centro")
    print("0. Voltar")