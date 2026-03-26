tipe = int(input('put veicle tipe (1-4): '))

match tipe:
    case 1: #tipe1
        print("Valor: R$ 5.00")
    case 2: #tipe2
        print("Valor: R$ 10.00")
    case 3: #tipe3
        print('value: $ 15.00')
    case 4: #tipe4
        print('value: $ 25.00')
    case _:
        print('invalid tipe')