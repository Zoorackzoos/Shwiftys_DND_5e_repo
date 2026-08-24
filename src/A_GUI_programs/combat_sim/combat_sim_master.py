"""
the goal of this file is to:
1. ✅ calculate initiative and use a step system
   ✅ to tell you who's initiative it is
2. ✅ take in damage against monsters and tell if they're dead or not. hp stored as a variable
3. ✅ take in healing against monsters and tell they're new hp value. hp stored as a variable
4. ❌ have monster dictionaries stored in a array.
    a. instead of crafting markdown files that contain the stat block for every new monster
       so this program is normalized...
       instead i will put in values to the spreadsheet from the "update_homebrew_monster.py"
       keys.
    b. from there i can craft temp dictionaries and put them in the array. or something similar.
    c. the monster list will be modified in the source code, not via the GUI.
5. ✅ smooth GUi interface. interaction instructions top,
   get_damage_and_chance_to_hit.py stuff middle, verbose bullshit below that.
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

    combat_sim_master_path_to_monsters_all_stats_homebrew_csv_file = \
    "../../../sheets/monsters_all_stats_homebrew/monsters_all_stats_homebrew.csv"

    combat_sim_cycle_combat(
        initiative_rolls_dictionary=initiative_rolls_dictionary,
    )

if __name__ == "__main__":
   combat_sim_master()