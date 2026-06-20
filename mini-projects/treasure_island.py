# This lesson just reinforced my understanding of how branching works in Python
print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
direction = input("You are at a cross road. Do you pick \"left\" or \"right\"?")
if direction == "left":
    print("You are teleported back home. You will never get the treasure. GAME OVER.")
else:
    sink_or_wait = input("You see a big pond. Will you \"swim\" to the other shore or will you \"wait\"?")
    if sink_or_wait == "swim":
        print("The shore is further than you thought. You see a buoy and sit on it. Hopefully, help arrives...")
        print("It doesn't. GAME OVER.")
    else:
        print("A boat floats over and it has oars. You decide to row the boat to your destination.")
        door_color = input("Once on shore, you see a castle with two colored doors. One pink and one purple. "
                           "What do you choose? ")
        if door_color == "pink":
            print("You are now trapped in the mansion as a ghost. GAME OVER.")
        else:
            print("You found the treasure. Time to go home. CONGRATS!")
