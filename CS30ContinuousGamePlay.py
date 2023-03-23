###############################################################################
# Title: CS 30 Continuous Gameplay Menu
# coder: Calvin Hui
# version: 002
###############################################################################
""" This is an RPG menu that has different action prompts """
import sys
# possible actions
possible_actions = ["explore", "attack", "defend", "heal", "quit"]
# possible directions
possible_directions = ["north", "south", "east", "west", "back"]
while True:
    # Flag for validation
    flag = 1
    # print title
    print()
    print(" *** RPG Menu *** ")
    print()

    # print list of possible actions to select from
    print("What do you want to do?")
    for action in possible_actions:
        print(f"{action}")

    action_input = input("Action: ")

    # prints action message for options without sub menu
    if action_input.lower() in possible_actions:
        print(f"{action_input.title()}!")

    # quit function to end the loop
    if action_input.lower() == "quit":
        print("Goodbye!")
        sys.exit()

    # print message for invalid action input
    if action_input.lower() not in possible_actions:
        print("Invalid Action!")

    # opens sub menu of possible of directions
    while True:
        if action_input.lower() in possible_actions:
            if action_input.lower() == "explore":
                for direction in possible_directions:
                    print(f" * {direction}")

                direction_input = input("Which direction do you want to go? ")

                if direction_input.lower() != "back":

                    # if the input is valid prints out a message
                    if direction_input.lower() in possible_directions:
                        print(f"Going {direction_input}!")
                        break
                    # if the input is not valid, prints out a message
                    else:
                        flag = 0
                        print("Invalid Direction!")

                # goes back to main menu
                if direction_input.lower() == "back":
                    print("Back to main menu.")
                    break
            if flag == 1:
                print()
                break
