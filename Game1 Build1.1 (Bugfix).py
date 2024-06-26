#Samuel Theiss
#Extra Project Game
#Period 5 - 9/20/21

print("Welcome to [game1]!")
input("Press enter to start.")

#Variables:
running = "0"

key = str("no")
keyDescription = str(" There is a key hanging from a rack.")

sword = str("no")
swordDescription = str("\nYou see a sword attached to a decoration on the wall.")

kitchenStatus = str("one in the south side of the room")
hallStatus = str("one in the east\nside of the room")
diningRoomStatus = str("one in the west side of the room")

kitchenInput = str("south")
hallInput = str("east")
diningRoomInput = str("west")


#First Room, uses: all variables
def firstRoom():
    global running
    global key
    global keyDescription
    global sword
    global swordDescription
    global kitchenStatus
    global hallStatus
    global diningRoomStatus
    global kitchenInput
    global hallInput
    global diningRoomInput

    #Reset variable definitions for every replay:
    running = "0"

    key = str("no")
    keyDescription = str(" There is a key hanging from a rack.")

    sword = str("no")
    swordDescription = str("\nYou see a sword attached to a decoration on the wall.")

    kitchenStatus = str("one in the south side of the room")
    hallStatus = str("one in the east\nside of the room")
    diningRoomStatus = str("one in the west side of the room")

    kitchenInput = str("south")
    hallInput = str("east")
    diningRoomInput = str("west")
    
    #Game start:
    print("\nYou wake up on a cold, stone floor. You don't know how you got here.\nYou see a door.")

    while running == "0":
        action = input("\nOpen the door?\n(yes, no): ")
        
        if action == "no":
            print("\nYou decide to stay where you are and see what happens.")
        elif action == "yes":
            print("\nYou walk up to and walk through the door.")
            secondRoom()
            break
        else:
            print("\nInvalid input.")

#Second Room, uses: action, kitchenStatus, hallStatus, diningRoom, kitchenInput, hallInput, diningRoomInput, running
def secondRoom():
        global kitchenStatus
        global hallStatus
        global diningRoomStatus
        global kitchenInput
        global hallInput
        global diningRoomInput
        global running
        
        print("\nIn  this room, you see three doors, " + kitchenStatus + ", " + hallStatus + " and " + diningRoomStatus + ".")

        while running == "0":
            action = input("\nWhich door do you open?\n(" + kitchenInput + ", " + hallInput + ", " + diningRoomInput + "): ")
            
            
            if (action == "south") or (action == "kitchen"):
                kitchenStatus = "the door to the kitchen"
                kitchenInput = "kitchen"
                kitchen()
                break
            elif (action == "east") or (action == "hall"):
                hallStatus = "the door to the hall"
                hallInput = "hall"
                hall()
                break
            elif (action == "west") or (action == "dining room"):
                diningRoomStatus = "the door to the Dining Room"
                diningRoomInput = "dining room"
                diningRoom()
                break
            else:
                print("\nInvalid input.")

