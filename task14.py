day = int(input('day:'))
month = int(input('month: '))
year = int(input('year'))

bissexto = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

match month:
    case 2:
        limit = 29 if bissexto else 28
    case 4 | 6 | 9 | 11:
        limit = 30
    case 1 | 3 | 5 | 7 | 8 | 10 | 12:
        limit = 31
    case _:
        limit = -1

print('invalid date' if 1 <= day <= limit else 'invalid date')