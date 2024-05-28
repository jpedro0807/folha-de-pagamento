
funcionarios = {}


# Def responsável vela verificação de todas entradas do sistema
def verificação(message, valor):#message é o paramentro q vai receber a msg e paramentro  valor é a variavel q vai receber o tipo de dado q eu coloquei no final de cada input
        while True:
            try:
                valor = valor(input(message))# se ele conseguir transformar a msg sem nenhum erro ele return valor
                return valor
#caso der algum erro com a msg q n é do tipo valor ele vai retornar esse print e só vai sair do loop caso o usuario digite um numero correto com a do tipo da variavel declarado em valor  
            except ValueError:
                print("Entrada inválida. Por favor, tente novamente.\n")


# def para inserir funcionários
def inserir_funcionario(funcionarios, matricula, nome, codigo_funcao, faltas, salario_bruto, vendas=0):
    
    
    if matricula in funcionarios:
        print("Funcionário com esta matrícula já existe.")
        return
    funcionarios[matricula] = {
        'nome': nome,
        'codigo_funcao': codigo_funcao,
        'faltas': faltas,
        'salario_bruto': salario_bruto,
        'vendas': vendas
        
    }
    print("-" * 55)
    print(f"Funcionário {nome} inserido com sucesso.")
    print("_" * 55)





# Def para remover funcionários
def remover_funcionario(funcionarios, matricula):
    if matricula in funcionarios:
        del funcionarios[matricula]
        print(f"Funcionário {matricula} removido com sucesso.")
    else:
        print("Funcionário não encontrado.")


# Def resposável para determinar a folha de pagamento de um funcionário
def determinar_folha_pagamento(funcionarios, matricula,vendas):
    
    print("_" * 55)
    print("\t\t   Folha De Pagamento")
    print("-" * 55)
    if matricula in funcionarios:
        cadastro = funcionarios[matricula]
        salario_bruto = cadastro['salario_bruto']
        faltas = cadastro['faltas']
        
        desconto_faltas = (salario_bruto / 30) * faltas
        salario_com_faltas = salario_bruto - desconto_faltas
        comissao=0
        if cadastro['codigo_funcao'] == 101: 
            vendas = verificação("Digite o volume de vendas do mês: ",float)
            comissao=vendas*0.09
            salario_com_faltas += comissao
        
        
        if salario_com_faltas <= 2259.20:
            imposto = 0.0
        elif salario_com_faltas <= 2828.65:
            imposto = 0.075
        elif salario_com_faltas <= 3751.05:
            imposto = 0.15
        elif salario_com_faltas <= 4664.68:
            imposto = 0.225
        else:
            imposto = 0.275
        
        salario_liquido = salario_com_faltas * (1 - imposto)

        valor_imposto=salario_com_faltas*imposto
        print("\nInformações do Funcionário:")
        print("-"*55)

        print(f"Matrícula:\t\t\t {matricula}")
        print(f"Nome:\t\t\t\t {cadastro['nome']}")
        print(f"Código da Função:\t\t {cadastro['codigo_funcao']}")
        
        print("-"*55)

        print(f"Vendas:\t\t\t\t {vendas}")
        print(f"Comissão:\t\t\t {comissao}")
        

        print("-"*55)
        
        print(f"Percentual de Imposto:\t\t {imposto * 100:.2f}%")
        print(f"Valor do Imposto:\t\t {valor_imposto}")

        print("-"*55)

        print(f"Faltas:\t\t\t\t {cadastro['faltas']}")
        print(f"Desconto por Faltas:\t\t {desconto_faltas:.2f}")
        print(f"Salário após Faltas:\t\t {salario_com_faltas:.2f}")

        print("-"*55)

        print(f"Salário Bruto:\t\t\t {salario_bruto:}")
        print(f"Salário Líquido:\t\t {salario_liquido:.2f}\n")
    else:
        print("Funcionário não encontrado.")





def gerar_relatorio(funcionarios):
    print("Matrícula | Nome | Código da Função | Salário Bruto | Salário Líquido")
    for matricula, info in funcionarios.items():
        salario_liquido, imposto = calcular_salario_liquido(info)
        print(f"{matricula} | {info['nome']} | {info['codigo_funcao']} | {info['salario_bruto']} | {salario_liquido}")


def calcular_salario_liquido(funcionario):
    
    salario_bruto = funcionario['salario_bruto']
    faltas = funcionario['faltas']
    
    desconto_faltas = (salario_bruto / 30) * faltas
    salario_com_faltas = salario_bruto - desconto_faltas
    
    if funcionario['codigo_funcao'] == 101:  
        comissao = funcionario['vendas'] * 0.09
        salario_bruto += comissao
    
    if salario_com_faltas <= 2259.20:
        imposto = 0.0
    elif salario_com_faltas <= 2828.65:
        imposto = 0.075
    elif salario_com_faltas <= 3751.05:
        imposto = 0.15
    elif salario_com_faltas <= 4664.68:
        imposto = 0.225
    else:
        imposto = 0.275
    
    salario_liquido = salario_com_faltas * (1 - imposto)
    
    return salario_liquido, imposto * 100

