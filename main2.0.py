
funcionario = {}

# Função para cadastrar funcionários
def Cadastrar():
    print("_" * 55)
    print("\t\t   Cadastrar Funcionario")
    print("-" * 55)
    
    codigo_funcao = int(input("Insira o código da função (101 para Vendedor, 102 para Administrativo): "))
    while codigo_funcao not in [101, 102]:
        codigo_funcao = int(input("Código inválido. Insira o código da função (101 para Vendedor, 102 para Administrativo): "))

    matricula =int(input("Insira a matrícula: "))
    nome = input("Digite o Nome do funcionário: ")
    faltas = 0
    if codigo_funcao == 101:
        salario_bruto = 1500
        salario_liquido = 1500
    else:
        salario_bruto = 6950
        salario_liquido = 6950

    funcionario[matricula] = {
        'nome': nome,
        'codigo_funcao': codigo_funcao,
        'faltas': faltas,
        'Salario_liquido': salario_liquido,
        'salario_bruto': salario_bruto
    }
    print("_" * 55)
    print("\t   Cadastro Bem Sucedido")
    print("-" * 55)
    print("Matrícula\tNome\tCódigo Função\tFaltas\tSalário Líquido\tSalário Bruto")

    matricula_cadastrada = matricula
    cadastro = funcionario[matricula_cadastrada]
    print(f"{matricula_cadastrada}\t{cadastro['nome']}\t{cadastro['codigo_funcao']}\t\t{cadastro['faltas']}\t{cadastro['Salario_liquido']}\t{cadastro['salario_bruto']}\n")

    print("[1]Excluir\n[2]Voltar")
    num = int(input("Opção desejada: "))
    if num == 1:
        del funcionario[matricula_cadastrada]
        print("Deletado com sucesso")
    if num == 2:
        return

# Função para remover funcionários
def Remover():
    print("_" * 55)
    print("\t\t   Remover Funcionario")
    print("-" * 55)
    excluir = input("Digite a matrícula do funcionário: ")
    if excluir in funcionario:
        cadastro = funcionario[excluir]
        print("Matrícula\tNome\tCódigo Função\tFaltas\tSalário Bruto")
        print(f"{excluir}\t{cadastro['nome']}\t{cadastro['codigo_funcao']}\t\t{cadastro['faltas']}\t{cadastro['salario_bruto']}")
        print("[1]Confirmar\n[0]Voltar")
        confirmacao = int(input("Opção Desejada: "))

        if confirmacao == 1:
            del funcionario[excluir]
            print("_" * 55)
            print(f"Funcionário {excluir} removido com sucesso.")
            print("-" * 55)
        if confirmacao == 0:
            return
    else:
        print("Funcionário não encontrado")

# Função para exibir um ou todos os funcionários
def buscarFuncionario(matricula=None):
    print("_" * 55)
    print("\t   Funcionários Cadastrados")
    print("-" * 55)
    
    print("Matrícula\tNome\tCódigo Função\tSalário Bruto\tFaltas\tSalário Líquido")
    
    if matricula:
        if matricula in funcionario:
            cadastro = funcionario[matricula]
            salario_bruto = cadastro['salario_bruto']
            faltas = cadastro['faltas']
            desconto_faltas = (salario_bruto / 30) * faltas
            salario_com_faltas = salario_bruto - desconto_faltas
            
            if cadastro['codigo_funcao'] == 101:  # Vendedor
                comissao = 0 
                salario_com_faltas += comissao
            
            # Determinar o imposto
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
            
            print(f"{matricula}\t\t{cadastro['nome']}\t{cadastro['codigo_funcao']}\t\t{salario_bruto}\t\t{faltas}\t{salario_liquido:.2f}")
            return
        else:
            print("Funcionário não encontrado.")
    else:
        for matricula, cadastro in funcionario.items():
            salario_bruto = cadastro['salario_bruto']
            faltas = cadastro['faltas']
            desconto_faltas = (salario_bruto / 30) * faltas
            salario_com_faltas = salario_bruto - desconto_faltas
            
            if cadastro['codigo_funcao'] == 101:  # Vendedor
                comissao = 0 
                salario_com_faltas += comissao
            
            # Determinar a alíquota do imposto
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
            
            print(f"{matricula}\t\t{cadastro['nome']}\t{cadastro['codigo_funcao']}\t\t{salario_bruto}\t\t{faltas}\t{salario_liquido:.2f}")
