import random

guessed_number = random.randint(0, 100)

attempts = 0

max_attempts = 10

while attempts < max_attempts:
    user_number = int(input('Введите ваше число: '))
    if guessed_number == user_number:
        print('Вы угадали число')
        break
    attempts += 1
    if user_number < guessed_number:
        print('Ваше число меньше загаданного')
    else:
        print('Ваше число больше загаданного')

else:
    print('Вы не угадали')



