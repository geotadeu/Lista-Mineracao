#Faça um programa que receba um número inteiro n e o fatore.

numero = int(input('Informe o número para ser fatorado'))

resultado = 1
for n in range(1,numero+1):
    resultado *= n

print(resultado)