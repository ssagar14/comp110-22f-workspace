"""EX02 - One Shot Wordle."""

__author__ = "730469142"

word: str = "python"
guess: str = input(f"What is your {len(word)}-letter guess? ")
white_box: str = "\U00002B1C"
green_box: str = "\U0001F7E9"
yellow_box: str = "\U0001F7E8"
i: int = 0
emoji: str = ""

while len(guess) != len(word):
    """Making sure guess is correct number of letters"""
    guess = input(f"That was not {len(word)} letters! Try again: ")

while i < len(word):
    if guess[i] == word[i]:
        """Adding green box if correct letter in correct place"""
        emoji = emoji + green_box
    else:
        exist: bool = False
        alt_i: int = 0
        while not exist and alt_i < len(word):
            """Adding yellow or white box"""
            if word[alt_i] == guess[i]:
                exist = True
            else:
                alt_i = alt_i + 1
        if exist == True:
            emoji = emoji + yellow_box
        else: 
            emoji = emoji + white_box
    i = i + 1
print(emoji)

if guess == word:
    print("Woo! You got it!")
else:
    print("Not quite. Play again soon!")