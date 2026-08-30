import keyboard

from A_GUI_programs.confirm_quit_via_keyboard import confirm_quit_via_keyboard
from A_GUI_programs.universal_terminal_clear import universal_terminal_clear
from universal_functions.display.print_2d_list_that_contains_dictionaries import \
    print_2d_list_that_contains_dictionaries
from universal_functions.display.print_dictionary_nicely import print_dictionary_nicely
from universal_functions.spreadsheet_stuff.dict_based_database_interpretors.get_rows_from_dict_on_param_type_and_string import \
    get_rows_from_dict_on_param_type_and_string
from universal_functions.vars.enums import spreadsheet_enums

def get_default_monster_list(
    monsters_all_stats_homebrew_dict
):
    # in case it's not obvious this returns a list with dicts in it.
    # so that's why i have the [0] on the end
    goblin_dict = get_rows_from_dict_on_param_type_and_string(
        dict_in_question=monsters_all_stats_homebrew_dict,
        param_type=spreadsheet_enums.SpreadsheetKeysEnums.NAME.value,
        string="Goblin"
    )[0]
    skeleton_dict = get_rows_from_dict_on_param_type_and_string(
        dict_in_question=monsters_all_stats_homebrew_dict,
        param_type=spreadsheet_enums.SpreadsheetKeysEnums.NAME.value,
        string="Skeleton"
    )[0]
    black_dragon_dict = get_rows_from_dict_on_param_type_and_string(
        dict_in_question=monsters_all_stats_homebrew_dict,
        param_type=spreadsheet_enums.SpreadsheetKeysEnums.NAME.value,
        string="Dragon, Chromatic, Black, Young"
    )[0]
    monster_list = \
    [
        goblin_dict,
        skeleton_dict,
        black_dragon_dict
    ]
    return monster_list


def get_one_giant_rat_and_three_small_rats(
    monsters_all_stats_homebrew_dict
):
    rat_dict = get_rows_from_dict_on_param_type_and_string(
        dict_in_question=monsters_all_stats_homebrew_dict,
        param_type=spreadsheet_enums.SpreadsheetKeysEnums.NAME.value,
        string="Misc. Creature, Rat",
    )[0]
    giant_rat_dict = get_rows_from_dict_on_param_type_and_string(
        dict_in_question=monsters_all_stats_homebrew_dict,
        param_type=spreadsheet_enums.SpreadsheetKeysEnums.NAME.value,
        string="Misc. Creature, Giant Rat",
    )[0]

    monster_list = \
        [
            giant_rat_dict,
            rat_dict,
            rat_dict,
            rat_dict
        ]
    return monster_list

def get_one_ancient_gold_dragon(
    monsters_all_stats_homebrew_dict
):
    ancient_gold_dragon_dict = get_rows_from_dict_on_param_type_and_string(
        dict_in_question=monsters_all_stats_homebrew_dict,
        param_type=spreadsheet_enums.SpreadsheetKeysEnums.NAME.value,
        string="Dragon, Metallic, Gold, Ancient"
    )[0]
    monster_list = \
    [
       ancient_gold_dragon_dict
    ]
    return monster_list

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
    monsters_all_stats_homebrew_dict
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

    """
    list that contains lists.
        sub_list[0] <-- name of the sub list
        sub_list[1] <-- list that contains dictionaries of the monsters
    """
    list_of_monster_lists = \
        [
            [
                "default_monster_list",
                get_default_monster_list(
                    monsters_all_stats_homebrew_dict=monsters_all_stats_homebrew_dict
                )
            ],
            [
                "one_giant_rat_and_three_small_rats",
                get_one_giant_rat_and_three_small_rats(
                    monsters_all_stats_homebrew_dict=monsters_all_stats_homebrew_dict
                )
            ],
            [
                "one_ancient_gold_dragon",
                get_one_ancient_gold_dragon(
                    monsters_all_stats_homebrew_dict=monsters_all_stats_homebrew_dict
                )
            ],
            #this is for a GUI element. it's less ad-hac code to deal with this here.
            [
                "!!!!! create a monster list !!!!!",
                "ERROR: list_of_monster_lists: tried calling create a monster list string"
            ]
        ]

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
                    if monster_selection_screen_parent_index == len(list_of_monster_lists)-1:
                        pass
                    else:
                        monster_selection_are_you_sure_menu_trigger_bool = True
                        default_update_monster_list_selection_screen_GUI()
            elif monster_selection_are_you_sure_menu_trigger_bool == True:
                if event.name == "left":
                    monster_selection_are_you_sure_menu_trigger_bool = False
                    default_update_monster_list_selection_screen_GUI()
                if event.name == "right":
                    monster_list_selection_screen_keep_going_bool = False
                    return_value_monster_list = list_of_monster_lists[monster_selection_screen_parent_index]

    print_2d_list_that_contains_dictionaries(
        list_dict_variable=return_value_monster_list[1]
    )
    return return_value_monster_list[1]