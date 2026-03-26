print("Validador e Classificador de Triângulos")

l1 = float(input("Digite o valor do primeiro lado: "))
l2 = float(input("Digite o valor do segundo lado: "))
l3 = float(input("Digite o valor do terceiro lado: "))

if (l1 < l2 + l3) and (l2 < l1 + l3) and (l3 < l1 + l2):
    print("Os lados formam um triângulo.")
    if l1 == l2 == l3:
        print("O triângulo é equilátero.")
    elif l1 == l2 or l1 == l3 or l2 == l3:
        print("O triângulo é isósceles.")
    else:
        print("O triângulo é escaleno.")