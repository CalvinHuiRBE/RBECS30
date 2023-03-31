########################################################
# Title: CS 30 RPG Map
# coder: Calvin Hui
# version: 002
########################################################
""" This is an RPG Map """

# map layout
Map = [
    ['shed', 'backyard', 'flowerbed'],
    ['kitchen', 'dining-room', 'living-room'],
    ['washroom', 'front-foyer', 'garage']
]
# start location
row = 2
col = 1
MaxCol = 2
MaxRow = 2

playing = True


def movement():
    """Group that is responsible for all the movement and where the player can or can not go."""
    global row, col, MaxRow, MaxCol, playing
    # list the available directions that the player can go within the parameter of the map
    while True:
        print(f"Where would you like to go?")
        if row != 0:
            print(f" * North")
        if row != MaxRow:
            print(f" * South")
        if col != MaxCol:
            print(f" * East")
        if col != 0:
            print(f" * West")

        # player can input their desired direction with in the list above
        movement_choice = input(f"Choice: ")

        # moves the player within the map by + or - 1 unit
        if movement_choice.lower() == "north" and row > 0:
            row -= 1
            break
        elif movement_choice.lower() == "south" and row < MaxRow:
            row += 1
            break
        elif movement_choice.lower() == "east" and col < MaxCol:
            col += 1
            break
        elif movement_choice.lower() == "west" and col > 0:
            col -= 1
            break
        # type quit to exit the game
        elif movement_choice.lower() == "quit":
            playing = False
            break
        # for invalid direction/input
        else:
            print(f"Sorry cant go that way!")


# prints message
# with the corresponding location on the map
while playing:
    location_description = Map[row][col]
    if location_description == 'front-foyer':
        print(f"Welcome to the Abandoned House.")
        print(f"If you would like to leave type: Quit.")
        movement()
    if location_description == 'living-room':
        print(f"The Living room")
        print(f"Doesnt seem like anyone is living here.")
        movement()
    if location_description == 'garage':
        print(f"The Garage")
        print(f"Just a garage, doesn't seem like there is anything interesting.")
        movement()
    if location_description == 'flowerbed':
        print(f"The Flowerbed")
        print(f"Beautiful flowers but there is something shiny in stuck in the flowerbed.")
        movement()
    if location_description == 'shed':
        print(f"The Shed")
        print(f"There's a shed in the backyard, but seems like its locked.")
        movement()
    if location_description == 'dining-room':
        print(f"The Dining Room")
        print(f"It smells.")
        movement()
print(f"Goodbye :( .")
