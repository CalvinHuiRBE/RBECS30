# RPG Simple Menu
import sys

print("Justice League: Crisis on Infinite Earths")
print("Valid actions for current location")
# valid directions and actions for the character
valid_actions = ["actions", "directions"]
# possible actions
possible_actions = ["explore", "attack", "defend", "heal", "quit"]
# possible directions
possible_directions = ["north", "south", "east", "west"]
while True:
    print("What do you want to do?")
    for action in possible_actions:
        print(f"{action}")
    # input action
    action_input = input("Action: ")
    if action_input.lower() in possible_actions:
        if action_input.lower() == "explore":
            for direction in possible_directions:
                print(f" * {direction}")
            direction_input = input("Which direction do you want to go? ")
            # checking if input is in the list possible_directions
            if direction_input.lower() in possible_directions:
                print(f"Go {direction_input}!")
            elif direction_input.lower() not in possible_directions:
                print("Invalid direction!")
        elif action_input.lower() == "quit":
            print("Goodbye!")
            sys.exit()
        # checking if the input is in the list possible_actions
        elif action_input.lower() in possible_actions:
            print(f"{action_input.title()}!")
