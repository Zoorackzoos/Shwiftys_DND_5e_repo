import contextlib
import datetime
from pathlib import Path

import keyboard

from A_GUI_programs.combat_sim.get_sorted_initiative_rolls_from_greatest_to_least import \
    get_sorted_initiative_rolls_from_greatest_to_least
from A_GUI_programs.confirm_quit_via_keyboard import confirm_quit_via_keyboard
from A_GUI_programs.universal_terminal_clear import universal_terminal_clear
from universal_functions.spreadsheet_stuff.dict_based_database_interpretors.get_dict_from_csv_file import \
    get_dict_from_csv_file
from universal_functions.spreadsheet_stuff.dict_based_database_interpretors.get_rows_from_dict_on_param_type_and_string import \
    get_rows_from_dict_on_param_type_and_string
from universal_functions.vars.enums.spreadsheet_enums import SpreadsheetKeysEnums


def _build_monster_row_formatter(list_that_contains_dictionaries_that_are_monsters):
    """
    Scans all monster dicts once and returns a function that formats a single
    monster dict into an aligned "name : max_hp : current_hp : ac : life_status"
    row, padded to the widest value seen in each column.

    claude made this
    """
    columns = ["Name", "HP", "current_hp", "AC", "life_status"]
    labels = {"Name": "name", "HP": "max_hp", "current_hp": "current_hp", "AC": "ac", "life_status": "life_status"}

    widths = {}
    for col in columns:
        max_width = len(labels[col])
        for monster_dict in list_that_contains_dictionaries_that_are_monsters:
            max_width = max(max_width, len(str(monster_dict[col])))
        widths[col] = max_width

    def format_header():
        return " : ".join(f"{labels[col]:<{widths[col]}}" for col in columns)

    def format_row(monster_dict):
        return " : ".join(f"{str(monster_dict[col]):<{widths[col]}}" for col in columns)

    return format_header, format_row

def detect_if_NPC_and_display_monster_if_yes(
        sub_list,
        list_that_contains_dictionaries_that_are_monsters,
        selected_npc_bool,
        selected_npc_index,
        npc_interaction_menu_bool,
        npc_interaction_menu_index,
        performing_attack_bool,
        performing_damage_bool,
        performing_heal_bool,
        damage_or_heal_integer_that_actually_a_string
):
    """
    displays good or evil NPC monsters.
    claude updated this
    """
    if sub_list[0].lower() == "evil" or sub_list[0].lower() == "good":
        format_header, format_row = _build_monster_row_formatter(list_that_contains_dictionaries_that_are_monsters)
        print("\t\t  ", format_header())

        if selected_npc_bool:
            monster_dict_index = 0
            for monster_dict in list_that_contains_dictionaries_that_are_monsters:
                marker = "\t\t →" if monster_dict_index == selected_npc_index else "\t\t  "
                print(marker, format_row(monster_dict))
                monster_dict_index += 1

        elif npc_interaction_menu_bool:
            interaction_option_menu_string_list = \
                [
                    "make this monster attack",
                    "make this monster take damage",
                    "make this monster heal health"
                ]
            monster_dict_index = 0
            for monster_dict in list_that_contains_dictionaries_that_are_monsters:
                if monster_dict_index == selected_npc_index:
                    print("\t\t →", format_row(monster_dict))
                    gui_logic_interaction_menu_index = 0
                    for string in interaction_option_menu_string_list:
                        if gui_logic_interaction_menu_index == npc_interaction_menu_index:
                            print("\t\t\t →", string)
                            if performing_attack_bool == True:
                                print("\t\t\t\t →",
                                      "detect_if_NPC_and_display_monster_if_yes: performing_attack_bool == True")
                            elif performing_damage_bool == True:
                                print("\t\t\t\t →", "how much damage does", monster_dict["Name"], "take?")
                                print("\t\t\t\t →", damage_or_heal_integer_that_actually_a_string)
                            elif performing_heal_bool == True:
                                print("\t\t\t\t →", "how much health does", monster_dict["Name"], "heal?")
                                print("\t\t\t\t →", damage_or_heal_integer_that_actually_a_string)
                        else:
                            print("\t\t\t  ", string)
                        gui_logic_interaction_menu_index += 1
                else:
                    print("\t\t  ", format_row(monster_dict))
                monster_dict_index += 1

        else:
            for monster_dict in list_that_contains_dictionaries_that_are_monsters:
                print("\t\t  ", format_row(monster_dict))


