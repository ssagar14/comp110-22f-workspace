"""An example of conditional if-else statements"""

SECRET: int = 3

print("I'm thinking of a number between 1-5, what is it?")
guess: int = int(input("What is your guess? "))

if guess == SECRET: 
    print("You guessed correctly!!")
    print("Awesome")
else:
    print("Sorry, you guessed incorrectly :(")
    print("Oops, sorry")

print("Game over.")