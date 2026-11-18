# MRP II - Pedal Forte Bicicletas

Trabalho 2 de Programação em Python, Engenharia de Computação, CEFET-MG Campus Divinópolis. Professor Guido Pantuza.

Aluno: Lucas Domingos Pereira

Sistema em modo texto feito para a fábrica fictícia Pedal Forte Bicicletas. Dá pra cadastrar itens e a estrutura de produto, controlar o estoque, informar a demanda do plano mestre, rodar o MRP, acompanhar as ordens de produção e de compra, ver a carga dos centros de trabalho, calcular o custo padrão e gerar gráficos.

## Como executar

Precisa do Python 3.10 ou mais novo, no Linux.

Clonar o repositório, entrar na pasta e instalar o matplotlib, que é usado nos gráficos:

```
pip install matplotlib
```

Se a janela do gráfico não abrir, instalar também o tkinter com `sudo apt install python3-tk`.

Depois é só rodar:

```
python main.py
```

Na pasta `data/` já tem uma base de demonstração (2 produtos acabados, 2 semiacabados, 8 matérias-primas e 2 centros de trabalho), então dá pra testar sem cadastrar nada. Os dados são lidos quando o programa abre e gravados depois de cada cadastro ou alteração e também quando ele fecha.

## Pastas

```
MRP2_PedalForte/
    main.py          ponto de entrada e navegação entre os menus
    menu.py          só os prints dos menus
    itens.py         cadastro de itens
    estrutura.py     BOM e árvore indentada
    estoque.py       movimentações, saldo e histórico (kardex)
    mps.py           plano mestre de produção
    mrp.py           cálculo do MRP
    ordens.py        OPs, OCs e apontamento
    capacidade.py    centros, roteiros e carga x capacidade
    custos.py        custo padrão
    relatorios.py    exportação em CSV
    graficos.py      gráficos (matplotlib)
    persistencia.py  leitura e gravação dos arquivos
    utils.py         leitura e validação das entradas, formatação
    data/            arquivos de dados
    graficos/        PNGs gerados (a pasta é criada sozinha)
    README.md
```

## Como usar

O menu principal tem 8 opções: cadastros, estoque, plano mestre (MPS), executar MRP, ordens, carga x capacidade, custo padrão e relatórios (CSV e gráficos). Cada uma abre um submenu, e a opção 0 volta.

Pra testar um ciclo completo: cadastrar a demanda de um produto no MPS, executar o MRP, firmar e liberar uma ordem de produção, apontar a produção e depois olhar o estoque.

Alguns detalhes:

- Os códigos dos itens são do tipo PA-001, SA-010 e MP-100. O tipo do item vem do próprio código.
- A data é DD/MM/AAAA. Apertando ENTER fica a data de hoje.
- Os CSV exportados vão pra pasta `data/` e os gráficos pra pasta `graficos/`.
- O gráfico de estoque projetado só funciona depois de executar o MRP.

## Como os dados ficam guardados

Tudo fica num dicionário chamado `dados`, que vai passando de função em função. Cada chave dele tem um arquivo na pasta `data/`: itens.json, estrutura.json, estoque.json, movimentos.csv, centros.json, roteiros.json, mps.json e ordens.json.

Em itens e estoque a chave é o código do item. A estrutura guarda, pra cada item pai, uma lista com os componentes e a quantidade de cada um. As ordens e os movimentos são listas de dicionários.

## Decisões de projeto

Usei funções e dicionários, sem POO, porque achei mais simples de explicar.

O `menu.py` só tem os prints. Os laços de navegação ficam no `main.py`.

As semanas nos dicionários são texto ("1" a "8"), porque o JSON só aceita texto como chave. Já nas listas do MRP e da carga usei 9 posições e não uso a posição 0, assim a semana 3 fica na posição 3.

O tipo do item (PA, SA ou MP) é tirado do código na hora do cadastro, pra não dar conflito entre os dois.

A função que registra movimento de estoque não pergunta nada pro usuário, pra poder ser chamada também pelo apontamento de produção. No apontamento o sistema olha se tem todos os componentes antes de baixar qualquer um, pra não deixar o estoque pela metade.

Ordem atrasada não é um status. É um campo à parte (`atrasada`), porque o status só anda entre PLANEJADA, FIRME, LIBERADA e ENCERRADA. Quando a liberação cai antes da semana 1 a ordem é criada e marcada como atrasada, aparece na lista de exceções, mas não entra nas liberações que servem de base pro cálculo dos componentes.

Entrada e saída de estoque só aceitam quantidade maior que zero. Só o ajuste aceita número negativo.

Na carga dos centros (RN09) somei as OPs na semana em que elas são liberadas, de qualquer status. Encerrar uma ordem de compra só muda o status dela. A entrada da matéria-prima no estoque é feita pelo menu de estoque, com o número da nota no documento.

## Requisitos funcionais

- RF01: menu.py e main.py
- RF02: itens.py
- RF03: estrutura.py (adicionar_componente e exibir_estrutura)
- RF04: estoque.py (registrar_movimento)
- RF05: estoque.py (consultar_saldo, exibir_historico e verificar_alerta)
- RF06: capacidade.py (cadastrar_centro e definir_roteiro)
- RF07: mps.py
- RF08: mrp.py (executar_mrp e exibir_registro_mrp)
- RF09: mrp.py e ordens.py (criar_ordem)
- RF10: ordens.py (firmar_ordem, liberar_ordem e encerrar_ordem)
- RF11: ordens.py (apontar_producao)
- RF12: capacidade.py (calcular_carga e exibir_crp)
- RF13: custos.py
- RF14: relatorios.py
- RF15: persistencia.py
- RF16: graficos.py

## Regras de negócio

- RN01: utils.py (validar_codigo_item) e itens.py
- RN02: estoque.py (registrar_movimento)
- RN03: estrutura.py (validar_componente)
- RN04 a RN08: mrp.py
- RN09: capacidade.py (calcular_carga)
- RN10: estoque.py. Os movimentos só são acrescentados no histórico e nunca apagados, correção é feita por ajuste.