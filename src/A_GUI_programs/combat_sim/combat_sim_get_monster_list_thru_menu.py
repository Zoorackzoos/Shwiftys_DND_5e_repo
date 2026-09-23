"""
    this is where the monster list selections screen is.
    it contains
        * list of monsters the user can select from
        * GUI for monster list selection screen
    it returns
        * the monster list selected
    in teh future, you'll be able to
        * make your own monster list and have it exported as a JSON file or something.
            * that means yit imports the file as well, so make a directory search system.
"""

import keyboard

from A_GUI_programs.combat_sim.combat_sim_user_creates_own_monster_list import combat_sim_user_creates_own_monster_list
from A_GUI_programs.combat_sim.helper_functions.build_monster_lists_from_folder import build_monster_lists_from_folder
from A_GUI_programs.confirm_quit_via_keyboard import confirm_quit_via_keyboard
from A_GUI_programs.universal_terminal_clear import universal_terminal_clear


def update_monster_list_selection_screen_GUI(
    list_of_monster_lists,
    monster_selection_screen_parent_index,
    monster_selection_are_you_sure_menu_trigger_bool
):
    """
    later on you could add a child menu index system and have it so if someone
    right arrows on a monster it could expand to show you all of it's properties within reason
        that's feature creep though. i'm not doing it.

    :param list_of_monster_lists:
    :param monster_selection_screen_parent_index:
    :param monster_selection_are_you_sure_menu_trigger_bool:
    :return:
    """
    universal_terminal_clear()

    tab_amount = "\t"

    starter_context_string = """update_monster_list_selection_screen_GUI
    You must select a list of monsters for your party to fight.
    If you want to make your own you can do it here in the menu
    Or you can create one in the code. I don't mind :-).
    Or select one i've made below.
    The "→" character marks the monster list or menu option you have selected.
    If you click a monster list I already made,
        it will show you the monsters in that list.
        and then it will prompt you if you're sure you want to select it.
    If you click on the "create a monster list" option it will move you to teh create a monster GUI.
        I will have more info there.
    """
    print(starter_context_string)

    sub_list_loop_index = 0

    for sub_list in list_of_monster_lists:
        if monster_selection_are_you_sure_menu_trigger_bool:
            if sub_list_loop_index == monster_selection_screen_parent_index:
                print(tab_amount, "→ ", sub_list[0])
                print(tab_amount + "\t→ ", "are you sure you want to select this monster list?")
                for monster_dict in sub_list[1]:
                    print(tab_amount+"\t  ",monster_dict["Name"])
            else:
                print(tab_amount, "  ", sub_list[0])
            sub_list_loop_index +=1
        else:
            if sub_list_loop_index == monster_selection_screen_parent_index:
                print(tab_amount, "→ ", sub_list[0])
            else:
                print(tab_amount, "  ", sub_list[0])
            sub_list_loop_index +=1

def combat_sim_get_monster_list_thru_menu(
    spreadsheet_monsters_dict_in_question
):
    """
    1. you have pre-determined monster lists to select from
    2. you can make your own as well by looking them up in the "monsters_all_stats_homebrew_dict"
        BUT ONLY BY NAME!!!!
        a. i have a feeling this will make performance issues because the spreadsheet has
         greater than 100 entries

    GUI look like this
    ```
    You must select a list of monster.
    If you want to make your own you can do it here in the menu
    Or you can create one in the code. I don't mind :-).
    Or select one i've made below.
    The "→" character marks the monster list or menu option you have selected.
    If you click a monster list I already made,
        it will show you the monsters in that list.
        and then it will prompt you if you're sure you want to select it.
    If you click on the "create a monster list" option it will move you to teh create a monster GUI.
        I will have more info there.

        → default_monster_list
          one_giant_rat_and_three_small_rats
          one_anchient_gold_dragon
          !!!!! create a monster list !!!!!
    ```

    :monsters_all_stats_homebrew_dict:
        big ahh dictionary. you can use the function
        "get_rows_from_dict_on_param_type_and_string" to parse it
    :return:
    """


    path_to_monster_list_of_dicts_folder = \
        "monster_list_of_dicts_folder"

    """
    list that contains lists.
        sub_list[0] <-- name of the sub list
        sub_list[1] <-- list that contains dictionaries of the monsters
    """
    list_of_monster_lists = build_monster_lists_from_folder(
        folder_path=path_to_monster_list_of_dicts_folder,
        spreadsheet_monsters_dict_in_question=spreadsheet_monsters_dict_in_question
    )

    # still append special GUI-only entry manually, since it's not a real file-backed list
    list_of_monster_lists.append(
        [
            "!!!!! create a monster list !!!!!",
            "ERROR: list_of_monster_lists: tried calling create a monster list string"
        ]
    )

    # to keep player cursor in correct position
    monster_selection_screen_parent_index = 0

    monster_selection_are_you_sure_menu_trigger_bool = False

    def default_update_monster_list_selection_screen_GUI():
        update_monster_list_selection_screen_GUI(
            list_of_monster_lists=list_of_monster_lists,
            monster_selection_screen_parent_index=monster_selection_screen_parent_index,
            monster_selection_are_you_sure_menu_trigger_bool=monster_selection_are_you_sure_menu_trigger_bool
        )

    # return value :-3
    return_value_monster_list = None

    default_update_monster_list_selection_screen_GUI()

    create_your_own_monster_list_bool = False

    # the "are you sure" bool in teh GUI logic.
    monster_list_selection_screen_keep_going_bool = True

    while monster_list_selection_screen_keep_going_bool:
        event = keyboard.read_event()
        if event.event_type == keyboard.KEY_DOWN:

            if event.name == "q":
                if confirm_quit_via_keyboard():
                    print("quiting...")
                    exit(0)
                else:
                    default_update_monster_list_selection_screen_GUI()

            if monster_selection_are_you_sure_menu_trigger_bool == False:
                #navigation
                if event.name == "up":
                    if monster_selection_are_you_sure_menu_trigger_bool == False:
                        if monster_selection_screen_parent_index <= 0:
                            pass
                        else:
                            monster_selection_screen_parent_index -= 1
                    default_update_monster_list_selection_screen_GUI()

                if event.name == "down":
                    if monster_selection_are_you_sure_menu_trigger_bool == False:
                        if monster_selection_screen_parent_index >= len(list_of_monster_lists)-1:
                            pass
                        else:
                            monster_selection_screen_parent_index += 1
                    default_update_monster_list_selection_screen_GUI()

                if event.name == "left":
                    pass
                if event.name == "right":
                    # the last element in list_of_monster_lists
                    # is always the "create your own monster list" option
                    if monster_selection_screen_parent_index == len(list_of_monster_lists)-1:
                        create_your_own_monster_list_bool = True
                    else:
                        monster_selection_are_you_sure_menu_trigger_bool = True
                        default_update_monster_list_selection_screen_GUI()
            elif monster_selection_are_you_sure_menu_trigger_bool == True:
                if event.name == "left":
                    monster_selection_are_you_sure_menu_trigger_bool = False
                    create_your_own_monster_list_bool = False
                    default_update_monster_list_selection_screen_GUI()
                if event.name == "right":
                    monster_list_selection_screen_keep_going_bool = False
                    if create_your_own_monster_list_bool == True:
                        return_value_monster_list = combat_sim_user_creates_own_monster_list(
                            spreadsheet_monsters_dict_in_question=spreadsheet_monsters_dict_in_question
                        )
                    else:
                        return_value_monster_list = list_of_monster_lists[monster_selection_screen_parent_index]

    return return_value_monster_list[1]

if __name__ == "__main__":
    print("hello me, meet the real me.")