def update_combat_sim_cycle_combat_interface(
        sorted_initiative_rolls_list,
        user_selected_initiative_roll,
        system_selected_initiative_roll,
        list_that_contains_dictionaries_that_are_monsters,
        selected_npc_bool,
        selected_npc_index,
        selected_pc_bool,
        npc_interaction_menu_bool,
        npc_interaction_menu_index,
        performing_attack_bool,
        performing_damage_bool,
        performing_heal_bool,
        damage_or_heal_integer_that_actually_a_string
):
    """
    This is also called "the update function" in other comment.s
    Any time I need a new GUI blurb dynamically, I usually add a new variable, and a if statement here.

    :param sorted_initiative_rolls_list:
        list of mini lists. 1st value = name, 2nd value = initiative roll (integer)
    :param user_selected_initiative_roll:
        AKA "sorted_initiative_rolls_list[user_initiative_roll_index]". The index increases or decreased based on how
        the user pressed the up or down arrow. It updates dynamically here to show which menu option is selected
    :param system_selected_initiative_roll:
        AKA "sorted_initiative_rolls_list[system_initative_roll_index]". That index increased based on how many times
        "t" was pressed to increment the turn.
    :param list_that_contains_dictionaries_that_are_monsters:
        list --> dictionary --> keys --> values.
    :param selected_npc_bool:
        if you pressed right while on a NPC in the menu, this is triggered to draw the child menu which allows you to
        select the specific NPC.
    :param selected_npc_index:
        this is a index to let the GUI know where you are in the specific NPC selection menu.
        also used to tell the damage and heal logic which monster to modify.
    :param selected_pc_bool:
        doesn't really do anything right now because design-wise PCs are not advocated for.
    :param npc_interaction_menu_bool:
        tells the GUI you've selected a specific NPC, and now you want to choose which interaction to do on it.
    :param npc_interaction_menu_index:
        tells the GUI where you are in the interaction menu.
    :param performing_attack_bool:
        tells the GUI you want the monster to attack
        from there you can:
        * select the monster's attack action
        * whether you have a action left
        * depending on the action,
            * it tells you what it got to hit and what damage
            * it tells you what the attacked person must get as a save and the damage.
    :param performing_damage_bool:
        tells the GUI and the logic minorly that the user is inputting a integer that is the damage
         being dealt to the monster
    :param performing_heal_bool:
        the same as performing_damage_bool but healing instead of damaging.
    :param damage_or_heal_integer_that_actually_a_string:
        this integer holds the damage a monster is dealt or the health a monster is healed.
        this is only a positive number. heal or hurt is determined by the bools.
    :return:
        returns nothing. this is a GUI printer.
    """
    universal_terminal_clear()

    update_combat_sim_cycle_combat_interface_start = """update_combat_sim_cycle_combat_interface
    you are in combat now.
    Press 'q' to quit.
    the '→' character indicates which PC / NPC 's you've selected.
    the '!" character indicates which PC / NPC 's turn it is to play.
    Use the UP and DOWN arrow key to go between PCs or NPCs.
    Use the RIGHT arrow on a parent NPC label to choose which NPC to interact with.
    from there, use the RIGHT arrow on a NPC to go to a menu. 
    from there you can either:
        * make them do an attack. Either hit something or a make someone else do a saving throw.
        * make them take damage which an integer you input.
        * make them heal with an integer you input.
    Use the "T" button to cycle through turns once the selected one has ended. (T for turn)
    Use the LEFT arrow to go back in the menu.
"""
    print(update_combat_sim_cycle_combat_interface_start)

    # printing the NPCs and PCs
    for sub_list in sorted_initiative_rolls_list:
        # i'm comparing the names because list versus list can be fucky.
        # is both a system and user selected initiative roll
        #  sub_list[0] name    #sub_list[0] name
        if (sub_list[0] == user_selected_initiative_roll[0]
                and
                sub_list[0] == system_selected_initiative_roll[0]):
            if selected_pc_bool == True:
                print("\t!→", sub_list[0], ":", sub_list[1])
                print("\t\t  ","no pc interactions yet sorry >_<")
            else:
                print("\t!→", sub_list[0], ":", sub_list[1])
                detect_if_NPC_and_display_monster_if_yes(
                    sub_list=sub_list,
                    list_that_contains_dictionaries_that_are_monsters=list_that_contains_dictionaries_that_are_monsters,
                    selected_npc_bool=selected_npc_bool,
                    selected_npc_index=selected_npc_index,
                    npc_interaction_menu_bool=npc_interaction_menu_bool,
                    npc_interaction_menu_index=npc_interaction_menu_index,
                    performing_attack_bool=performing_attack_bool,
                    performing_damage_bool=performing_damage_bool,
                    performing_heal_bool=performing_heal_bool,
                    damage_or_heal_integer_that_actually_a_string=damage_or_heal_integer_that_actually_a_string
                )
        # is a system selected initiative roll
        elif sub_list[0] == system_selected_initiative_roll[0]:
            print("\t! ", sub_list[0], ":", sub_list[1])
            detect_if_NPC_and_display_monster_if_yes(
                sub_list=sub_list,
                list_that_contains_dictionaries_that_are_monsters=list_that_contains_dictionaries_that_are_monsters,
                selected_npc_bool=selected_npc_bool,
                selected_npc_index=selected_npc_index,
                npc_interaction_menu_bool=npc_interaction_menu_bool,
                npc_interaction_menu_index=npc_interaction_menu_index,
                performing_attack_bool=performing_attack_bool,
                performing_damage_bool=performing_damage_bool,
                performing_heal_bool=performing_heal_bool,
                damage_or_heal_integer_that_actually_a_string=damage_or_heal_integer_that_actually_a_string
            )
        # is a user selected initiative roll
        elif sub_list[0] == user_selected_initiative_roll[0]:
            if selected_pc_bool == True:
                print("\t →", sub_list[0], ":", sub_list[1])
                print("\t\t  ", "no pc interactions yet sorry >_<")
            else:
                print("\t →", sub_list[0], ":", sub_list[1])
                detect_if_NPC_and_display_monster_if_yes(
                    sub_list=sub_list,
                    list_that_contains_dictionaries_that_are_monsters=list_that_contains_dictionaries_that_are_monsters,
                    selected_npc_bool=selected_npc_bool,
                    selected_npc_index=selected_npc_index,
                    npc_interaction_menu_bool=npc_interaction_menu_bool,
                    npc_interaction_menu_index=npc_interaction_menu_index,
                    performing_attack_bool=performing_attack_bool,
                    performing_damage_bool=performing_damage_bool,
                    performing_heal_bool=performing_heal_bool,
                    damage_or_heal_integer_that_actually_a_string=damage_or_heal_integer_that_actually_a_string
                )
        else:
            print("\t  ", sub_list[0], ":", sub_list[1])
            detect_if_NPC_and_display_monster_if_yes(
                sub_list=sub_list,
                list_that_contains_dictionaries_that_are_monsters=list_that_contains_dictionaries_that_are_monsters,
                selected_npc_bool=selected_npc_bool,
                selected_npc_index=selected_npc_index,
                npc_interaction_menu_bool=npc_interaction_menu_bool,
                npc_interaction_menu_index=npc_interaction_menu_index,
                performing_attack_bool=performing_attack_bool,
                performing_damage_bool=performing_damage_bool,
                performing_heal_bool=performing_heal_bool,
                damage_or_heal_integer_that_actually_a_string=damage_or_heal_integer_that_actually_a_string
            )