#Kitchen, uses: action, key, running
def kitchen():
    global key
    global keyDescription
    global running
    
    print("\nYou open the south door. The room looks like a kitchen." + keyDescription)
    
    while running == "0":
        if key == "no":
            action1 = input("\nTake the key?\n(yes, no): ")

            if action1 == "yes":
                print("\nYou take the key.")
                key = "yes"
                keyDescription = str("")

                while running == "0":
                    action2 = input("\nExit the room?\n(yes, no): ")
                    if action2 == "yes":
                        print("\nYou walk back through the door you came in from.")
                        secondRoom()
                        break
                    elif action2 == "no":
                        print("\nYou decide to stay in the kitchen for awhile. Nothing happens.")
                    else:
                        print("\nInvalid input")
            elif action1 == "no":
                print("\nYou decide not to take the key.")
                key = "no"
                while running == "0":
                    action2 = input("\nExit the room?\n(yes, no): ")
                    if action2 == "yes":
                        print("\nYou walk back through the door you came in from.")
                        secondRoom()
                        break
                    elif action2 == "no":
                        print("\nYou decide to stay in the kitchen for awhile. Nothing happens.")
                    else:
                        print("\nInvalid input")
            else:
                print("\nInvalid input.")
        else:

            while running == "0":
                if key == "yes":
                    action3 = input("\nPut the key back?\n(yes, no): ")
                    if action3 == "yes":
                        print("\nYou put the key back where you found it.")
                        key = "no"
                        keyDescription = " There is a key hanging from a rack."
                        break
                    elif action3 == "no":
                        print("\nYou decide to keep the key.")
                        break
                    else:
                        print("\nInvalid input.")
                else:
                    break
            
            while running == "0":
                action2 = input("\nExit the room?\n(yes, no): ")

                if action2 == "yes":
                    print("\nYou walk back through the door you came in from.")
                    secondRoom()
                    break
                elif action2 == "no":
                    print("\nYou decide to stay in the kitchen for awhile. Nothing happens.")
                else:
                    print("\nInvalid input")

#Dining Room, uses: sword, swordDescription, running
def diningRoom():
    global sword
    global swordDescription
    global running
    
    print("\nYou walk through the west door. The room has a large table set with plates.\nIt looks like a dining room." + swordDescription)

    while running == "0":
        if sword == "no":
            while running == "0":
                action1 = input("\nTake the sword?\n(yes, no): ")
                if action1 == "yes":
                    print("\nYou decide to take the sword")
                    sword = "yes"
                    swordDescription = str("")

                    while running == "0":
                        action2 = input("\nExit the room?\n(yes, no): ")
                        if action2 == "yes":
                            print("\nYou walk back through the door you came in from.")
                            secondRoom()
                            break
                        elif action2 == "no":
                            print("\nYou decide to stay in the dining room for awhile. Nothing happens.")
                        else:
                            print("\nInvalid input")
                elif action1 == "no":
                    print("\nYou decide to not take the sword")

                    while running == "0":
                        action2 = input("\nExit the room?\n(yes, no): ")
                        if action2 == "yes":
                            print("\nYou walk back through the door you came in from.")
                            secondRoom()
                            break
                        elif action2 == "no":
                            print("\nYou decide to stay in the dining room for awhile. Nothing happens.")
                        else:
                            print("\nInvalid input")
                else:
                    print("\nInvalid input.")
            break
        elif sword == "yes":
            while running == "0":
                action1 = input("\nPut the sword back?\n(yes, no): ")
                if action1 == "yes":
                    print("\nYou decide to replace the sword")
                    sword = "no"
                    swordDescription = "\nYou see a sword attached to a decoration on the wall."
                    break
                elif action1 == "no":
                    print("\nYou decide to keep the sword.")
                    break
                else:
                    print("\nInvalid input")
        
            while running == "0":
                    action2 = input("\nExit the room?\n(yes, no): ")
                    if action2 == "yes":
                        print("\nYou walk back through the door you came in from.")
                        secondRoom()
                        break
                    elif action2 == "no":
                        print("\nYou decide to stay in the dining room for awhile. Nothing happens.")
                    else:
                        print("\nInvalid input")
            

