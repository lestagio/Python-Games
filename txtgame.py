import game_text
import json
import time
import sys

name = ""
inventory = ['knife']
traps_checked = False
room_txt = ""
variables = {
    'next_room': 'cave',
    'shipwreck_visited': False
}
desc_printed = False
printed_rooms = {
    'cave': False,
    'east_cave': False,
    'cave_entrance': False,
    'shipwreck': False,
    'ocean_path': False,
    'shack': False,
    'shack_reentered': False,
    'lighthouse': False,
    'endgame': False

}
shack_scene = False
door_broken = False
james = None


def save():
    save_data = {
        'inventory': inventory,
        'traps_checked': traps_checked,
        'variables': variables,
        'name': name
    }

    with open('game_save.json', 'w') as f:
        json.dump(save_data, f)
        print("Game saved successfully.")
def load():
    global inventory, traps_checked, variables, printed_rooms

    try:
        with open('game_save.json', 'r') as f:
            save_data = json.load(f)
            inventory = save_data['inventory']
            traps_checked = save_data['traps_checked']
            if 'variables' in save_data:
                variables.update(save_data['variables'])
        print("Game loaded successfully.\n")
        next_room = variables['next_room']

        if next_room == "cave":
            cave("look")
        elif next_room == "cave_entrance":
            cave_entrance("look")
        elif next_room == "east_cave":
            east_cave("look")
        elif next_room == "shipwreck":
            shipwreck("look")
        elif next_room == "ocean_path":
            ocean_path("look")
        return

    except FileNotFoundError:
        print("No saved game found.")
def print_inv():
    if inventory:
        print(", ".join(inventory))

def help_txt():

    print(game_text.txt["helptxt"])

def item_desc(item):
    global inventory
    if item == 'knife' and 'knife' in inventory:
        print(game_text.txt["knife"])
    elif item == 'broadsword' and 'broadsword' in inventory:
        print(game_text.txt["sword"])
    elif item == 'matches' and 'matches' in inventory:
        print(game_text.txt["matches"])
    elif (item == 'kerosene lamp' or item == 'lamp') and 'kerosene lamp' in inventory:
        print(game_text.txt["kerosene lamp"])
    elif item == 'golden key' or item == 'gold key' or item == 'key' and 'golden key' in inventory:
        print(game_text.txt["golden_key"])
def set_variable(var_name, value):
    global variables
    variables[var_name] = value

def cave(user_input):
    set_variable("next_room", "cave")

    next_room = 'cave'


    if user_input == 'look' or user_input == 'look around':
        print("To the north of the cave, there is light. Looking east, the cave descends into darkness. \n"
              "You hear a brief scream, and then an explosion to the east. Be careful if you go there! \n")
    elif user_input == 'east' and 'broadsword' in inventory:
        print(game_text.txt['east_with_sword'])
    elif user_input == 'east':
        next_room = 'east_cave'
    elif user_input == 'north':
        next_room = 'cave_entrance'
    elif user_input == 'west' or user_input == 'south':
        print("You can't go that way.")
    else:
        print("Sorry, I don't understand that command. Type 'HELP' for assistance.")

    return next_room


