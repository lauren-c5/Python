import asyncio


# 1. We wrap the game in an async function so it doesn't freeze the browser
async def main():
    print("Welcome to the haunted haven!")
    print("Your mission: Escape the haunted house... or else!")

    # 2. Add 'await' before every input() so the browser can pause and accept text
    choice1 = await input(
        "You enter the house. Straight ahead is the kitchen, to the right is the living room. Where do you want to go? Type 'living room' or 'kitchen'.\n")
    choice1 = choice1.lower()

    if choice1 == "kitchen":
        choice2 = await input(
            "All four Teletubbies are standing there, staring at you. They start to chase you. You can either run out the back door or down the stairs to the basement. Type 'backdoor' or 'basement'. \n")
        choice2 = choice2.lower()

        if choice2 == "basement":
            choice3 = await input(
                "You've come across 3 doors. Bronze, Brass, and Black. Choose a door. Type 'bronze' or 'brass', or 'black'.\n")
            choice3 = choice3.lower()

            if choice3 == "brass":
                print("A ghost has risen from the ashes and took your soul. Game over.")
            elif choice3 == "bronze":
                print("The Teletubbies caught you and beat you up. Game over.")
            elif choice3 == "black":
                print("You escaped the Haunted House. You win!")
            else:
                print("The door you chose wasn't an option. You lose.")
        else:
            print("You got attacked by wild hogs. Game over.")
    else:
        print("The boogeyman caught you. Game over!")


# 3. This starts the async game loop at execution
asyncio.run(main())
