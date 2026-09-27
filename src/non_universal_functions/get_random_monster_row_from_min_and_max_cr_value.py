import random

from src.universal_functions.display.print_2d_list_that_contains_dictionaries import \
    print_2d_list_that_contains_dictionaries
from src.universal_functions.display.print_dictionary_nicely import print_dictionary_nicely
from src.universal_functions.spreadsheet_stuff.dict_based_database_interpretors.get_dict_from_csv_file import \
    get_dict_from_csv_file
from src.universal_functions.spreadsheet_stuff.dict_based_database_interpretors.get_rows_from_dict_on_param_type_and_string import \
    get_rows_from_dict_on_param_type_and_string
from universal_functions.enums import spreadsheet_enums

path_to_monsters_csv_file = "../../sheets/monsters_all_stats_homebrew/monsters_all_stats_homebrew.csv"

def get_random_monster_row_from_min_and_max_cr_value(
        max_cr_value,
        min_cr_value,
        tab_amount="\t",
        spreadsheet_monsters_dict_in_question=get_dict_from_csv_file(path_to_csv_file=path_to_monsters_csv_file,
                                                                     tab_amount="")
):
    """
    will get a monster based off of a random value between the min and max values for the CR.

    so if i put in 0 - 1. the code will get a monster from either:
        * cr 1
        * cr 0
        * cr 0.125
        * cr 0.25
        * cr 0.50
    and so on for greater value denominations.

    :param spreadsheet_monsters_dict_in_question:
    :param max_cr_value:
    :param min_cr_value:
    :param tab_amount:
    :return:
    """
    print(tab_amount,"get_random_monster_row_from_min_and_max_cr_value")
    tab_amount += "\t"

    # get the random integer via the threshhold
    randomly_selected_cr_value_based_off_threshold = random.randint(min_cr_value, max_cr_value)

    monsters_of_cr_type = get_rows_from_dict_on_param_type_and_string(
        spreadsheet_monsters_dict_in_question=spreadsheet_monsters_dict_in_question,
        param_type=spreadsheet_enums.SpreadsheetKeysEnums.CR.value,
        string=str(randomly_selected_cr_value_based_off_threshold),
        tab_amount=tab_amount
    )

    random_index = random.randint(0, len(monsters_of_cr_type) - 1)

    return monsters_of_cr_type[random_index]

if __name__ == "__main__":
    tab_amount = "\t"

    random_monster_dict = get_random_monster_row_from_min_and_max_cr_value(
        max_cr_value=spreadsheet_enums.CRTypeEnums.ONE.value,
        min_cr_value=spreadsheet_enums.CRTypeEnums.ZERO_NO_CHALLENGE.value,
        tab_amount=tab_amount
    )

    print("random_monster_dict:")
    print(tab_amount,random_monster_dict)
    print("random_monster_dict's name:")
    print(tab_amount,random_monster_dict[spreadsheet_enums.SpreadsheetKeysEnums.NAME.value])
    print("random_monster_dict's cr:")
    print(tab_amount, random_monster_dict[spreadsheet_enums.SpreadsheetKeysEnums.CR.value])
    print("random_monster_dict's URL:")
    print(tab_amount, random_monster_dict[spreadsheet_enums.SpreadsheetKeysEnums.URL.value])