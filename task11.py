player = input('select stone, paper or scissor: ').lower()
computer = 'stone'

if player == computer:
    print('tie')
else:
    if player == 'stone':
        if computer == 'scissor':
            print('you win')
        else:
            print('you lose')

    elif player == 'paper':
        if computer == 'stone':
            print('you win')
        else:
            print('you lose')

    elif player == 'scissor':
        if computer == 'paper':
            print('you win')
        else:
            print('you lose')

    else:
        print('invalid option')