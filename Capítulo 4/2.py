import math
import numpy
n1 = int(input('Digite um valor em graus para um ângulo: '))
n_convert = numpy.deg2rad(n1)
print('O valor do cosseno é: ', math.cos(n_convert))
print('O valor do seno é: ', math.sin(n_convert))
print('O valor da tangente é: ', math.tan(n_convert))
