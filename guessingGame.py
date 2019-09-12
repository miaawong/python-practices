import random

guessesTaken = 0

num = random.randint(1, 99)

for guessesTaken in range(3):
    print 'Guess a number between 1 and 100'
    guessesTaken + 1
    guess = int(input())
    if guess == num:
        print "YOU GUESS CORRECTLY!!!"
        break
    elif guess < num:
        print 'too low'
    elif guess > num:
        print "too high!"

if guess != num:
    print "nope! the number i was thinking of was", num
