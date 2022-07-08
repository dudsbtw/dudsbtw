import random
random_number = random.randint(1,10)
guess = int(input('Guess a number from 1 to 10 '))
if guess > random_number:
    print('Your guess was higher than the random number.')
elif guess < random_number:
    print('Your guess was lower than the random number.')
elif guess == random_number:
    print('You are right!')
