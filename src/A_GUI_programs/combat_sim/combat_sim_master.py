"""
the goal of this file is to:
1. ✅ calculate initiative and use a step system
   ✅ to tell you who's initiative it is
2. ✅ take in damage against monsters and tell if they're dead or not. hp stored as a variable
3. ✅ take in healing against monsters and tell they're new hp value. hp stored as a variable
4. 🤙 have monster dictionaries stored in a list.
    a. i was just speculating on how monsters would work here.
    b. they're in a list, but like. the attack feature isn't there.
    c. the spreadsheet would need a way to hold the action / attack information. and i'm not sure about that.
5. ✅ smooth GUi interface. interaction instructions top,
   get_damage_and_chance_to_hit.py stuff middle, verbose bullshit below that.
6. ❌ monsters can attack with accurate attack information
7. ❌ utility abilities are showcased
8. ❌ GUI shows how many actions / multiattacks a monster has left in the attack GUI
    a. so if you have a monster attack, and they can attack twice the gui would say
    something like 1/2 actions used or something.
9. ❌ monster list selections screen
    a. like you are asked which encounter you want to run.
    b. this means you have to have manually loaded monsters
    c. and those monsters have to have acceptable spreadsheet values.
10. ❌ make action "markdown to dictionary" parser.
    a. i'll read a stat block, put that information into a markdown file
    b. i'll put that markdown file through the markdown parser,
     and it will create a list of dictionaries that will store the attack information
    c. that information will be stored in teh spreadsheet cells.
        i. is that a good idea though?
        ii. counter question, it's not lik putting each action in their separate cell is a better idea.
11. ❌ design and implement legendary actions
"""
import time

from A_GUI_programs.combat_sim.combat_sim_cycle_combat import combat_sim_cycle_combat
from A_GUI_programs.combat_sim.combat_sim_initative import take_initiative_roles
from A_GUI_programs.universal_terminal_clear import universal_terminal_clear


def ask_to_run_combat_sim_master():
    print("You've ran \"combat_sim_master.py\" . Would you like to continue? (y/n)")
    user_info = input()
    while user_info != ["y", "n", "skip_i"]:
        if user_info == "y":
            print("running program...")
            time.sleep(0.5) #just give me some breathing thinking room
            return None
        elif user_info == "n":
            print("exiting program.")
            exit(0)
        elif user_info == "skip_i":
            print("you're skipping the initiative setting with default values.")
            time.sleep(0.5)
            universal_terminal_clear()
            return "skip_i"
        else:
            universal_terminal_clear()
            print("You've ran \"combat_sim_master.py\" . Would you like to continue? (y/n)")
            user_info = input("Invalid input. Must be 'y' or 'n'\n")

    print("ERROR: ask_to_run_combat_sim_master: broke out of while user_info loop. shidding pants and returning None.")
    return None


def combat_sim_master():
    universal_terminal_clear()
    possible_skip_code = ask_to_run_combat_sim_master()

    #these are default values, they get pasted over by "take_initiative_roles()"
    initiative_rolls_dictionary = \
    {
        "Mikey": 1,
        "Forest": 2,
        "Thalis": 3,
        "Micheal": 4,
        "Evil": 5,  # these are the monsters, AKA the bad guys.
        "Good": None  # these are DM controlled allies. They're not always there so this can be Null.
    }

    if possible_skip_code == "skip_i":
        #skipping initative inputs
        pass
    else:
        initiative_rolls_dictionary = take_initiative_roles()

    combat_sim_cycle_combat(
        initiative_rolls_dictionary=initiative_rolls_dictionary,
    )

if __name__ == "__main__":
   combat_sim_master()