# Função para inserir faltas
def faltas():
    print("_" * 55)
    print("\t   Painel De Faltas")
    print("-" * 55)

    matricula =int(input("Digite a Matrícula do funcionário: "))

    if matricula in funcionario:
        cadastro = funcionario[matricula]
        cadastro['faltas'] += 1  # Incrementa as faltas
       

        if cadastro['codigo_funcao'] == 101:
            cadastro['Salario_liquido'] -= 50  # Reduz o salário líquido
        if cadastro['codigo_funcao'] == 102:
            cadastro['Salario_liquido'] -= 232  # Reduz o salário líquido
        
        buscarFuncionario(matricula)
        return
# calcular o salario de um unico funcionario
def declarar_folha_pagamento():
    global funcionario
    print("_" * 55)
    print("\t\t   Folha De Pagamento")
    print("-" * 55)
    matricula = int(input("Digite a matrícula do funcionário: "))
    if matricula in funcionario:
        cadastro = funcionario[matricula]
        salario_bruto = cadastro['salario_bruto']
        faltas = cadastro['faltas']
        
        desconto_faltas = (salario_bruto / 30) * faltas
        salario_com_faltas = salario_bruto - desconto_faltas
        
        if cadastro['codigo_funcao'] == 101: 
            comissao = float(input("Digite o volume de vendas do mês: ")) * 0.09
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
        
        print("\nInformações do Funcionário:")
        print("-"*55)
        print(f"Matrícula:\t\t\t {matricula}")
        print("-"*55)
        print(f"Nome:\t\t\t\t {cadastro['nome']}")
        print("-"*55)
        print(f"Código da Função:\t\t {cadastro['codigo_funcao']}")
        print("-"*55)
        print(f"Faltas:\t\t\t\t {cadastro['faltas']}")
        print("-"*55)
        print(f"Salário Bruto:\t\t\t {salario_bruto:}")
        print("-"*55)
        print(f"Comissão:\t\t\t {comissao}")
        print("-"*55)
        print(f"Desconto por Faltas:\t\t {desconto_faltas:.2f}")
        print("-"*55)
        print(f"Salário após Faltas:\t\t {salario_com_faltas:.2f}")
        print("-"*55)
        print(f"Percentual de Imposto:\t\t {imposto * 100:.2f}%")
        print("-"*55)
        print(f"Salário Líquido:\t\t {salario_liquido:.2f}\n")
    else:
        print("Funcionário não encontrado.")

#tela de inicio
while True:
    print("\n[1]Cadastrar\n[2]Remover Funcionario\n[3]Exibir funcionários\n[4]Inserir falta\n[5]Folha de pagamento\n[0]Sair")
    num_tela = int(input("Opção Desejada: "))
    
    if num_tela == 1:
        Cadastrar()
    elif num_tela == 2:
        Remover()
    elif num_tela == 3:
        print("\n[1]Buscar unico funcionario\n[2]Buscar todos funcionarios")
        opção_buscar=int(input("Opçao Desejada:"))
        if opção_buscar==1:
            matricula=int(input("\nDigite a matricula: "))
            buscarFuncionario(matricula)
        else:
            buscarFuncionario()
        
    elif num_tela == 4:
        
        faltas()
    elif num_tela == 5:
        declarar_folha_pagamento()
    elif num_tela == 0:
        break
    else:
        print("Opção inválida. Tente novamente.")
