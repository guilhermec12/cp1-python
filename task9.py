n1 = float(input('put first number: '))
n2 = float(input('put second number'))

print('select option:\n')
print('1. add')
print('2. subtract')
print('3. multiplication')
print('4. division')

operation = input('digite your operation number:')

if operation == '1':
    result = n1 + n2
    print('result:', result)

elif operation == '2':
    result = n1 - n2
    print('result:', result)

elif operation == '3':
    result = n1 * n2
    print('result:', result)

elif operation == '4':
    if n2 == 0:
        print('invalid operation')
    else:
        result = n1 / n2
        print('result:', result)

else:
    print('invalid option')