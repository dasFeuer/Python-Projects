name = input("Type your name: ")
print(f"Welocme {name} to this adventure!")

answer = input(
    "You are on a dirt road, it has come to an end and you go left or right. Which way would you like to go?: ").lower()
if answer == "left":
    answer = input("You come to a river, you can walk around it or swin across? Type walk to walk arould and swim to swim across: ").lower()
    if answer == "swim":
        print("You swam across and were eaten by an alligator.")
    elif answer == "walk":
        print("You walked for many miles, ran out of water and you lost the game.")
    else:
        print("Not a valid option. You lose.")
elif answer == "right":
    answer = input("You come to a bridge, it looks wobbly, do you want cross it or head back (cross/back): ").lower()
    if answer == "back":
        print("You go back and lose.")
    elif answer == "cross":
        answer = input("You crossed the bridge and meet a stranger. Do you talk to them? (Yes/No): ").lower()

        if answer == "yes":
            print("You talked to stranger and they gave you gold. YOU WIN!")
        elif answer == "no":
            print("You ignored the stranger and they are offended and you lose.")
        else:
            print("Not a valid option. You lose.")

    else:
        print("Not a valid option. You lose.")
else:
    print("Not a valid option. You lose.")

print(f"Thank you for trying {name}. See you soon!")
