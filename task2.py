temp_c = float(input("Digite uma temperatura em Celsius: "))

fahrenheit = temp_c * 9/5 + 32
kelvin = temp_c + 273.15

opcao = int(input("Digite a opção desejada para conversão\n\n1: Fahrenheit    2: Kelvin\n\nDigite a opção desejada: "))

match opcao:
    case 1:
        print(f"Sua temperatura {temp_c:.2f} ºC em Fahrenheit é de {fahrenheit:.2f} ºF")
    case 2:
        print(f"Sua temperatura {temp_c:.2f} ºC em Kelvin é de {kelvin:.2f} ºK")

