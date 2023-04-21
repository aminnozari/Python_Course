import random

words_bank = ['tree', 'book', 'linux', 'python', 'java', 'amin', 'rock', 'javascript', 'up']

word = random.choice(words_bank)
joon = 7
user_true_chars = []


while True:
    for i in range(len(word)):
        if word[i] in user_true_chars:
            print(word[i], end='')
        else:
            print('-', end='')

    user_char = input('\nplease enter a character: ').lower()

    if user_char in word:
        user_true_chars.append(user_char)
        print('yes')
    else:
        joon -= 1
        print('no')

    if len(user_true_chars) == len(word):
        print('You Win')
        break

    if joon == 0:
        print('Game Over')
        break