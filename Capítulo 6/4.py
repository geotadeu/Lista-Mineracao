#Faça um programa que liste para o usuário um menu com quatro opções, sendo cada
#uma referente à uma operação matemática básica. Após o usuário ter escolhido a
#opção, leia dois valores e realiza a operação selecionada.


print('-'*30)
print('Calculadora')
print('1 - Adição')
print('2 - Subtração')
print('3 - Multiplicação')
print('4 - Divisão')
print('-'*30)

op = int(input('Informe a operação desejada: '))
n1 = float(input('Informe o primeiro número: '))
n2 = float(input('Informe o segundo número: '))

if op == 1:
    print('O resultado da soma é: ', n1+n2)
elif op == 2:
    print('O resultado da subtração é: ', n1-n2)
elif op == 3:
    print('O resultado da multiplicação é: ', n1*n2)
elif op == 4:
    print('O resultado da divisão é: ', n1/n2)
else:
    print('Opção informada é inválida')