print("Welcome to the quiz game!")
play = input("Do you want to play?(y/n): ")

if play.lower() != "y":
    quit()

print("Okay! Let's play :)")
score = 0

answer = input("What is CPU stands for? ")
if answer.lower() == "central processing unit":
    print ("Awesome! Your answer is correct!")
    score += 1
else:
    print ("Sorry, but your answer is wrong :(")
    ctn = input("Do you want to continue the game (y/n): ")
    if ctn.lower() != "y":
        print("Thank you for playing the game!")
        quit()
    else:
        print("Awesome! Then let's continue.")

answer = input("What is GPU stands for? ")
if answer.lower() == "graphics processing unit":
    print ("Awesome! Your answer is correct!")
    score += 1
else:
    print ("Sorry, but your answer is wrong :(")
    ctn = input("Do you want to continue the game (y/n): ")
    if ctn.lower() != "y":
        print("Thank you for playing the game!")
        quit()
    else:
        print("Awesome! Then let's continue.")

answer = input("What is RAM stands for? ")
if answer.lower() == "random access memory":
    print ("Awesome! Your answer is correct!")
    score += 1
else:
    print ("Sorry, but your answer is wrong :(")
    ctn = input("Do you want to continue the game (y/n): ")
    if ctn.lower() != "y":
        print("Thank you for playing the game!")
        quit()
    else:
        print("Awesome! Then let's continue.")

answer = input("What is PSU stands for? ")
if answer.lower() == "power supply":
    print ("Awesome! Your answer is correct!")
    score += 1
else:
    print ("Sorry, but your answer is wrong :(")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 4) * 100) + " %." )

# try:
#     while True:
#         rate = int(input("How much do you rate this game from 0 to 10: "))
#         if rate <= -1 or rate >= 11:
#              input = int(input("Please enter valid rating from 1 to 10: "))
#         elif rate >= 8 and rate <= 10:
#             print ("Thank you so much. I am really happy that liked my game!")
#             break
#         elif rate >= 0 and rate <= 7:
#             print ("Thank you for your rating. I will try make this game more better.")
#             break
#         else:
#             print("See you soon!")
#         # else:
#         #     if rate <= -1 and rate >= 11:
#         #      input = int(input("Please enter valid rating from 1 to 10: "))
# except:
#     print("Due to invaild input this game is over! Thank you for playing. See you soon!")
while True:
    rate = input("How much do you rate this game from 0 to 10: ")
    if rate.isdigit():
        rate = int(rate)
        if rate >= 0 and rate <= 10:
            if rate >= 8:
                print("Thank you so much. I am really happy that you liked my game!")
            else:
                print("Thank you for your rating. I will try to make this game even better.")
            break
        else:
            print("Please enter a valid rating from 0 to 10.")
    else:
        print("Please enter a valid number.")

print("See you soon!")
