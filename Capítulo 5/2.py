t = int(input('Informe uma quantidade de segundos: '))

# Calcule a quantas horas:minutos:segundos
hr = int(t // 3600)
min = int((t - (hr * 3600)) // 60)
seg = int(t - (hr * 3600) - (min * 60))

print('A quantidade de segundos informados correspondem a: {}h:{}m:{}s' .format(hr, min, seg))