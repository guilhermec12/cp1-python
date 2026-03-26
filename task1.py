peso = float(input('digite seu peso: '))
altura = float(input('digite sua altura: '))

imc = peso / (altura**2)

if imc <= 18.5:
    print('Abaixo do peso')
elif 18.5 < imc <= 24.9:
    print('Peso normal')
elif 25 <= imc <= 29.9:
    print('Sobrepeso')
elif 30 <= imc <= 34.9:
    print('Obesidade 1 grau')
elif 35 <= imc <= 39.9:
    print('Obesidade 2 grau')
else:
    print('Obesidade morbida')