import random
secretNumber = random.randint(1, 20)
taken = []
tries = taken
for guessesTaken in range(1, 30):
    print('Guess a number: ')
    guess = int(input())
    taken.append(guess)
    if guess < secretNumber:
        print('Your guess is too low.')

    elif guess > secretNumber:
        print('Your guess is too high.')
    else:
        break

if guess == secretNumber:
    for i in taken:
        if guess in tries:
            tries.pop()
    print(
        'Good job! You guessed my number in ' + str(len(tries)) + ' guesses!'
        )
else:
    print('The correct number was' + str(secretNumber))
