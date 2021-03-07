import random

guessed_number = random.randint(0, 100)
user_number = int(input('Введите ваше число: '))
if user_number < guessed_number:
    print('Ваше число меньше загаданного')
elif user_number > guessed_number:
    print('Ваше число больше загаданного')
else:
    print('Вы угадали число')