def east_cave(user_input):
    global traps_checked
    global desc_printed

    set_variable("next_room", "east_cave")

    next_room = 'east_cave'

    if not printed_rooms['east_cave']:
        print("It appears that some traps have been set off recently, judging by the arm on the floor.  \n"
              "There is smoke in the room, too, and you heard an explosion earlier. Perhaps a bomb?\n"
              "There's a broadsword in the other side of the room, too.")
        printed_rooms['east_cave'] = True

    if user_input == 'look traps':
        print("Good thing you looked at the traps closer. There is a tripwire on the ground that you surely \n"
              "would have hit walking to the broadsword. It's connected to 2 small bombs, but you can't take \n"
              "them. They are connected so that they will be triggered if simply touched. You can now get the sword safely!")
        traps_checked = True

    elif user_input == 'take broadsword' and traps_checked == False:
        print("As you walk over to the broadsword, your foot catches a tripwire. You see 2 bombs fly into the \n"
              "air, and you can guess what happens next. They explode, and you die an explosive death.\n\n")
        time.sleep(3)
        print('\n' * 5)


        for _ in range(2):
            game_over_text = "GAME OVER " * 10
            words = game_over_text.split()
            for word in words:
                print(word, end=' ', flush=True)
                time.sleep(0.1)
            print()

        print("\n\nYou exploded!")

        game_setup()

    elif user_input == 'take broadsword' and traps_checked == True:
        print("You carefully step over the tripwire, take the broadsword, and go back to the room where you \n"
              "started.")
        inventory.append('broadsword')
        next_room = 'cave'
    elif user_input == 'west':
        print("You walk west back to the cave.")
        next_room = 'cave'

    elif user_input == 'north':
        print("You can't go that way.")
    elif user_input == "":
        print("Sorry, I don't understand that command. Type 'HELP' for assistance.")
    else:
        print("Sorry, I don't understand that command. Type 'HELP' for assistance.")

    return next_room

def cave_entrance(user_input):
    set_variable("next_room", "cave_entrance")
    next_room = 'cave_entrance'

    if user_input == 'look' or user_input == 'look around':
        print("To the west, there is a shipwreck. East, a large lighthouse, although it is blocked by bushes.\n"
              "To the north, there appears to be a path leading to the lighthouse.")
        return next_room
    elif user_input == 'west':
        return 'shipwreck'
    elif user_input == 'south':
        print("You head right back to where you started.")
        next_room = 'cave'
    elif user_input == 'north':
        print("You walk north.")
        next_room = 'ocean_path'
    else:
        print("Sorry, I don't understand that command. Type 'HELP' for assistance.")

    return next_room

def shipwreck(user_input):
    set_variable("next_room", "shipwreck")
    set_variable("shipwreck_visited", True)
    next_room = 'shipwreck'

    if user_input == 'look' or user_input == 'look around':
        print("Your captain lies on the ground. A locked crate is in the water.")
    elif user_input == 'look captain' or user_input == 'check captain':
        print("Your captain has a gold key around his neck.")
    elif user_input == 'take key':
        print("You kneel down and take the golden key.")
        inventory.append('golden key')
    elif user_input == 'east':
        print("You leave the shipwreck and walk east.")
        next_room = 'cave_entrance'
    elif user_input == 'west' or user_input == 'south' or user_input == 'north':
        print("You can't go that way.")
    elif user_input == 'look crate':
        print("It's a small crate labeled 'EMERGENCY'")


    elif user_input == 'open crate':
        if 'golden key' in inventory:
            print("You use the golden key to open the crate. Inside, you find a kerosene lamp and some kerosene, as well as some matches.\n"
                  "You put some kerosene into the lamp, and save the rest for later.")
            inventory.remove('golden key')
            inventory.extend(['kerosene lamp', 'kerosene', 'matches'])
        else:
            print("The crate is locked. You need to use a key to open it.")
    else:
        print("Sorry, I don't understand that command. Type 'HELP' for assistance.")

    return next_room

def ocean_path(user_input):
    set_variable("next_room", "ocean_path")
    next_room = 'ocean_path'
    global shack_scene
    global james
    if user_input == 'look' or user_input == 'look around':
        print("To the west, you see a small shack. To the east, you see the lighthouse in the distance.")
    elif user_input == 'west' and shack_scene == False:
        next_room = 'shack'
        print("You walk over to the shack.\n\n")
        shack_scene = True
        time.sleep(1)

        if variables['shipwreck_visited']:
            shack_text = game_text.txt['shipwreck_visited']
        else:
            shack_text = game_text.txt['shipwreck_not_visited']

        if 'broadsword' in inventory:
            james = True
            shack_sword_text = game_text.txt['shack_with_sword'].format(name=name)
        else:
            james = False
            shack_sword_text = game_text.txt['shack_no_sword'].format(name=name)

        print(game_text.txt[next_room].format(name=name, shack=shack_text, shack_sword=shack_sword_text))
        if 'broadsword' in inventory:
            inventory.append('hammer')
            next_room = 'ocean_path'
        elif 'broadsword' not in inventory:
            inventory.extend(['hammer', 'pistol'])
            next_room = 'ocean_path'
    elif user_input == 'west' and shack_scene == True:
        next_room = 'shack_reentered'
    elif user_input == 'east':
        print("You walk to the lighthouse.")
        next_room = 'lighthouse'
    elif user_input == 'north':
        print("You can't go that way.")
    elif user_input == 'south':
        print("You go back to the cave's entrance.")
    elif user_input == 'west' and 'pistol' in inventory:
        print("You look at James. He says 'If you think I'm going back into that shack, you're crazy!' You walk in without him.")
        next_room = 'shack_reentered'
    else:
        print("Sorry, I don't understand that command. Type 'HELP' for assistance.")

    return next_room

