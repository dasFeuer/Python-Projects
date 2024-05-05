import random

COLORS =["R", "G", "B", "Y", "W", "O"]
TRIES = 10
CODE_LENGTH = 4

def generateCode():
    code = []

    for _ in range(CODE_LENGTH):
        color = random.choice(COLORS)
        code.append(color)

        return code
    
def guessCode():
    while True:
        guess = input("Guess: ").upper().split(" ")

        if len(guess) != CODE_LENGTH:
            print(f"You must guess {CODE_LENGTH} colors.")
            continue

        for color in guess:
            if color not in COLORS:
                print(f"Invaild color: {color}. Try again.")
                break
            else:
                break

        return guess
    
def checkCode(guess, realCode):
    colorCounts = {}
    correctPos = 0
    incorrectPos = 0

    for color in realCode:
        if color not in colorCounts:
            colorCounts[color] = 0
            colorCounts[color] += 1

    for guessColor, realColor in  zip(guess, realCode):
        if guessColor == realColor:        
            correctPos += 1    
            colorCounts[guessColor] -= 1


    for guessColor, realColor in  zip(guess, realCode):
        if guessColor in colorCounts and colorCounts[guessColor] > 0:
            incorrectPos += 1
            colorCounts[guessColor] -= 1

    return correctPos, incorrectPos

def game():
    print(f"Welcome to mistermind, you have {TRIES} to guess the code...")
    print("The valid colors are", *COLORS)

    code = generateCode()
    for attempts in range(1, TRIES + 1):
        guess = guessCode()
        correctPos, incorrectPos = checkCode(guess, code)

        if correctPos == CODE_LENGTH:
            print(f"You guessed the code in {attempts} tries.")
            break

        print(f"Correct Positions: {correctPos} | Incorrect Positions: {incorrectPos}.")

    else:
        print("You ran out of tries, the code was:", *code)


if __name__ == "__main__":
    game()