#Hall, uses: key, kitchenInput, running
def hall():
    global key
    global kitchenInput
    global running
    
    print("\nYou walk through the east door. The room looks like a large hall.\nThere is a large door, possibly a way out, but there is a troll sleeping on it.")
    
    while running == "0":
        action1 = input("Wake up the troll?\n(yes, no): ")
        if action1 == "yes":
            print("\nYou decide to wake up the troll")
            print("\nThe troll wakes up and looks at you.")

            if (key == "yes") and (sword == "yes"):
                print("\nThe troll notices your sword, goes wide-eyed, jumps up and picks up their club.")
                print("\"Go and put that sword back where you found it!\" demands the troll.")

                while running == "0":
                    action2 = input("\nLeave the room?\n(yes, no): ")

                    if action2 == "yes":
                        print("\nYou decide to leave the room.")
                        secondRoom()
                        break
                    elif action2 == "no":
                        print("\nYou decide to stay and fight the troll.")
                        print("\nYou draw your sword and start to run up to the troll to stab it, but you get tangled in the string of the key and you fall over. Before you can get up, the troll's club comes down on your head killing you instantly.")
                        print("\n---------- GAME OVER ----------")
                        while running == "0":
                            replay = input("\nPlay again?\n(yes, no): ")
                            if replay == "yes":
                                firstRoom()
                                break
                            elif replay == "no":
                                print("\nGame Ended.")
                                running = "1"
                                break
                            else:
                                print("\nInvalid input.")
                        break
                    else:
                        print("\nInvalid input.")
            elif (key == "yes") and (sword == "no"):
                print("\"Good job getting this far,\" the troll says. Give me the key and I'll open the door for you and let you out, or leave the room.")
                while running == "0":
                    
                    while running == "0":
                        action2 = input("\nGive the troll the key, refuse, or leave the room?\n(yes, no, leave): ")
                        if action2 == "yes":
                            print("\nYou hand the key over to the troll.")
                            print("As soon as the key leaves your hand the troll smiles evily and pushes you back.")
                            print("\"Fool!\" the troll admonishes \"I could never have gotten the key myself, but now that you gave it to me, I can leave this accursed place!\" the troll proclaims truimphantly.")
                            print("An evil smile creeps over the trolls face as they start pulling out their club. \"For your hard work, how about I give you a reward?\" the troll says, still pulling out their club. You don't think whatever reward the troll has in mind is going to be one you want to recieve. \"I'll give you a quick death!\" the troll says, laughing malevolently. You try to turn and run to the door, but the trolls club cracks open your skull before you can make it to the door, killing you instantly.")
                            print("\n---------- GAME OVER ----------")
                            while running == "0":
                                replay = input("\nPlay again?\n(yes, no): ")
                                if replay == "yes":
                                    firstRoom()
                                    break
                                elif replay == "no":
                                    print("\nGame Ended.")
                                    running = "1"
                                    break
                                else:
                                    print("\nInvalid input.")
                            break
                        elif action2 == "no":
                            print("\nYou tuck your key deeper into your clothes with a defiant look in your eye.")
                            print("Anger flahses over the troll's face and they pull out their club. \"If you won't give me the key I'll just have to take it from you,\" the troll states angrily.")
                            print("The troll is much quicker than you thought it would be, and before you can make it to the door you feel a strong hand grab your arm, cutting off all means of escape.")
                            print("\"No more running now, human!\" the troll cries truimphantly. \"Now to take your key,\" says the troll, more focused than earlier.")
                            print("The troll tears through your clothing and takes your key, which it holds in the air as if it were a piece of treasure.")
                            print("\"Now to figure out what to do with you,\" the troll says as their gaze shifts back to you, it's mouth in a sneer. A frown creeps onto it's face as their gaze looses focus on you. The troll shrugs it's shoulders and returns it's gaze back to you after it's contemplation. \"I can't think of anything fun to do with you, so I just kill you now,\" the troll decides as a malicious grin appears back on it's face, and before you can even protest, it slams you into the ground, snapping your neck and killing you instantly.")
                            print("\n---------- GAME OVER ----------")
                            while running == "0":
                                replay = input("\nPlay again?\n(yes, no): ")
                                if replay == "yes":
                                    firstRoom()
                                    break
                                elif replay == "no":
                                    print("\nGame Ended.")
                                    running = "1"
                                    break
                                else:
                                    print("\nInvalid input.")
                            break
                        elif action2 == "leave":
                            print("\nYou decide to leave the room.")
                            print("The troll sighs and slumps down into the corner, going to sleep again.")
                            secondRoom()
                            break
                        else:
                            print("\nInvalid input.")
                    break
            elif (key == "no") and (sword == "yes"):
                print("\nThe troll notices your sword, goes wide-eyed, jumps up and picks up their club.")
                print("\"Go and put that sword back where you found it!\" demands the troll.")
                
                while running == "0":
                    action2 = input("\nLeave the room?\n(yes, no): ")
                    if action2 == "yes":
                        print("\nYou decide to leave the room.")
                        secondRoom()
                        break
                    elif action2 == "no":
                        print("\nYou decide to stay and fight the troll.")
                        print("You draw your sword and start runnig towards the troll. Taken aback by your bravery, the troll stumbles and delays their swing allowing you to get close.")
                        print("You slash across the troll's stomach, elicting a scream of pain from the troll and a splash of blood, but it quickly regains it composure, before you can get in another slash, so you retreat out of the troll's range.")
                        print("As you retreat you notice that the troll's wound seems to heal itself, and before you go in for another strike, the slash is already healed.")
                        print("You relize that if you want to defeat the troll, you'll need to cut off it's head so that you can kill it before it regenerates. That's going to be a problem, however, since the troll is a good yard taller than you, alought you think you can reach if you try.")
                        print("You steel yourself and start running in again. This time the troll is ready for you, and it's club swings in at you. You just barely manage to dodge it however and you jump on to the troll's head to cut it off with your sword.")
                        print("The troll's eyes widen with fear as it realizes that it's attacked missed, and cries, \"Nooo! It can't end like this!\" To the troll's detriment, however, it already has.")
                        print("Your sword ealisly slices through the troll's neck and it's body falls to the ground limp. It's head rolls onto the ground, still stuck in the troll's expression of fear. A messy bussiness, but necessary.")
                        print("Looking at the door the troll was sleeping on again, you notice that there is a keyhole where the troll was sleeping.")
                        if kitchenInput == "kitchen":
                            print("You remember the key you say in the kitchen and decide to go and retrive that.")
                            print("After retriving the key, you make it back to the hall and turn the key in the lock of the door.")
                            print("The keylock turns easily and soon you hear a click and the key won't turn anymore; the door is open")
                            print("You walk through the door and your finally free.")
                            print("\n---------- VICTORY ----------")
                            while running == "0":
                                replay = input("\nPlay again?\n(yes, no): ")
                                if replay == "yes":
                                    firstRoom()
                                    break
                                elif replay == "no":
                                    print("\nGame Ended.")
                                    running = "1"
                                    break
                                else:
                                    print("\nInvalid input.")
                            break
                        else:
                            print("Realizing you need a key to open the door, you exit the hall and search the other doors.")
                            print("In the south door, you find a room that looks like a kitchen.")
                            print("After a quick glance you notice a key hanging from a rack in the room.")
                            print("After retriving the key, you make it back to the hall and turn the key in the lock of the door.")
                            print("The keylock turns easily and soon you hear a click and the key won't turn anymore; the door is open")
                            print("You walk through the door and your finally free.")
                            print("\n---------- VICTORY ----------")
                            while running == "0":
                                replay = input("\nPlay again?\n(yes, no): ")
                                if replay == "yes":
                                    firstRoom()
                                    break
                                elif replay == "no":
                                    print("\nGame Ended.")
                                    running = "1"
                                    break
                                else:
                                    print("\nInvalid input.")
                            break
            elif (key == "no") and (sword == "no"):
                print("The troll sees that you don't have anything other than your clothes on you and a look of dissapointment appears on its face for a moment before vanishing again")
                print("\"Come back when you've brought the key with you the troll says, an evil grin crossing its face for a second as he finishes the scentence.")
                print("Without any way to oppose the troll, you decide to leave the room.")
                secondRoom()
                break
        elif action1 == "no":
            print("\nYou decide not to wake up the troll.")
            while running == "0":
                action2 = input("\nLeave the room?\n(yes, no): ")
                if action2 == "yes":
                    print("\nYou exit the room.")
                    secondRoom()
                    break
                elif action2 == "no":
                    print("\nYou decide to stay in the room. Nothing Happens.")
                else:
                    print("\nInvalid input.")
        break

firstRoom()
