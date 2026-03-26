note1 = float(input('put your first note: '))
note2 = float(input('put your note: '))
absence = float(input('put absence porcentage (%): '))


if absence > 25:
    print('reproved due to absence')
else:
    media = (note1 + note2) / 2
    print('media:', media)

    if media >= 7.0:
        print('approved')
    elif media >= 5.0:
        print('recuperation')
    else:
        print('reproved')