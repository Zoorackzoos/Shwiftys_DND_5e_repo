import random

from src.non_universal_functions.get_random_cr_from_list import get_random_cr_from_list
from src.universal_functions.display.print_2d_list_that_contains_dictionaries import \
    print_2d_list_that_contains_dictionaries
from src.universal_functions.display.print_dictionary_nicely import print_dictionary_nicely
from src.universal_functions.spreadsheet_stuff.dict_based_database_interpretors.get_dict_from_csv_file import \
    get_dict_from_csv_file
from src.universal_functions.spreadsheet_stuff.dict_based_database_interpretors.get_rows_from_dict_on_param_type_and_string import \
    get_rows_from_dict_on_param_type_and_string
from universal_functions.vars.enums import spreadsheet_enums

path_to_monsters_csv_file = "../../sheets/monsters_all_stats_homebrew/monsters_all_stats_homebrew.csv"

def get_random_monster_row_from_cr_lvl(cr_lvl, tab_amount="\t"):
    """

    :param cr_lvl:
    :param tab_amount:
    :return:
    """
    print(tab_amount,"get_random_monster_row_from_cr_lvl")
    tab_amount += "\t"

    monster_dict = get_dict_from_csv_file(
        path_to_csv_file=path_to_monsters_csv_file,
        tab_amount=tab_amount
    )

    list_of_monsters_with_that_cr_value = get_rows_from_dict_on_param_type_and_string(
        dict_in_question=monster_dict,
        param_type=spreadsheet_enums.SpreadsheetKeysEnums.CR.value,
        string=str(cr_lvl),
        tab_amount=tab_amount
    )

    print(tab_amount,"list_of_monsters_with_that_cr_value...")
    print_2d_list_that_contains_dictionaries(
        list_dict_variable=list_of_monsters_with_that_cr_value,
        tab_amount=tab_amount+"\t"
    )

    chosen_monster = random.choice(list_of_monsters_with_that_cr_value)

    print(tab_amount,"chosen_monster is....")
    print_dictionary_nicely(
        dict_in_question=chosen_monster,
        tab_amount=tab_amount+"\t"
    )

if __name__ == "__main__":
    tab_amount = "\t"

    #update the "lvl_integer" parameter each time they level up the staff of the spire
    random_cr_lvl = get_random_cr_from_list(
        lvl_integer=0,
        tab_amount=tab_amount
    )

    get_random_monster_row_from_cr_lvl(
        cr_lvl=random_cr_lvl,
        tab_amount=tab_amount
    )