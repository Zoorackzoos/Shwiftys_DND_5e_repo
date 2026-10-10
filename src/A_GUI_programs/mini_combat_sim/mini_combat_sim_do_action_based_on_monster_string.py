import ast

import keyboard

from A_GUI_programs.actions_list_print_handler import actions_list_print_handler
from A_GUI_programs.combat_sim.helper_functions.get_damage_and_get_chance_to_hit import get_damage, get_chance_to_hit
from A_GUI_programs.combat_sim.helper_functions.get_parsed_dict_from_dice_string import get_parsed_dict_from_dice_string
from A_GUI_programs.confirm_quit_via_keyboard import confirm_quit_via_keyboard
from A_GUI_programs.universal_terminal_clear import universal_terminal_clear
from universal_functions.enums import spreadsheet_enums, markdown_interpreter_related_enums
from universal_functions.get_cr_from_precise_monster_search import get_cr_from_precise_monster_search
from universal_functions.spreadsheet_stuff.dict_based_database_interpretors.get_dict_from_csv_file import \
    get_dict_from_csv_file
from universal_functions.spreadsheet_stuff.dict_based_database_interpretors.get_rows_from_dict_on_param_type_and_string import \
    get_rows_from_dict_on_param_type_and_string

path_to_monsters_csv_file = "../../../sheets/monsters_all_stats_homebrew/monsters_all_stats_homebrew.csv"

def update_mini_combat_sim_GUI(
        actions_list,
        action_index,
        selecting_action_bool,
        execute_selected_action,
        tab_amount = ""
):
    # intro text
    universal_terminal_clear()
    print(tab_amount, "mini_combat_sim_do_action_based_on_monster_string")
    tab_amount += "\t"
    print(tab_amount, "you execute actions here without having to put action data in \"get_damage_and_get_chance_to_hit.py\".")
    print(tab_amount, "\tusers aren't supposed to use this. only me >:-)")
    print(tab_amount, "this mini combat sim is limited to 1 monster. so if you want to run a new monster's actions.")
    print(tab_amount, "you need to load \"chosen_monster_string\" with a different monster string.\"")
    print()

    gui_based_action_index = 0
    actions_list_print_handler(
        attack_selection_menu_index=gui_based_action_index,
        action_index=action_index,
        actions_list=actions_list,
        executed_attack_bool=selecting_action_bool,
        tab_amount=tab_amount
    )


def mini_combat_sim_do_action_based_on_monster_string(
        monster_string,
        tab_amount=""
):
    """
    mini_combat_sim_do_action_based_on_monster_string:
        you execute actions here without having to put action data in
        "get_damage_and_get_chance_to_hit.py".
            users aren't supposed to use this. only me >:-)

        →   monster
            monster

    :param monster_string:
    :param tab_amount:
    :return:
    """

    # this returns multiple rows, get the 1st one.
    monster_dict = get_rows_from_dict_on_param_type_and_string(
        spreadsheet_monsters_dict_in_question=get_dict_from_csv_file(
            path_to_csv_file=path_to_monsters_csv_file,
            tab_amount=tab_amount
        ),
        param_type=spreadsheet_enums.SpreadsheetKeysEnums.NAME.value,
        string=monster_string,
        tab_amount=tab_amount
    )[0]

    action_list = ast.literal_eval(
        monster_dict[spreadsheet_enums.SpreadsheetKeysEnums.ACTIONS.value]
    )

    combat_cycle_keep_program_running_bool = True
    action_index = 0
    selecting_action_bool = True
    execute_selected_action = False

    def default_update_mini_combat_sim_GUI():
        update_mini_combat_sim_GUI(
            actions_list=action_list,
            action_index=action_index,
            tab_amount=tab_amount,
            selecting_action_bool=selecting_action_bool,
            execute_selected_action=execute_selected_action
        )

    default_update_mini_combat_sim_GUI()

    while combat_cycle_keep_program_running_bool:
        event = keyboard.read_event()
        if event.event_type == keyboard.KEY_DOWN:
            if event.name == "q":
                if confirm_quit_via_keyboard():
                    exit(0)

            if selecting_action_bool:
                if event.name == "up":
                    action_index -= 1
                    default_update_mini_combat_sim_GUI()
                elif event.name == "down":
                    action_index += 1
                    default_update_mini_combat_sim_GUI()
                elif event.name == "right":
                    selecting_action_bool = False
                    default_update_mini_combat_sim_GUI()
                elif event.name == "left":
                    pass

            else:
                if event.name == "left":
                    selecting_action_bool = True
                    default_update_mini_combat_sim_GUI()
                if event.name == "right":
                    print("shit")
                    default_update_mini_combat_sim_GUI()




if __name__ == "__main__":
    tab_amount = ""

    # put the strings of the monster in the combat encounter here.
    # they get fed into chosen_monster_string
    goblin_string = "Goblin"

    chosen_monster_string = goblin_string

    mini_combat_sim_do_action_based_on_monster_string(
        monster_string=chosen_monster_string,
        tab_amount=tab_amount
    )