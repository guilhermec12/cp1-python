idade = int(input('digite sua idade: '))
id_cont = int(input('digite o tempo de contribuição: '))

if idade >= 65 or id_cont >= 30:
    print('voce pode se aposentar.')
elif idade >= 60 and id_cont >= 25:
    print('voce pode se aposentar mas com certas regras')
else:
    print('voce ainda nao pode se aposentar')
