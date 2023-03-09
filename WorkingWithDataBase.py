# Instructions:
# Step 1: loop through the database and print the Superhero Names, ex. Spider-man.
#
# Step 2: loop through the database and print the hero's names, ex. Peter Parker.
#
# Step 3: Combine the above loops to create a table of the Superhero's titles and names.
#              Note you can copy the following format() code to create the table:
#               print("{:<12} {:<12}".format("Hero Title:", "Name:"))
#
#               print("{:<12} {:<12}".format(__________, ___________)) #blanks vary because they are based on your code.

# Database Example Code - created from the Dictionaries you submitted yesterday
Marvel_Superheros = {
  "Spiderman": {
           "Name": "Peter Parker",
           "Weapons": ["Webbing"],
           "Super Powers": ["Speed", "Reflexes", "Spider-Sense"],
           "Weaknesses": ["Ethyl Chloride Pesticide"]},
  "Thing": {
           "Name": "Ben Grimm",
           "Weapons": ["Fists"],
           "Powers": ["Immortal", "Super Strength",
                      "Enhanced Lung Capacity", "Good Fighter"], "Weakness": [None]},
  "Baby_Groot": {
           "Name": "Baby Groot",
           "Weapons": ["Strong Branches"],
           "Super Powers": ["Self-Healing", "Controls Plant",
                            "Immune to Fire"],
           "Weaknesses": ["Termites"]},
  "Ironman": {
           "Name": "Tony Stark",
           "Weapons": ["Ironman Suit", "AI", "Blasters"],
           "Superpowers": ["Smart", "Rich"],
           "Weaknesses": ["Arrogant"]},
  "Deadpool": {
           "Name": "Wade Wilson",
           "Weapons": ["Katanas", "Grenades", "Guns"],
           "Super Powers": ["Speed", "Bullet Proof", "Self-Healing"],
           "Weaknesses": ["Women", "Ugly"]},
  "Ant-man": {
           "Name": "Scott Lang",
           "Weapons": ["Ant-man Suit"],
           "Super Powers": ["Communication with Insects", "Sound Amplification"],
           "Weaknesses": ["Lacks Ability Control"]}
}

# Step 1
print("This prints superhero titles.")
for Hero_Names in Marvel_Superheros:
    print(Hero_Names)

# Step 2
print("This prints the persons name")
for Hero_Names in Marvel_Superheros:
    for key in Marvel_Superheros[Hero_Names]:
        if key == "Name":
            print(Marvel_Superheros[Hero_Names][key])

# Step 3
print("{:<15} {:<15}".format("Hero Title:", "Name:"))
for Hero_Names in Marvel_Superheros:
    for key in Marvel_Superheros[Hero_Names]:
        if key == "Name":
            print("{:<15} {:<15}".format(Hero_Names, Marvel_Superheros[Hero_Names[key]]))
