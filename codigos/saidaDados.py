''' print("Hello World!")
print('Hello world!')

print("Helo world\nSegundo print")

print("Usando\ttabulação \n")

print("------------------\n") '''

print("############## VARIAVEIS ################################")

print("variaveis em python não são identificadas pelo tipo, a propria linguagem faz a conversão automaticamente")

nome = 'Danilo'
print("nome = 'Danilo'")
print(nome)
print("---------------------------------------------------------")
print("IDENTIFICANDO TIPOS DE VARIAVEIS: ")
nome = 'Danilo'
idade = 30
altura = 1.78
status_emprego = True
salario = 1500.00

print(type(nome))
print(type(idade))
print(type(altura))
print(type(status_emprego))
print(type(salario))
print()

print(nome, 'tem', idade, 'anos', 'e', altura, 'de altura, trabalha?:', status_emprego, ', o salario é de R$:', salario)

#outra forma de exibir os dados:
'''
Quando utilizamos o + para concatenação o python não consegue converter inteiros e floats automaticamente para string,
 nesse caso é necessario converter os valores para string: 
'''

print(nome + ' tem ' + str(idade) + ' anos e ' + str(altura) + ' de altura, trabalha?: ' + str(status_emprego) + ', o salario é de R$: ' + str(salario))
