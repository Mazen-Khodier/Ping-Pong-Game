import os
print("This is a basic launcher!")
while True:
    print("\n\nPlease Choose a Game Mode from the Following: ")
    print("practice, multiplayer, vs computer, computer\n")
    x = input()
    if x == "practice":
        os.system('python Practice_Mode.py')
    elif x == "multiplayer":
        os.system('Multiplayer_Mode.py')
    elif x == "vs computer":
        os.system('VS_Computer_Mode.py')
    elif x == "computer":
        os.system('Watch_Computer_Mode.py')