#Def responsável para procurar o funcionario com maior salario liquido do mês
def maior_salario_liquido(funcionarios):
    if not funcionarios:
        print("Nenhum funcionário cadastrado.")
        return
    
    salario_maximo = -1
    func_max = None
    for matricula, info in funcionarios.items():
        salario_liquido, imposto = calcular_salario_liquido(info)
        if salario_liquido > salario_maximo:
            salario_maximo = salario_liquido
            func_max = (matricula, info['nome'], info['codigo_funcao'], info['salario_bruto'], imposto, salario_liquido)

    print("\nFuncionário com maior salário líquido:\n")
    

    print("Matrícula | Nome | Código da Função | Salário bruto |Imposto | Salário Líquido")
    print(f"{func_max[0]}\t  | {func_max[1]}\t | {func_max[2]}\t\t    | {func_max[3]}\t    | {func_max[4]}    | {func_max[5]}")




#Def responsável para procurar o funcionario com maior numero de faltas do mês
def maior_faltas(funcionarios,matricula):
    print("_" * 55)
    print("\t\t   Campeão em faltas")
    print("-" * 55)
    if not funcionarios:
        print("Nenhum funcionário cadastrado.")
        return
    
    max_faltas = -1
    func_max_faltas = None
    for matricula, info in funcionarios.items():
        if info['faltas'] > max_faltas:
            max_faltas = info['faltas']
            desconto_faltas = (info['salario_bruto'] / 30) * info['faltas']
            func_max_faltas = (matricula, info['nome'], info['codigo_funcao'], info['faltas'], desconto_faltas)

    print("Matrícula | Nome | Código da Função | Número de Faltas  | Desconto no Salário")
    print(f"{func_max_faltas[0]}\t  | {func_max_faltas[1]}\t | {func_max_faltas[2]}\t\t    |{func_max_faltas[3]}\t\t\t| {func_max_faltas[4]}")
    

def Adicionar_faltas(funcionarios, matricula):
    if matricula in funcionarios:
        cadastro = funcionarios[matricula]
        cadastro['faltas'] += 1  

        desconto_faltas = (cadastro['salario_bruto'] / 30) * cadastro['faltas']
        cadastro['salario_liquido'] = cadastro['salario_bruto'] - desconto_faltas

        if cadastro['codigo_funcao'] == 101:
            cadastro['salario_liquido'] -= 50 
        elif cadastro['codigo_funcao'] == 102:
            cadastro['salario_liquido'] -= 232  

        
        print(f"Funcionário {cadastro['nome']} recebeu uma falta.")
        
    else:
        print("Funcionário não encontrado")

#def responsavel pela interface principal
def menu():
    while True:
        print("_" * 55)
        print("\t\t   Tela Inicial")
        print("-" * 55)
        print("[1]. Inserir Funcionário")
        print("[2]. Remover Funcionário")
        print("[3]. Determinar Folha de Pagamento de um Funcionário")
        print("[4]. Gerar Relatório de Todos os Funcionários")
        print("[5]. Imprimir Funcionário com Maior Salário Líquido")
        print("[6]. Imprimir Funcionário com Maior Número de Faltas")
        print("[7]. Inserir faltas")
        print("[0]. Sair")
        
        opcao = verificação("Escolha uma opção: ",int)
        
        if opcao == 1:
            print("_" * 55)
            print("\t\t   Cadastrar cliente")
            print("-" * 55)
            codigo_funcao = verificação("(101 para Vendedor, 102 para Administrativo)\nCódigo da Função : ",int)
            while codigo_funcao not in [101, 102]:
                codigo_funcao = verificação("Código inválido. Insira o código da função (101 para Vendedor, 102 para Administrativo): ",int)

            matricula = verificação("Matrícula: ",int)
            nome = input("Nome: ")
            faltas = verificação("Número de Faltas: ",int)

            if codigo_funcao == 101:
                salario_bruto = 1500
                
                vendas = verificação("Volume de Vendas: ",float)
                inserir_funcionario(funcionarios, matricula, nome, codigo_funcao, faltas, salario_bruto, vendas)

            elif codigo_funcao == 102:
                vendas=0
                salario_bruto = verificação("Salário Bruto: ",float)
                if 2150>+salario_bruto<=6950:
                    salario_bruto = verificação("Salario indisponivel.\nSalário Bruto: ",float)
                inserir_funcionario(funcionarios, matricula, nome, codigo_funcao, faltas, salario_bruto,vendas)

            else:
                print("Código de função inválido.")
        
        elif opcao == 2:
            matricula = verificação("Matrícula: ",int)
            remover_funcionario(funcionarios, matricula)
            
        elif opcao == 3:
            matricula = verificação("Matrícula: ",int)
            
            determinar_folha_pagamento(funcionarios, matricula,vendas)
        
        elif opcao == 4:
            gerar_relatorio(funcionarios)
        
        elif opcao == 5:
            maior_salario_liquido(funcionarios)
        
        elif opcao == 6:
            maior_faltas(funcionarios)

        elif opcao==7:
            print("_" * 55)
            print("\t   Painel De Faltas")
            print("-" * 55)
            matricula = verificação("Matrícula: ",int)
            Adicionar_faltas(funcionarios,matricula)

        elif opcao == 0:
            break
        
        else:
            print("Opção inválida. Tente novamente.")


menu()
