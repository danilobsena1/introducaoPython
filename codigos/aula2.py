# a = 10
# b = 4

a = int(input("Digite o 1° valor: "))
b = int(input("Digite o 2° valor:  "))

soma = a + b
subtracao = a - b
multiplicacao = a * b
divisao = a / b
restoDivisao = a % 2

print("Soma: " + str(soma))  # A variavel soma foi convertida para string

print("Soma: {}. Subtração: {}".format(soma, subtracao))
# ou
print("Soma: {soma} Subtração: {subtracao}".format(soma=soma, subtracao=subtracao))
print()
print("Soma: {soma} \nSubtração: {subtracao} \nMultiplição: {multiplicacao} "
      "\nDivisão: {divisao} \nRestoDivisão {restoDivisao}".format(soma=soma, subtracao=subtracao,
                                                                  multiplicacao=multiplicacao, divisao=divisao,
                                                                  restoDivisao=restoDivisao))
