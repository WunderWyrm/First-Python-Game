

print("Welcome to [game1]!")
input("Press enter to start.")

#Variables:
action = " "
key = "no"

kitchen = "one in the south side of the room"
hall = "one in the east\nside of the room"
diningRoom = "one in the west side of the room"

kitchenInput = "south"
hallInput = "east"
diningRoomInput = "west"


#First Room, uses: action
def firstRoom():
    global action

    print("\nYou wake up on a cold, stone floor. You don't know how you got here.\nYou see a door.")

    while "0" == "0":
        action += input("\nOpen the door?\n(yes, no): ")

        if action == "no":
            print("\nYou decide to stay where you are and see what happens.")
        elif action == "yes":
            print("\nYou walk up to and open the door.")
            secondRoom()
            break
        else:
            print("\nInvalid input.")
#Second Room, uses: action, kitchen, hall, diningRoom, kitchenInput, hallInput, diningRoomInput
def secondRoom():
        global action
        global kitchen
        global hall
        global diningRoom
        global kitchenInput
        global hallInput
        global diningRoomInput
        
        print("\nYou see three doors, " + kitchen + ", " + hall + " and " + diningRoom + ".")

        while "0" == "0":
            action += input("\nWhich door do you open?\n(" + kitchenInput + ", " + hallInput + ", " + diningRoomInput + "): ")

            if action == "south" or "kitchen":
                kitchen += "the door to the kitchen"
                kitchenInput += "kitchen"
                kitchen()
                break
            elif action == "east" or "hall":
                hall += "the door to the hall"
                hallInput += "hall"
                hall()
                break
            elif action == "west" or "dining room":
                diningRoom += "the door to the diningRoom"
                diningRoomInput += "dining room"
                diningRoom()
                break
            else:
                print("Invalid input.")
#Kitchen, uses: action, key
def kitchen():
    global action
    global key
    
    print("\nYou open the south door. The room looks like a kitchen. There is a key hanging from a rack.")

    while "0" == "0":
        action += input("\nTake the key?\n(yes, no): ")

        if action == "yes":
            print("\nYou take the key.")
            key = "yes"
            break
        elif action == "no":
            print("\nYou decide not to take the key.")
            key = "no"
            break
        else:
            print("\nInvalid input.")

    while "0" == "0":
        action += input("\nExit the room?\n(yes, no)")

        if action == "yes":
            print("\nYou walk back through the door you came in from.")
            secondRoom()
            break
        elif action == "no":
            print("\nYou decide to stay in the kitchen for awhile. Nothing happens.")
        else:
            print("\nInvalid input")


firstRoom()
