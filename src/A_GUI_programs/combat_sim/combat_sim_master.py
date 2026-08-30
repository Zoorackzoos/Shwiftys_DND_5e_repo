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
from A_GUI_programs.combat_sim.combat_sim_get_monster_list_thru_menu import combat_sim_get_monster_list_thru_menu
from A_GUI_programs.combat_sim.combat_sim_initative import take_initiative_roles
from A_GUI_programs.universal_terminal_clear import universal_terminal_clear
from universal_functions.spreadsheet_stuff.dict_based_database_interpretors.get_dict_from_csv_file import \
    get_dict_from_csv_file
from universal_functions.spreadsheet_stuff.dict_based_database_interpretors.get_rows_from_dict_on_param_type_and_string import \
    get_rows_from_dict_on_param_type_and_string
from universal_functions.enums.spreadsheet_enums import SpreadsheetKeysEnums

def get_default_monster_list(
        monsters_all_stats_homebrew_dict
):
    """
    a goblin
    a skeleton
    a "Dragon, Chromatic, Black, Young"

    the reason they're called monster_name[0] in the dictionary delcartion
    is becuase this funciton "get_rows..." retruns a list of dictionaries.
        since my query is specfici enough were it returns a list with 1 dictionary
        we just use list[0] to get that 1 monster.
    """
    goblin_list_that_contains_dict = get_rows_from_dict_on_param_type_and_string(
        dict_in_question=monsters_all_stats_homebrew_dict,
        param_type=SpreadsheetKeysEnums.NAME.value,
        string="goblin",
        tab_amount=""
    )
    skeleton_list_that_contains_dict = get_rows_from_dict_on_param_type_and_string(
        dict_in_question=monsters_all_stats_homebrew_dict,
        param_type=SpreadsheetKeysEnums.NAME.value,
        string="skeleton",
        tab_amount=""
    )
    chromatic_blank_young_dragon_list_that_contains_dict = get_rows_from_dict_on_param_type_and_string(
        dict_in_question=monsters_all_stats_homebrew_dict,
        param_type=SpreadsheetKeysEnums.NAME.value,
        string="Dragon, Chromatic, Black, Young",
        tab_amount=""
    )

    # you'd figure i would be taught how to name variables by now but no.
    # "fuck them kids" -every university on earth.
    list_that_contains_dictionaries_that_are_monsters = \
        [
            goblin_list_that_contains_dict[0],
            skeleton_list_that_contains_dict[0],
            chromatic_blank_young_dragon_list_that_contains_dict[0]
        ]

    return list_that_contains_dictionaries_that_are_monsters

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

    # fetching the large ahh dictionary
    combat_sim_cycle_combat_path_to_monsters_csv_file = \
        "../../../sheets/monsters_all_stats_homebrew/monsters_all_stats_homebrew.csv"
    monsters_all_stats_homebrew_dict = get_dict_from_csv_file(
        path_to_csv_file=combat_sim_cycle_combat_path_to_monsters_csv_file)

    # also gets overwritten by combat_sim_get_monster_list_thru_menu() later.
    list_that_contains_dictionaries_that_are_monsters = get_default_monster_list(
        monsters_all_stats_homebrew_dict=monsters_all_stats_homebrew_dict
    )

    # this skips initiative and also monster selection
    if possible_skip_code == "skip_i":
        #skipping initative inputs
        pass
    else:
        list_that_contains_dictionaries_that_are_monsters = combat_sim_get_monster_list_thru_menu(
            monsters_all_stats_homebrew_dict=monsters_all_stats_homebrew_dict
        )
        initiative_rolls_dictionary = take_initiative_roles()

    combat_sim_cycle_combat(
        initiative_rolls_dictionary=initiative_rolls_dictionary,
        list_that_contains_dictionaries_that_are_monsters=list_that_contains_dictionaries_that_are_monsters
    )

if __name__ == "__main__":
   combat_sim_master()