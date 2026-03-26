print('income tax calculator')

salary = float(input("put your wage: "))

if salary <= 2.112:
    impost = 0
elif salary <= 2.826:
    impost = salary * 0.075 - 1713.58
else:
    print("salary above the limit for tax calculator")
