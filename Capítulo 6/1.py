#Faça um código que receba um número n do usuário e imprima os n primeiros
#números da sequência de Fibonacci.

n = int(input('Quantos termos da sequencia de Fibonacci você quer mostrar? '))
t1 = 0
t2 = 1

print('{} → {}' .format(t1,t2), end = '')
cont = 3
while cont <= n:
    t3 = t1 +t2
    print(' → {}'.format(t3), end = '')
    t1 =t2
    t2 = t3
    cont += 1
print(' → FIM')