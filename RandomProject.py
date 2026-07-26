import sys
import time


MAX_SUSPENSE_LEVEL = 5


def add_item_to_inventory(inventory, item):
    if item not in inventory:
        inventory.append(item)
    return inventory


def update_suspense_level(current_level, action):
    if action == "raise":
        return min(current_level + 1, MAX_SUSPENSE_LEVEL)
    if action == "lower":
        return max(current_level - 1, 0)
    return current_level


def show_status(player_name, inventory, suspense_level):
    slow_print(f"{player_name}'s status")
    slow_print(f"Inventory: {', '.join(inventory) if inventory else 'empty'}")
    slow_print(f"Suspense: {'█' * suspense_level}{'░' * (MAX_SUSPENSE_LEVEL - suspense_level)}")
    print()


# slow_print function is defined here to create the typing effect.
def slow_print(text, speed=0.06):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    print()

# This allows the user to save their progress
def save_game(player_name, chapter_name):
    with open("save_data.txt", "w") as file:
        file.write(player_name + "\n")
        file.write(chapter_name + "\n")
    slow_print("\n[ Progress saved automatically ]\n")

# Allows the user to load in their saved game.
def load_game():
    try:
        with open("save_data.txt", "r") as file:
            lines = file.readlines()
            if len(lines) >= 2:
                name = lines[0].strip()
                chapter = lines[1].strip()
                return name, chapter
    except FileNotFoundError:
        # If the file doesn't exist yet (first time playing), return None.
        return None    

# Porch function is defined here as a key part in the program.
def porch(player_name, inventory, suspense_level):
    slow_print("You walk to your front porch and see a package sitting there. It's pretty big, but it has no return address. You pick it up and notice a note attached to it.")
    slow_print("The note reads: Dear " + player_name + ",\n\nInside this package, you will find the tools and instructions you need to participate. Remember, time is of the essence. Good luck, agent.\n\n- The Anomaly")
    inventory = add_item_to_inventory(inventory, "mysterious package")
    suspense_level = update_suspense_level(suspense_level, "raise")
    print()
    slow_print("Take the package inside? (y/n): ")
    take_package = input()


    if take_package.lower() == 'y':
        slow_print("You bring the package along with you and place it on the kitchen counter. You open it and find a pair of glasses, a pen, and a sort of book.")
        inventory = add_item_to_inventory(inventory, "glasses")
        inventory = add_item_to_inventory(inventory, "mysterious pen")
        inventory = add_item_to_inventory(inventory, "lab notebook")
        suspense_level = update_suspense_level(suspense_level, "raise")
        show_status(player_name, inventory, suspense_level)
        slow_print("You: Looks pretty normal. I wonder what these are for...")
        slow_print("There is another note inside the box. It reads: \"This box contains all the lab equipment you need. The pen has a vial of a deadly neurotoxin inside it. You will be the first one to be testing it. You will have a specialized databook you will use to record results. I have also included the address of the area that you will be working in. It is highly secretive, so do not forget it. You have been given the sum of $1,000. You will be paid more later.\"")
        print()
        slow_print("You have been given the sum of $1,000. You will be paid more later.")
        print()
        slow_print("Good luck, " + player_name + "\"", speed=0.1)
        print()
        slow_print("You: How does he even know my name? And I'm not a killer! I wouldn't even be needing this!")
        print()
        slow_print("You fiddle with the pen for a while and discover that it can't even write. You pretty much stuff the pen in your pocket and shelve the rest, forgetting all about it.")
       
        time.sleep(2.5)
       
        slow_print("[ This is the end of Chapter 1 ]", speed=0.1)
        time.sleep(1.5)
        save_game(player_name, "Chapter 2")
        slow_print("Proceed to Chapter 2? (y/n)", speed=0.07)
        chapter_2_proceed = input()
        if chapter_2_proceed.lower() == 'y':
            return chapter_2(player_name, inventory, suspense_level)
        else:
            slow_print("You decide to take a break and relax for a while. You will be back where you started.")    
            sys.exit()

    return inventory, suspense_level

# Chapter 2 events.
def chapter_2(player_name, inventory, suspense_level):
    print()
    slow_print("7:16 AM. Papa John's Diner, Palm Beach, Florida.")
    print()
    slow_print("You are enjoying your usual breakfast of waffles and coffee, but you are interrupted by a knocking sound on the window.")
    time.sleep(0.8)
    slow_print("You can't see the source of the noise.")
    time.sleep(1)
    slow_print("Check it out? (y/n)")
    building_exit = input(">> ")
    return diner(building_exit, player_name, inventory, suspense_level)


