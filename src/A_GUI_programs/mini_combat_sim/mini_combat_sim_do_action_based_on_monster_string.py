import ast

import keyboard

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

    GUI_based_action_index = 0
    for action in actions_list:
        if GUI_based_action_index == action_index:
            print(tab_amount,"→ ",action)
            if selecting_action_bool == False:
                tab_amount += "\t"
                # TODO: refactor this.
                # if it's a martial attack
                if ((action[markdown_interpreter_related_enums.ActionKeyEnums.ATTACK_TYPE.value]
                    ==
                    markdown_interpreter_related_enums.AttackTypeEnums.MELEE_ATTACK.value)
                    or
                    (action[markdown_interpreter_related_enums.ActionKeyEnums.ATTACK_TYPE.value]
                     ==
                     markdown_interpreter_related_enums.AttackTypeEnums.RANGED_ATTACK.value)):

                    chance_to_hit = "unknown"
                    if markdown_interpreter_related_enums.ActionKeyEnums.HIT_MODIFIER.value in action:
                        # pass a simple string to int conversion, into a function. to get the chance to hit
                        chance_to_hit = get_chance_to_hit(
                            hit_modifier=int(action[markdown_interpreter_related_enums.ActionKeyEnums.HIT_MODIFIER.value]),
                            tab_amount=tab_amount
                        )

                    damage = "unknown"
                    if markdown_interpreter_related_enums.ActionKeyEnums.DAMAGE.value in action:
                        parsed_damage_dice_dict = get_parsed_dict_from_dice_string(
                            dice_string=action[
                                markdown_interpreter_related_enums.ActionKeyEnums.DAMAGE.value],
                        )
                        damage = get_damage(
                            damage_dice=parsed_damage_dice_dict,
                            tab_amount=tab_amount
                        )

                    print(tab_amount,"chance to hit =", chance_to_hit)
                    print(tab_amount,"damage =", damage)
                    print(tab_amount,"damage_type =",action[markdown_interpreter_related_enums.ActionKeyEnums.DAMAGE_TYPE.value])
                    print(tab_amount,"range =",action[markdown_interpreter_related_enums.ActionKeyEnums.RANGE.value])

                # if it's a saving throw attack
                elif (action[markdown_interpreter_related_enums.ActionKeyEnums.ATTACK_TYPE.value]
                    ==
                    markdown_interpreter_related_enums.AttackTypeEnums.SAVING_THROW.value):

                    print(tab_amount,"save_stat =",action[markdown_interpreter_related_enums.ActionKeyEnums.SAVE_STAT.value])
                    print(tab_amount,"save_dc =",action[markdown_interpreter_related_enums.ActionKeyEnums.SAVE_DC.value])
                    print(tab_amount,"damage =", get_damage
                            (
                                damage_dice=get_parsed_dict_from_dice_string
                                    (
                                        dice_string=action[markdown_interpreter_related_enums.ActionKeyEnums.DAMAGE.value]
                                    ),
                                tab_amount=tab_amount
                            )
                          )
                    print(tab_amount,"damage_type =",action[markdown_interpreter_related_enums.ActionKeyEnums.DAMAGE_TYPE.value])
                    print(tab_amount,"range =",action[markdown_interpreter_related_enums.ActionKeyEnums.RANGE.value])

                # if it's auto-hit
                elif (action[markdown_interpreter_related_enums.ActionKeyEnums.ATTACK_TYPE.value]
                    ==
                    markdown_interpreter_related_enums.AttackTypeEnums.AUTO_HIT.value):

                    print(tab_amount,"This is a auto-hit attack so it just hits it's target")
                    print(tab_amount,"damage =", get_damage
                            (
                                damage_dice=get_parsed_dict_from_dice_string
                                    (
                                    dice_string=action[markdown_interpreter_related_enums.ActionKeyEnums.DAMAGE.value]
                                    ),
                                tab_amount=tab_amount
                            )
                          )
                    print(tab_amount,"damage_type =",action[markdown_interpreter_related_enums.ActionKeyEnums.DAMAGE_TYPE.value])
                    print(tab_amount,"range =",action[markdown_interpreter_related_enums.ActionKeyEnums.RANGE.value])

                # if it's a utility / trait
                elif (action[markdown_interpreter_related_enums.ActionKeyEnums.ATTACK_TYPE.value]
                        ==
                        markdown_interpreter_related_enums.AttackTypeEnums.UTILITY.value):

                    print(tab_amount,"This is a utility, AKA aa trait. so there's no attack to execute.")

                else:
                    print(tab_amount,"The system cannot identify the attack_type this action has.")
        else:
            print(tab_amount,"  ",action)
        GUI_based_action_index += 1

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