def shack_reentered(user_input):
    set_variable("next_room", "shack_reentered")
    next_room = 'shack_reentered'
    print(game_text.txt["shack_reentered"])

    if user_input == 'look' or user_input == 'look around':
        print("The monster has just busted through the window, ready to kill you.")
        return next_room


    if user_input == 'stab shadow' or user_input == 'stab monster':
        if 'broadsword' in inventory:
            print("You stab the shadow like you did before. This time, though, your sword catches the light coming through the window.\n"
                  "It hits the monster directly, and it screeches. The monster disappears, although only temporarily. If you \n"
                  "can project a very bright source of light directly onto the creature, maybe you can kill it for good.")
            next_room = 'ocean_path'
        else:
            print("You don't have a good enough weapon to stab the shadow.")
    elif user_input == 'shoot shadow' or user_input == 'shoot creature':
        if 'pistol' in inventory:
            print("You shoot the creature with your pistol until it runs out of ammo. But the shadow persists. It reaches \n"
                  "out and strangles you. You watch your arms disintegrate, then your legs, and then... you are no more.")
            time.sleep(3)
            print('\n' * 5)

            for _ in range(2):
                game_over_text = "GAME OVER " * 10
                words = game_over_text.split()
                for word in words:
                    print(word, end=' ', flush=True)
                    time.sleep(0.1)
                print()

                print("\n\nThe shadow consumed you for good. Sorry!")

                game_setup()
        else:
            print("You don't have a pistol to shoot the shadow.")

    elif user_input == "north" or user_input == "south" or user_input == "west" or user_input == "east":
        print("You make a move, but the shadow quickly consumes you and you die.")
        time.sleep(3)
        print('\n' * 5)

        for _ in range(2):
            game_over_text = "GAME OVER " * 10
            words = game_over_text.split()
            for word in words:
                print(word, end=' ', flush=True)
                time.sleep(0.1)
            print()

            print("\n\nThe shadow consumed you for good. Sorry!")

            game_setup()
    else:
        print("Sorry, I don't understand that command. Type 'HELP' for assistance.")

    return next_room

def lighthouse(user_input):
    global door_broken
    set_variable("next_room", "lighthouse")
    next_room = 'lighthouse'

    if user_input == 'look' or user_input == 'look around':
        print("You've ascended the stairs of the lighthouse. However, you are now upon a wooden door that, although old, \n"
              "is locked up tight.")
        return next_room

    if user_input == 'south':
        print("You leave the lighthouse and go back to the ocean path.")
        next_room = 'ocean_path'
    elif user_input == 'east' or user_input == 'west':
        print("You can't go that way right now.")
    elif user_input == 'north' and not door_broken:
        print("You can't pass the door.")
    elif (user_input == 'attack door' or user_input == 'hit door' or user_input == 'break door') and not door_broken:
        print("Please specify the item you would like to use to break the door.")
    elif (user_input == 'attack door with hammer' or user_input == 'hit door with hammer' or user_input == 'break door with hammer') and not door_broken:
        print("You whack the door a few times. Wood falls everywhere, the hinges fall, and eventually, the door is down. You go up.")
        door_broken = True
        print(game_text.txt['endgame'].format(name=name))
        next_room = 'endgame'
    elif (user_input == 'shoot door' or user_input == 'shoot door with pistol') and not door_broken:
        if 'pistol' in inventory:
            print("You shoot the door's hinges a few times. They are old and rusty, and fall quickly under a barrage of bullets. The door is down now. You go up.")
            door_broken = True
            print(game_text.txt['endgame'].format(name=name))
            next_room = 'endgame'
        else:
            print("You don't have a pistol to shoot the door.")
    else:
        print("Sorry, I don't understand that command. Type 'HELP' for assistance.")

    return next_room