def diner(building_exit, player_name, inventory, suspense_level):
    if building_exit.lower() == 'y':
        slow_print("You pause your meal and exit through the back door.")
        print()
        slow_print("You see a shady figure leaning against the diner wall. He (or she) is wearing completely black clothing with a mask that covers their entire face. You can't see any of their features.")
        suspense_level = update_suspense_level(suspense_level, "raise")
        inventory = add_item_to_inventory(inventory, "shadowy clue")
        show_status(player_name, inventory, suspense_level)
        print()
        time.sleep(1.5)
       
        slow_print("Choose what you say (or do):", speed=0.05)
        print("[1] \"What do you want? You're knocking recklessly!\"")
        print("[2] Go back inside")


        slow_print("Your choice (1-2): ", speed=0.07)
        choice = input(">> ")


        if choice == "1":
            slow_print("You: What do you want? You're knocking recklessly!")
            time.sleep(1.5)
            print()
            slow_print("*Silence*")
            time.sleep(1)
            slow_print("Choose what you say (or do):", speed=0.05)
            print("[1] \"I said, what do you want?\"")
            print("[2] \"I'm not going to ask again. So I'm going to go back inside.\"")


            slow_print("Your choice (1-2): ", speed=0.07)
            choice = input(">> ")
            if choice == "1":
                slow_print("You: I said, what do you want?")
                time.sleep(1.5)
                slow_print("*Silence*")
                return proceeding_events_chapter_2(player_name, inventory, suspense_level)


            elif choice == "2":
                slow_print("You: I'm not going to ask again. So I'm going to go back inside.")
                time.sleep(1)
                slow_print("The figure doesn't respond. It reaches into its pocket and pulls out a small device. Instinct takes over, and you sprint away to your car and drive off. You don't look back.")
                sys.exit()    


        elif choice == "2":
            slow_print("You: I don't have time for this. I'm going inside.")
            time.sleep(1)
            slow_print("You go back inside and continue your meal, trying to forget the strange encounter.")
            sys.exit()
    else:
        slow_print("You ignore the knocking and finish your food peacefully.")
        sys.exit()


def proceeding_events_chapter_2(player_name, inventory, suspense_level):
    time.sleep(1.5)
    slow_print("Choose what you say (or do):", speed=0.05)
    print("[1] \"Are you even alive?!\"")
    print("[2] \"I'm not joking around! I want answers or I'm calling the police!\"")
    print("[3] \"I don't have time for this. I'm going inside.\"")
   
    slow_print("Your choice (1-3): ", speed=0.07)
    choice = input(">> ")


    if choice == "1":
        slow_print("You: Are you even alive?!")
        time.sleep(2)
        slow_print("???: You don't talk to the Anomaly that way.")
        suspense_level = update_suspense_level(suspense_level, "raise")
        inventory = add_item_to_inventory(inventory, "strange note")
        show_status(player_name, inventory, suspense_level)
        slow_print("Choose what you say (or do):", speed=0.05)
        print("[1] \"Say what?\"")
        print("[2] \"Whatever. I don't care.\"")
       
        slow_print("Your choice (1-2): ", speed=0.07)
        choice = input()
        if choice == "1":
            slow_print("You: Say what?")
            time.sleep(1)
            slow_print("The figure lunges at you, and a bag is swept over your head. You feel yourself being dragged away, and you lose consciousness.")
            time.sleep(2)
            slow_print("[ This is the end of Chapter 2 ]", speed=0.1)
            time.sleep(1.5)
            save_game(player_name, "Chapter 3")
            slow_print("Chapter 3 is coming soon!", speed=0.07)
            return inventory, suspense_level
           
        elif choice == "2":
            slow_print("You: Whatever. I don't care.")
            time.sleep(1)
            slow_print("The figure lunges at you, but you dodge the attack. You run back to your car and lock the doors. The figure doesn't follow you. It just watches as you call the police.")
            suspense_level = update_suspense_level(suspense_level, "lower")
            return inventory, suspense_level


    elif choice == "2":
        slow_print("You: I'm not joking around! I want answers or I'm calling the police!")
        time.sleep(1)
        slow_print("???: ...")
        time.sleep(0.8)
        print()
        slow_print("???: You have refused to cooperate. I'll have to do something about that.")
        slow_print("The figure reaches into its pocket and pulls out a small device. They press it, and a bright light flashes in your eyes. You feel your body go numb, and you collapse to the ground.")
        time.sleep(2)
        slow_print("[ This is the end of Chapter 2 ]", speed=0.1)
        time.sleep(1.5)
        save_game(player_name, "Chapter 3")
        slow_print("Chapter 3 is coming soon!", speed=0.07)
        return inventory, suspense_level
       
    elif choice == "3":
        slow_print("You: I don't have time for this. I'm going inside.")
        time.sleep(1)
        slow_print("The figure doesn't respond. You go back into the diner and continue your breakfast.")
        suspense_level = update_suspense_level(suspense_level, "lower")
        return inventory, suspense_level

    return inventory, suspense_level




