print ("Welcome to the haunted haven!")
print ("Your mission: Escape the haunted house... or else!")

choice1= input("You enter the house. Straight ahead is the kitchen, to the to right is the living room. "
               "Where do you want to go? Type 'living room' or 'kitchen'.\n").lower()

if choice1 == "kitchen":
    choice2 = input("All four Teletubbies are standing there, staring at you. They start to chase you."
            "You can either run out the back door or down the stairs to the basement. Type 'backdoor' or 'basement'. \n").lower()
    if choice2 == "basement":
        choice3 = input("You've come across 3 doors. Bronze, Brass, and Black. Choose a door. Type 'bronze' or 'brass', or 'black'.\n").lower()
        if choice3 == "brass":
            print("A ghost rose from the ashes and took your soul. Game over.")
        elif choice3 =="bronze":
            print("The Teletubbies caught you and beat you up. Game over.")
        elif choice3 == "black":
            print("You escaped the Haunted House. You win!")
        else:
            print("The door you chose wasn't an option. You lose.")
    else:
        print("You got attacked by wild hogs. Game over.")

else:
    print("The boogeyman caught you. Game over!")



