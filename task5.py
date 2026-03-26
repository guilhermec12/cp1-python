requestyear = int(input("select one year and put here: "))

calc1 = requestyear %4 == 0
calc2 = requestyear % 100 == 0
calc3 = requestyear % 400 == 0

if (calc1 and not calc2) or (calc3):
    print('Your year is bissexto')
else:
    print('Your year is not bissexto')
