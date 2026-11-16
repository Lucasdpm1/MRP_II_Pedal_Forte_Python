import utils
import persistencia
import menu
import itens
import estrutura
import estoque
import mps
import capacidade
import ordens
import mrp
import custos
import relatorios
import graficos      

dados=persistencia.carregar_tudo()   
print("\n")
while True:
    menu.menu()   
    opcao=utils.ler_opcao("Escolha uma opcao: ",["0","1","2","3","4","5","6","7","8"])
    print("\n")

    if(opcao=="0"): 
        break

    elif(opcao=="1"):   
        while True:
            menu.menu_cadastros()
            opcao_cadastro=utils.ler_opcao("Opcao: ",["0","1","2","3","4","5","6","7","8","9"])
            print("\n")
            if(opcao_cadastro=="0"):
                break
            elif(opcao_cadastro=="1"):
                itens.cadastrar_item(dados)
            elif(opcao_cadastro=="2"):
                itens.listar_dados(dados)
            elif(opcao_cadastro=="3"):
                itens.alterar_item(dados)
            elif(opcao_cadastro=="4"):
                estrutura.adicionar_componente(dados)
            elif(opcao_cadastro=="5"):
                codigo=utils.ler_codigo_item()
                if(codigo not in dados["itens"]):
                    print("Item nao encontrado")
                else:
                    estrutura.listar_componentes(dados,codigo)
            elif(opcao_cadastro=="6"):
                codigo=utils.ler_codigo_item()
                if(codigo not in dados["itens"]):
                    print("Item nao encontrado")
                else:
                    estrutura.exibir_estrutura(dados,codigo,0,1)    
            elif(opcao_cadastro=="7"):
                capacidade.cadastrar_centro(dados)
            elif(opcao_cadastro=="8"):
                capacidade.listar_centros(dados)
            elif(opcao_cadastro=="9"):
                capacidade.definir_roteiro(dados)
            print("\n")

    elif(opcao=="2"):    #estoque
        while True:
            menu.menu_estoque()
            opcao_estoque=utils.ler_opcao("Opcao: ",["0","1","2","3"])
            print("\n")
            if(opcao_estoque=="0"):
                break
            elif(opcao_estoque=="1"):
                estoque.menu_movimentar(dados)
            elif(opcao_estoque=="2"):
                codigo=utils.ler_codigo_item()
                if(codigo not in dados["itens"]):
                    print("Item nao encontrado")
                else:
                    print("Saldo:",estoque.consultar_saldo(dados,codigo))
                    estoque.verificar_alerta(dados,codigo)
            elif(opcao_estoque=="3"):
                codigo=utils.ler_codigo_item()
                if(codigo not in dados["itens"]):
                    print("Item nao encontrado")
                else:
                    estoque.exibir_historico(dados,codigo)   
            print("\n")

    elif(opcao=="3"):   
        while True:
            menu.menu_mps()
            opcao_mps=utils.ler_opcao("Opcao: ",["0","1","2"])
            print("\n")
            if(opcao_mps=="0"):
                break
            elif(opcao_mps=="1"):
                mps.cadastrar_demanda(dados)
            elif(opcao_mps=="2"):
                mps.exibir_mps(dados)
            print("\n")

    elif(opcao=="4"):    #mrp
        while True:
            menu.menu_mrp()
            opcao_mrp=utils.ler_opcao("Opcao: ",["0","1","2"])
            print("\n")
            if(opcao_mrp=="0"):
                break
            elif(opcao_mrp=="1"):
                mrp.executar_mrp(dados)
            elif(opcao_mrp=="2"):
                codigo=utils.ler_codigo_item()
                if(codigo not in dados["itens"]):
                    print("Item nao encontrado")
                else:
                    mrp.exibir_registro_mrp(dados,codigo)
            print("\n")

    elif(opcao=="5"):   
        while True:
            menu.menu_ordens()
            opcao_ordens=utils.ler_opcao("Opcao: ",["0","1","2","3","4","5"])
            print("\n")
            if(opcao_ordens=="0"):
                break
            elif(opcao_ordens=="1"):
                ordens.listar_ordem(dados)
            elif(opcao_ordens=="2"):
                numero=utils.ler_mensagem("Numero da ordem: ").upper()
                ordens.firmar_ordem(dados,numero)
            elif(opcao_ordens=="3"):
                numero=utils.ler_mensagem("Numero da ordem: ").upper()
                ordens.liberar_ordem(dados,numero)
            elif(opcao_ordens=="4"):
                numero=utils.ler_mensagem("Numero da ordem: ").upper()
                ordens.apontar_producao(dados,numero)
            elif(opcao_ordens=="5"):
                numero=utils.ler_mensagem("Numero da ordem: ").upper()
                ordens.encerrar_ordem(dados,numero)
            print("\n")

    elif(opcao=="6"):   
        while True:
            menu.menu_crp()
            opcao_crp=utils.ler_opcao("Opcao: ",["0","1"])
            print("\n")
            if(opcao_crp=="0"):
                break
            elif(opcao_crp=="1"):
                centro=utils.ler_mensagem("Centro: ").upper()
                capacidade.exibir_crp(dados,centro)
            print("\n")

    elif(opcao=="7"):    #custo padrao
        while True:
            menu.menu_custos()
            opcao_custos=utils.ler_opcao("Opcao: ",["0","1"])
            print("\n")
            if(opcao_custos=="0"):
                break
            elif(opcao_custos=="1"):
                codigo=utils.ler_codigo_item()
                if(codigo not in dados["itens"]):
                    print("Item nao encontrado")
                else:
                    custos.exibir_custo(dados,codigo)
            print("\n")

    elif(opcao=="8"):   
        while True:
            menu.menu_relatorios()
            opcao_relatorio=utils.ler_opcao("Opcao: ",["0","1","2","3","4","5","6"])
            print("\n")
            if(opcao_relatorio=="0"):
                break
            elif(opcao_relatorio=="1"):
                relatorios.exportar_estoque_csv(dados)
            elif(opcao_relatorio=="2"):
                relatorios.exportar_ordens_csv(dados)
            elif(opcao_relatorio=="3"):
                graficos.grafico_posicao_estoque(dados)
            elif(opcao_relatorio=="4"):
                codigo=utils.ler_codigo_item()
                if(codigo not in dados["itens"]):
                    print("Item nao encontrado")
                else:
                    graficos.grafico_estoque_projetado(dados,codigo)
            elif(opcao_relatorio=="5"):
                graficos.grafico_ordens_por_semana(dados)
            elif(opcao_relatorio=="6"):
                centro=utils.ler_mensagem("Centro: ").upper()
                graficos.grafico_carga_capacidade(dados,centro)
            print("\n")

persistencia.salvar_tudo(dados)    
print("Obrigado Por Usar.")