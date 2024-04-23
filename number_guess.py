import random

top_of_range = input("Type a number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print('Print number larger than 0 next time.')
        quit()

else:
    print('Please type a number next time.')
    quit()

random_number = random.randint(0, top_of_range)  # randrange
guesses = 0

while True:
    guesses += 1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)

    else:
        print('Please type a number next time.')
        continue

    if user_guess == random_number:
        print("You got it!")
        break
    elif user_guess > random_number:
        print("You guessed high than the number!")
    else:
        print("You guessed low than the number!")


print(f"You got it in {guesses} guesses")








# import random

# num = random.randint (1, 100)
# guess = 0
# while guess != num:
#     guess = int(input("Guess the number betweem 1 to 100: "))
#     if (guess == num):
#         print ("Congratulation! you have guess the right number")
#         print ("You haved guessed", guess,"and the answer was also", num )
#         break
#     elif ( guess > num):
#         print ("Try again, think of lower number")
        
#     elif (guess < num):
#         print("Try again, think of higher number")
    



   
        

     