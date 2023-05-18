import random

options = ('piedra', 'papel', 'tijera')


rounds = 1


def chooseOptions():
    user_option = input('piedra, papel o tijera => ')
    user_option = user_option.lower()

    if not user_option in options:
        print('esa opcion no es valida')
        return None, None

    computer_option = random.choice(options)

    print('User option =>', user_option)
    print('Computer option =>', computer_option)
    return user_option, computer_option


def checkRules(user_option, computer_option, user_wins, computer_wins):
    if user_option == computer_option:
        print('Empate!')
    elif user_option == 'piedra':
        if computer_option == 'tijera':
            print('piedra gana a tijera')
            print('user gano!')
            user_wins += 1
        else:
            print('Papel gana a piedra')
            print('computer gano!')
            computer_wins += 1
    elif user_option == 'papel':
        if computer_option == 'piedra':
            print('papel gana a piedra')
            print('user gano')
            user_wins += 1
        else:
            print('tijera gana a papel')
            print('computer gano!')
            computer_wins += 1
    elif user_option == 'tijera':
        if computer_option == 'papel':
            print('tijera gana a papel')
            print('user gano!')
            user_wins += 1
        else:
            print('piedra gana a tijera')
            print('computer gano!')
            computer_wins += 1
    return user_wins, computer_wins


def checkWinner(user_wins, computer_wins):
    winner = None

    if user_wins == 2:
        winner = 'user'
        print('Gano User!!! {} victorias lo llevan a la gloria.'.format(
            user_wins))

    if computer_wins == 2:
        winner = 'computer'
        print('Gano Computer!!! {} victorias lo llevan a la gloria.'.format(
            computer_wins))
    return winner


def runGame():

    computer_wins = 0
    user_wins = 0

    rounds = 1
    result = None

    while True:

        print('*' * 10)
        print('ROUND', rounds)
        print('*' * 10)

        print('computer_wins', computer_wins)
        print('user_wins', user_wins)

        rounds += 1

        user_option, computer_option = chooseOptions()

        user_wins, computer_wins = checkRules(
            user_option, computer_option, user_wins, computer_wins)
        result = checkWinner(user_wins, computer_wins)

        if result == 'user':
            break
        if result == 'computer':
            break


runGame()
