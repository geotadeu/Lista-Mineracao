valor1 = int(input('Digite o valor interiro a ser retirado em reais: '))

# Notas disponíveis: 100,00 reais; 50,00 reais; 10,00 reais; 1,00 real.

Nota100 = int(valor1 // 100)
Nota50 = int((valor1 - (Nota100 * 100)) // 50)
Nota10 = int((valor1 - (Nota100 * 100) - (Nota50 * 50)) // 10)
Nota1 = int((valor1 - (Nota100 * 100) - (Nota50 * 50) - (Nota10 * 10)) // 1)

print('O número mínimo de notas a ser retiradas é:')
print(' {} notas de R$100,00'.format(Nota100))
print(' {} notas de R$50,00'.format(Nota50))
print(' {} notas de R$10,00'.format(Nota10))
print(' {} notas de R$1,00'.format(Nota1))