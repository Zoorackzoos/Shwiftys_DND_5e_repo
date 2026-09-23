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
import copy

import keyboard

from A_GUI_programs.confirm_quit_via_keyboard import confirm_quit_via_keyboard
from A_GUI_programs.universal_terminal_clear import universal_terminal_clear
from universal_functions.display.print_2d_list_that_contains_dictionaries import \
    print_2d_list_that_contains_dictionaries
from universal_functions.spreadsheet_stuff.dict_based_database_interpretors.get_dict_from_csv_file import \
    get_dict_from_csv_file
from universal_functions.spreadsheet_stuff.dict_based_database_interpretors.get_rows_from_dict_on_param_type_and_string import \
    get_rows_from_dict_on_param_type_and_string
from universal_functions.enums import spreadsheet_enums

def get_list_with_quantity_of_monster_added_to_it(
        list_to_be_returned,
        monster_dict,
        quantity
):
    """
    if you have dictionaries of the same name then when you edit their
    * hp
    * life status
    they'll share a health pool. which is bad.

    :param list_to_be_returned:
    :param monster_dict:
    :param quantity:
    :return:
    """
    for i in range(quantity):
        list_to_be_returned.append( copy.deepcopy(monster_dict) )
    return list_to_be_returned

def get_monster_list_based_on_list_of_strings_and_ints(
        list_of_strings_and_ints,
        spreadsheet_monsters_dict_in_question,
        old_monster_list=[]
):
     """

     :param list_of_strings_and_ints:
        this contains a list of list which is the following:
            1. the string, ex: "Goblin"
                a. if this is not precise or you have a overloading row in the spreadsheet for some reason. then this won't work
            2. the quantity of the monster. ex: 2
                a. 2 goblins.
     :param old_monster_list:
        just in case the user (me) wants to add monsters to a existing list instead of just using this as a one stop shop.
     :return:
     """
     return_list = copy.deepcopy(old_monster_list)
     for sub_list in list_of_strings_and_ints:
         # reminder that this function ets multiple rows so we just get the 1st one.
         temp_monster_dict = get_rows_from_dict_on_param_type_and_string(
            spreadsheet_monsters_dict_in_question=spreadsheet_monsters_dict_in_question,
            param_type=spreadsheet_enums.SpreadsheetKeysEnums.NAME.value,
            string=sub_list[0],
            tab_amount="\t"
         )[0]
         return_list = get_list_with_quantity_of_monster_added_to_it(
             list_to_be_returned=return_list,
             monster_dict=temp_monster_dict,
             quantity=sub_list[1]
         )
     return return_list

def get_default_monster_list(
    spreadsheet_monsters_dict_in_question
):
    list_of_strings_and_ints = \
        [
            ["Goblin",1],
            ["Skeleton",1],
            ["Dragon, Chromatic, Black, Young",1]
        ]

    monster_list = get_monster_list_based_on_list_of_strings_and_ints(
        list_of_strings_and_ints=list_of_strings_and_ints,
        spreadsheet_monsters_dict_in_question=spreadsheet_monsters_dict_in_question
    )
    return monster_list


def get_one_giant_rat_and_three_small_rats(
    spreadsheet_monsters_dict_in_question
):
    string_and_quantity_parent_list = \
    [
        ["Misc. Creature, Rat",3],
        ["Misc. Creature, Giant Rat",1]
    ]
    monster_list = get_monster_list_based_on_list_of_strings_and_ints(
        list_of_strings_and_ints=string_and_quantity_parent_list,
        spreadsheet_monsters_dict_in_question=spreadsheet_monsters_dict_in_question
    )

    return monster_list

def get_one_ancient_gold_dragon(
    spreadsheet_monsters_dict_in_question
):
    strings_and_integer_list = \
    [
        ["Dragon, Metallic, Gold, Ancient",1]
    ]
    monster_list = get_monster_list_based_on_list_of_strings_and_ints(
        list_of_strings_and_ints=strings_and_integer_list,
        spreadsheet_monsters_dict_in_question=spreadsheet_monsters_dict_in_question,
    )
    return monster_list

def get_technodrome_2nd_floor_west_entrance(
    spreadsheet_monsters_dict_in_question
):
    list_of_strings_and_ints = \
        [
            ["Zombie, Cat",5],
            ["Goblin",5],
            ["Slime, Rad",4],
            ["Troll, Greatmaw",2],
            ["Devil, Chain",3],
            ["Misc. Creature, Giant Rat",3]
        ]
    monster_list = get_monster_list_based_on_list_of_strings_and_ints(
        list_of_strings_and_ints=list_of_strings_and_ints,
        spreadsheet_monsters_dict_in_question=spreadsheet_monsters_dict_in_question
    )
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
                    spreadsheet_monsters_dict_in_question=spreadsheet_monsters_dict_in_question
                )
            ],
            [
                "one_giant_rat_and_three_small_rats",
                get_one_giant_rat_and_three_small_rats(
                    spreadsheet_monsters_dict_in_question=spreadsheet_monsters_dict_in_question
                )
            ],
            [
                "one_ancient_gold_dragon",
                get_one_ancient_gold_dragon(
                    spreadsheet_monsters_dict_in_question=spreadsheet_monsters_dict_in_question
                )
            ],
            [
                "technodrome_2nd_floor_west_entrance",
                get_technodrome_2nd_floor_west_entrance(
                    spreadsheet_monsters_dict_in_question=spreadsheet_monsters_dict_in_question
                )
            ],
            # this is for a GUI element. it's less ad-hac code to deal with this here.
            # TODO: make create a list with it's import and export of the list thing.
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

if __name__ == "__main__":
    path_to_csv_file = "../../../sheets/monsters_all_stats_homebrew/monsters_all_stats_homebrew.csv"
    monsters_spreadsheet = get_dict_from_csv_file(
        path_to_csv_file=path_to_csv_file,
        tab_amount=""
    )
    monster_list = get_one_giant_rat_and_three_small_rats(
        spreadsheet_monsters_dict_in_question=monsters_spreadsheet
    )
    print_2d_list_that_contains_dictionaries(monster_list)