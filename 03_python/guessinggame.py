import random

number = random.randint(1,1000) # secret Number between 1 and 1000

n_guess = 1
guess = int(input("Guess the number between 1 and 1000: "))

while guess != number:
    # add more code here..
    if guess < number:
        print("Your guess",guess,"too low")
    elif guess > number:
        print("Your guess",guess,"too high")
    n_guess = n_guess + 1
    guess = int(input("Guess again: "))
print("Congratulations, you guessed the number", number, "in", n_guess, "guesses")


    
