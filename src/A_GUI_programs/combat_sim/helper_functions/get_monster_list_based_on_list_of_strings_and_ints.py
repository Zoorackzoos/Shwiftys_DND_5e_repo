import copy

from A_GUI_programs.combat_sim.helper_functions.get_list_with_quantity_of_monster_added_to_it import \
    get_list_with_quantity_of_monster_added_to_it
from universal_functions.enums import spreadsheet_enums
from universal_functions.spreadsheet_stuff.dict_based_database_interpretors.get_rows_from_dict_on_param_type_and_string import \
    get_rows_from_dict_on_param_type_and_string


def get_monster_list_based_on_list_of_strings_and_ints(
        list_of_strings_and_ints,
        spreadsheet_monsters_dict_in_question,
        old_monster_list=None
):
    """

    :param spreadsheet_monsters_dict_in_question:
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
    if old_monster_list is None:
        old_monster_list = []
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