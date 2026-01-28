import random

def hangman():
    print("Привет! Добро пожаловать в игру Виселица")

worldlist = ['мандарин', 'апельсин', 'яблоко', 'груша', 'виноград', 'манго']
secret = random.choice(worldlist)
guesses = "ауоыиэюяёе"
turns = 5

while turns > 0:
    missed = 0
    for letter in secret:
        if letter in guesses:
            print(letter, end = ' ')    
        else:
            print('_', end = ' ')
            missed += 1
    
    if missed == 0:
        print('\nТы выиграл!')
        break

    guess = input('\nНазови букву: ')
    guesses += guess

    if guess not in secret:
        turns -= 1
        print('\Не угадал.')
        print ('\n', 'Осталось попыток: ', turns)
        if turns < 5: print ('\n  | ')
        if turns < 4: print ('  O  ')
        if turns < 3: print (' /|\ ')
        if turns < 2: print ('  |  ')
        if turns < 1: print (' / \ ')
        if turns == 0: print ('')