def combat_sim_cycle_combat(
        initiative_rolls_dictionary,
):
    if initiative_rolls_dictionary is None:
        exit("ERROR: combat_sim_cycle_combat: initative_roles_dict is None.")

    """
    # sort initiative roles based from first to last. 20 means first 1 means last.
    #   to do this i'm going to have 'the structure that contains this' to be:
    #   a list
    #   that contains lists 
    #       with the 1st value in the sub-list be the PC / NPC's name
    #       the 2nd will be their roll (integer)
    """
    unsorted_initiative_rolls_list = []

    # add the roles to the rolls list
    for name, initiative_roll in initiative_rolls_dictionary.items():
        name_and_roll_list = [name, initiative_roll]
        unsorted_initiative_rolls_list.append(name_and_roll_list)

    current_time_var = str(datetime.datetime.now())[0:10]

    log_directory = Path("sorting_algo_log_folder")
    log_directory.mkdir(exist_ok=True)

    log_file_name = current_time_var + "_TERMINAL_OUTPUT_get_sorted_initiative_rolls_from_greatest_to_least.log"

    log_file_path = log_directory / log_file_name

    with open(log_file_path, "w") as log_file:
        with contextlib.redirect_stdout(log_file):
            sorted_initiative_rolls_list = get_sorted_initiative_rolls_from_greatest_to_least(
                unsorted_initiative_rolls_list=unsorted_initiative_rolls_list
            )

    universal_terminal_clear()

    # fetching the large ahh dictionary
    combat_sim_cycle_combat_path_to_monsters_csv_file = \
        "../../../sheets/monsters_all_stats_homebrew/monsters_all_stats_homebrew.csv"
    monsters_all_stats_homebrew_dict = get_dict_from_csv_file(
        path_to_csv_file=combat_sim_cycle_combat_path_to_monsters_csv_file)

    """
    #TDOD: make these monsters dynamic 
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

    """
    current hp, or hp used by the system.
    i can't rename HP in the spreadsheet because legacy reasons / paranoia over legacy reasons.
    so instead i'll call hp used by the system... in order to remember the max hp when the monster heals.
    "current hp" :-)
    """
    for monster_dict in list_that_contains_dictionaries_that_are_monsters:
        monster_dict["current_hp"] = monster_dict["HP"]

    # adding the "life_status" key to the dictionary we just made above.
    for monster_dict in list_that_contains_dictionaries_that_are_monsters:
        # True = alive.
        # False = dead.
        #   computer has to eat less.
        monster_dict["life_status"] = True

    """
    originally i had it as "sorted_initiative_rolls_list[0]" which stored those
    sub lists. 
       another situation where it makes more sense to have this be made in java. 
           oh well :-/ 
    """
    user_initiative_roll_index = 0
    system_initiative_roll_index = 0

    # if you selected a NPC. not a player. this includes it a evil or a godo NPC mind you.
    selected_npc_bool = False
    """
    #starts at 0, ends at whatever the NPC, either evil or good, length's is.
    #this is for the child menu
    """
    selected_npc_index = 0

    """
    currently this means nothing. it just tells the user "no pc interactions yet sorry >_<"
    """
    selected_pc_bool = False

    """
    technically you could min-max these 2 and the 2 above to be 1 variable. 
    where -1 = False and anything else to be "yes and here's the index"
        but tbh this is more readable.
            if i gave a shit about performance this would be in java. 
            or C. if i want to hurt myself.
    """
    npc_interaction_menu_bool = False
    npc_interaction_menu_index = 0

    performing_attack_bool = False
    performing_damage_bool = False
    performing_heal_bool = False

    # Am i ever going to learn anything good out of my classes?
    damage_or_heal_integer_that_actually_a_string = ""

    def default_input_update_combat_sim_cycle_combat_interface():
        """
        basically feeds all the variables above into the update function.
        it's here so i don't have to add all the parameters myself when I call it.
        :return:
        """
        update_combat_sim_cycle_combat_interface(
            sorted_initiative_rolls_list=sorted_initiative_rolls_list,
            user_selected_initiative_roll=sorted_initiative_rolls_list[user_initiative_roll_index],
            system_selected_initiative_roll=sorted_initiative_rolls_list[system_initiative_roll_index],
            list_that_contains_dictionaries_that_are_monsters=list_that_contains_dictionaries_that_are_monsters,
            selected_npc_bool=selected_npc_bool,
            selected_npc_index=selected_npc_index,
            selected_pc_bool=selected_pc_bool,
            npc_interaction_menu_bool=npc_interaction_menu_bool,
            npc_interaction_menu_index=npc_interaction_menu_index,
            performing_attack_bool=performing_attack_bool,
            performing_damage_bool=performing_damage_bool,
            performing_heal_bool=performing_heal_bool,
            damage_or_heal_integer_that_actually_a_string=damage_or_heal_integer_that_actually_a_string
        )

    # do this once with the starter indexes.
    default_input_update_combat_sim_cycle_combat_interface()

    combat_cycle_keep_program_running_bool = True

    while combat_cycle_keep_program_running_bool:
        # these 2 lines are so duplicate inputs aren't recorded / holding down the key does nothing
        event = keyboard.read_event()
        if event.event_type == keyboard.KEY_DOWN:
            if keyboard.is_pressed("q"):
                if confirm_quit_via_keyboard():
                    combat_cycle_keep_program_running_bool = False

            # makes you understand who's turn it is.
            # in my games the enemies have their collective term.
            # i think DND 5e has it so that each enemy has their own consecutive turn
            #       if we cna be honest though. fuck that. too much to understand.
            # hypothetically though you could configure this program to make that please able.
            if keyboard.is_pressed("t"):
                if system_initiative_roll_index >= len(sorted_initiative_rolls_list) - 1:
                    system_initiative_roll_index = 0
                else:
                    system_initiative_roll_index += 1
                selected_pc_bool = False
                default_input_update_combat_sim_cycle_combat_interface()

            # the parent menu. where you select either PCs or NPCs to go into their children menus.
            if selected_npc_bool == False and npc_interaction_menu_bool == False \
                    and performing_attack_bool == False and performing_damage_bool == False and performing_heal_bool == False:

                # navigation. no actions here.
                if keyboard.is_pressed("up"):
                    if user_initiative_roll_index > 0:
                        user_initiative_roll_index += -1
                        selected_pc_bool = False
                        default_input_update_combat_sim_cycle_combat_interface()
                elif keyboard.is_pressed("down"):
                    if user_initiative_roll_index < len(sorted_initiative_rolls_list) - 1:
                        user_initiative_roll_index += 1
                        selected_pc_bool = False
                        default_input_update_combat_sim_cycle_combat_interface()

                # action(s)
                elif keyboard.is_pressed("right"):
                    name_of_selected_npc_or_pc = sorted_initiative_rolls_list[user_initiative_roll_index][0].lower()
                    if name_of_selected_npc_or_pc == "evil" or name_of_selected_npc_or_pc == "good":
                        selected_npc_bool = True
                    else:
                        selected_pc_bool = True
                    default_input_update_combat_sim_cycle_combat_interface()

            # the child menu where you select monsters to do interaction actions on them.
            elif selected_npc_bool == True and npc_interaction_menu_bool == False \
                    and performing_attack_bool == False and performing_damage_bool == False and performing_heal_bool == False:
                # basically the same functionality in the if statement
                # except instead of in the parent NPC or PC menu
                # you're in the NPC's child monster menu.
                # from which you can make them do an attack, take damage or heal damage.

                # navigation, no actions here.
                if keyboard.is_pressed("up"):
                    if selected_npc_index > 0:
                        selected_npc_index -= 1
                        default_input_update_combat_sim_cycle_combat_interface()
                elif keyboard.is_pressed("down"):
                    if selected_npc_index < len(list_that_contains_dictionaries_that_are_monsters) - 1:
                        selected_npc_index += 1
                        default_input_update_combat_sim_cycle_combat_interface()

                # actions
                elif keyboard.is_pressed("right"):
                    selected_npc_bool = False
                    npc_interaction_menu_bool = True
                    default_input_update_combat_sim_cycle_combat_interface()
                elif keyboard.is_pressed("left"):
                    # go back to parent menu.
                    selected_npc_bool = False
                    npc_interaction_menu_bool = False
                    selected_npc_index = 0
                    npc_interaction_menu_index = 0
                    default_input_update_combat_sim_cycle_combat_interface()

            # child-child menu. where you actually do the attack, take damage or heal actions.
            elif selected_npc_bool == False and npc_interaction_menu_bool == True \
                    and performing_attack_bool == False and performing_damage_bool == False and performing_heal_bool == False:

                # navigation
                if keyboard.is_pressed("up"):
                    if npc_interaction_menu_index > 0:
                        npc_interaction_menu_index -= 1
                        default_input_update_combat_sim_cycle_combat_interface()
                elif keyboard.is_pressed("down"):
                    if npc_interaction_menu_index < len(list_that_contains_dictionaries_that_are_monsters) - 1:
                        npc_interaction_menu_index += 1
                        default_input_update_combat_sim_cycle_combat_interface()

                # actions
                elif keyboard.is_pressed("left"):
                    selected_npc_bool = True
                    npc_interaction_menu_bool = False
                    # don't modify the selected_npc_index.
                    npc_interaction_menu_index = 0
                    default_input_update_combat_sim_cycle_combat_interface()
                elif keyboard.is_pressed("right"):
                    # monster does an attack
                    if npc_interaction_menu_index == 0:
                        print("this hasn't been implmeneted yet sorry :-(")
                        """
                        performing_attack_bool = True
                        default_input_update_combat_sim_cycle_combat_interface()
                        """
                    # monster takes damage
                    elif npc_interaction_menu_index == 1:
                        performing_damage_bool = True
                        default_input_update_combat_sim_cycle_combat_interface()
                    # monster heals health
                    elif npc_interaction_menu_index == 2:
                        performing_heal_bool = True
                        default_input_update_combat_sim_cycle_combat_interface()

            elif performing_damage_bool == True or performing_heal_bool == True:
                # navigation
                if keyboard.is_pressed("left"):
                    performing_attack_bool = False
                    performing_damage_bool = False
                    performing_heal_bool = False
                    default_input_update_combat_sim_cycle_combat_interface()

                if event.name == "backspace":
                    # in python-ese. this means "take away the last character from the left in a string"
                    # balls --> ball
                    damage_or_heal_integer_that_actually_a_string = damage_or_heal_integer_that_actually_a_string[:-1]
                    default_input_update_combat_sim_cycle_combat_interface()

                if event.name.isdigit():
                    damage_or_heal_integer_that_actually_a_string += event.name
                    default_input_update_combat_sim_cycle_combat_interface()

                if keyboard.is_pressed("right"):
                    """
                    i was debating on whether to make a limit so you couldn't over-heal or over-kill a monster
                    but since we're also displaying the max hp as well. i think it's more functional to have that be
                    under the user's decretion.
                    """
                    if performing_damage_bool == True:
                        """
                        list <-- directories <-- keys <-- values :-D
                        """
                        list_that_contains_dictionaries_that_are_monsters[selected_npc_index]["current_hp"] = \
                            (int(list_that_contains_dictionaries_that_are_monsters[selected_npc_index]["current_hp"])
                             -
                             int(damage_or_heal_integer_that_actually_a_string))

                        if list_that_contains_dictionaries_that_are_monsters[selected_npc_index]["current_hp"] <= 0:
                            list_that_contains_dictionaries_that_are_monsters[selected_npc_index]["life_status"] = False

                        performing_damage_bool = False
                        damage_or_heal_integer_that_actually_a_string = ""
                        default_input_update_combat_sim_cycle_combat_interface()

                    elif performing_heal_bool == True:
                        list_that_contains_dictionaries_that_are_monsters[selected_npc_index]["current_hp"] = \
                            (int(list_that_contains_dictionaries_that_are_monsters[selected_npc_index]["current_hp"])
                             +
                             int(damage_or_heal_integer_that_actually_a_string))

                        # I never resurrect monsters. But, hypothetically if you wanted to the option is there :-/.
                        if list_that_contains_dictionaries_that_are_monsters[selected_npc_index]["current_hp"] >= 0:
                            list_that_contains_dictionaries_that_are_monsters[selected_npc_index]["life_status"] = True

                        performing_heal_bool = False
                        damage_or_heal_integer_that_actually_a_string = ""
                        default_input_update_combat_sim_cycle_combat_interface()