# --- GAME RUN STARTING HERE ---

def main():
    slow_print("Before the project is begun, enter your name:")
    player_name = input(">> ")
    inventory = []
    suspense_level = 0
    print()
    
    # Check if there's a saved game
    saved_data = load_game()
    if saved_data is not None:
        saved_name, saved_chapter = saved_data
        slow_print(f"Welcome back, {saved_name}!")
        print()
        slow_print(f"Resume from {saved_chapter}? (y/n): ")
        resume = input(">> ")
        if resume.lower() == 'y':
            player_name = saved_name
            if saved_chapter == "Chapter 2":
                chapter_2(player_name, inventory, suspense_level)
                return
            elif saved_chapter == "Chapter 3":
                slow_print("Chapter 3 is not yet available. Starting from Chapter 2.")
                chapter_2(player_name, inventory, suspense_level)
                return
    
    # Start new game from the beginning
    slow_print("3:05 PM. Palm Beach, Florida.")
    print()
    slow_print("You are in your living room, sitting alone with a cup of coffee and thinking about life.")
    time.sleep(2)
    
    slow_print("Incoming call...")
    time.sleep(1.5)
    
    slow_print("Pick up the call? (y/n): ")
    pick_call = input(">> ")
    
    if pick_call.lower() == 'y':
        print()
        slow_print("You: Hello? Who is this?")
        time.sleep(1.5)
        
        slow_print("???: Welcome to the Random Project. You have been chosen for a very special operation. You will be debriefed later on the details. For now, it is up to you. Good luck, agent.")
        time.sleep(2.5)
        
        slow_print("Choose what you say (or do):", speed=0.05)
        print("[1] \"Wait, what? Who are you? What operation? I don't even get what you're talking about!\"")
        print("[2] Cut the call")
        
        slow_print("Your choice (1-2): ", speed=0.07)
        choice = input(">> ")
        if choice == "1":    
            slow_print("You: Wait, what? Who are you? What operation? I don't even-")
            time.sleep(0.2)
            slow_print("???: No time for questions. I cannot say any more.")
            print()
            time.sleep(1.5)
        elif choice == "2":
            slow_print("*Click*")
            time.sleep(0.5)
            slow_print("You cut the call, drop the phone on the tea table, and continue sipping your coffee.")
            time.sleep(1)
            slow_print("You: What a weird call. I wonder if it was a prank or something.")
            sys.exit()    
           
        slow_print("Choose what you say (or do):", speed=0.05)
        print("[1] \"Um... fine. Just tell me where I need to go.\"")
        print("[2] \"You're crazy. I'm hanging up.\"")
        print("[3] \"I'm not doing anything until you tell me who you are!\"")
        
        slow_print("Your choice (1-3): ", speed=0.07)
        choice = input(">> ")
        print()
       
        if choice == "1":
            slow_print("You: Um... fine. Just tell me where I need to go.")
            time.sleep(1)
            slow_print("???: Spoken like a true professional. Check your front porch. There's something there.")
            time.sleep(1.5)
            slow_print("Check your porch? (y/n): ")
            check_porch = input(">> ")
            if check_porch.lower() == 'y':
                inventory, suspense_level = porch(player_name, inventory, suspense_level)
            elif check_porch.lower() == 'n':
                slow_print("Guess you weren't ready for this after all.")    
                sys.exit()
        
        elif choice == "2":
            slow_print("You: You're crazy. I'm hanging up.")
            time.sleep(1)
            slow_print("*Click*")
            time.sleep(1)
            slow_print("You drop the phone back on the tea table, then continue sipping your coffee.")
            sys.exit()
       
        elif choice == "3":
            slow_print("You: I'm not doing anything until you tell me who you are!")
            time.sleep(1)
            slow_print("???: *Sighs* Stubborn. You haven't changed a bit. Be gone. You have no place.")
            sys.exit()
       
        else:
            slow_print("You stare at the phone in stunned silence, unable to find your words.")
            time.sleep(1.5)
            slow_print("???: Silence is fine. Just go. You are not worthy and He is already watching you.")
            slow_print("*Click*")
            sys.exit()
    
    elif pick_call.lower() == 'n':
        slow_print("*Click*")
        time.sleep(1)
        slow_print("You drop the phone back on the tea table, then continue sipping your coffee.")
        sys.exit()


if __name__ == "__main__":
    main()
