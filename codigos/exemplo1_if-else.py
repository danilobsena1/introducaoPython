print('Escolha uma opção:\n1 = Guilherme\n2 = João \n3 = Maria\n')
opcao = input("Opção: ")

if opcao == '1':
    print('Guilherme')
elif opcao == '2':
    print('João')
elif opcao < '1' or opcao > '3':
    print('Opção invalida!')
else:
    print('Maria')