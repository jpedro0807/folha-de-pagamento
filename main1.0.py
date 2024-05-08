quant_funcionario=int(input("digite quantos funcionarios q digitar "))

funcionario={}
for i in range(quant_funcionario):
 codigo_funcao=int(input("codigo da função "))
 if codigo_funcao==101:
    matricula=input("digite a matricula ")
    nome=input("Digite o Nome ")
    faltas=input("numero de faltas ")
    salario_bruto=1500
    funcionario[matricula]={
                                'nome':nome,
                                'codigo_funcao':codigo_funcao,
                                'faltas':faltas,
                                'salario_bruto':salario_bruto}
for matricula in funcionario:
    cadastro=funcionario[matricula]
    print(f"{matricula}\t\t{cadastro['nome']}\t\t{cadastro['codigo_funcao']}\t\t{cadastro['faltas']}\t\t{cadastro['salario_bruto']}")

dict_intems = funcionario.items()
print(dict_intems)