def endgame(user_input):
    global variables
    set_variable("next_room", "endgame")
    next_room = 'endgame'



    if user_input == 'look' or user_input == 'look around':
        print("The monster approaches.")
        return next_room

    elif user_input == 'turn lens':
        print(game_text.txt['creature_dead'].format(name=name))
        time.sleep(3)
        print(game_text.txt['the_end'].format(name=name))
        input("Press enter to continue...")
        print(game_text.txt['end_txt'].format(name=name))
        sys.exit()

    else:
        print("Sorry, I don't understand that command. Type 'HELP' for assistance.")

    return next_room

def game_loop():
    global name
    global variables
    next_room = variables['next_room']

    while True:
        if next_room in printed_rooms and not printed_rooms[next_room] and next_room != 'endgame':
            if next_room != 'cave':
                print(game_text.txt[next_room].format(name=name))
                printed_rooms[next_room] = True

        user_input = input("\nWhat would you like to do? >> ").strip().lower()

        if user_input == "":
            continue
        elif user_input == 'help':
            help_txt()
        elif 'inspect' in user_input:
            item = user_input.split("inspect", 1)[-1].strip()
            item_desc(item)
            continue
        elif user_input == 'inventory':
            print_inv()
            continue
        elif user_input == 'save':
            save()
            continue
        elif user_input == 'load':
            load()
            continue

        if next_room != 'east_cave' and printed_rooms['east_cave']:
            printed_rooms['east_cave'] = False
        elif next_room != 'cave_entrance' and printed_rooms['cave_entrance']:
            printed_rooms['cave_entrance'] = False
        elif next_room != 'shipwreck' and printed_rooms['shipwreck']:
            printed_rooms['shipwreck'] = False
        elif next_room != 'ocean_path' and printed_rooms['ocean_path']:
            printed_rooms['ocean_path'] = False
        elif next_room != 'shack' and printed_rooms['shack']:
            printed_rooms['shack'] = False
        elif next_room != 'shack_reentered' and printed_rooms['shack_reentered']:
            printed_rooms['shack_reentered'] = False
        elif next_room != 'lighthouse' and printed_rooms['lighthouse']:
            printed_rooms['lighthouse'] = False
        elif next_room != 'endgame' and printed_rooms['endgame']:
            printed_rooms['endgame'] = False

        if variables['next_room'] == 'cave':
            next_room = cave(user_input)
        elif variables['next_room'] == 'east_cave':
            next_room = east_cave(user_input)
        elif variables['next_room'] == 'cave_entrance':
            next_room = cave_entrance(user_input)
        elif variables['next_room'] == 'shipwreck':
            next_room = shipwreck(user_input)
        elif variables['next_room'] == 'ocean_path':
            next_room = ocean_path(user_input)
        elif variables['next_room'] == 'shack_reentered':
            next_room = shack_reentered(user_input)
        elif variables['next_room'] == 'lighthouse':
            next_room = lighthouse(user_input)
        elif variables['next_room'] == 'endgame':
            next_room = endgame(user_input)

        set_variable("next_room", next_room)





def game_setup():
    global name
    global inventory

    while True:
        variables['next_room'] = 'cave'

        inventory = ['knife']
        name = input("Please enter your name: ")
        if not name.strip():
            print("Please enter a name.")
        else:
            confirmation = input(f"You entered '{name}'. Are you sure this is correct?")
            if confirmation.lower() == 'yes':
                break
            elif confirmation.lower() == 'no':
                continue

    print("Typing 'HELP' at any point will bring up some basic directions. You may try it when the text prompt appears.\n")

    print(game_text.txt["cave"].format(name=name))


    game_loop()

game_setup()
