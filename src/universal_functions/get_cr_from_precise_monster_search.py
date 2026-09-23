from src.universal_functions.display.print_2d_list_that_contains_dictionaries import \
    print_2d_list_that_contains_dictionaries
from src.universal_functions.spreadsheet_stuff.dict_based_database_interpretors.get_dict_from_csv_file import get_dict_from_csv_file
from src.universal_functions.spreadsheet_stuff.dict_based_database_interpretors.get_rows_from_dict_on_param_type_and_string import \
    get_rows_from_dict_on_param_type_and_string

default_path_monsters_all_stats_dict = "../../../sheets/monsters_all_stats_homebrew.csv"

def get_cr_from_precise_monster_search(param_type,
                                       string,
                                       path_to_monsters_csv_file=default_path_monsters_all_stats_dict,
                                       tab_amount="\t"):
    """
    this gets the CR of the 1st creature it detects based on
    * param_type
    * string

    the reason path_to_csv_file is a parameter is because i don't know how to make the
    pathing in this function universally flexible, without a parameter. because the file
    you're calling it in will have a different directory, from file to file.

    :param param_type:
    :param string:
    :param path_to_monsters_csv_file:
    :param tab_amount:
    :return:
    """
    global monster_row
    print(tab_amount,"get_cr_from_precise_monster_search")
    tab_amount += "\t"
    if path_to_monsters_csv_file == default_path_monsters_all_stats_dict:
        monster_row = (
            get_rows_from_dict_on_param_type_and_string(
                spreadsheet_monsters_dict_in_question=get_dict_from_csv_file
                (
                    path_to_csv_file=path_to_monsters_csv_file,
                    tab_amount=tab_amount
                ),
                param_type=param_type,
                string=string,
                tab_amount=tab_amount
            )
        )[0]
    elif path_to_monsters_csv_file != default_path_monsters_all_stats_dict:
        try:
            monster_row = (
                get_rows_from_dict_on_param_type_and_string
                (
                    spreadsheet_monsters_dict_in_question=get_dict_from_csv_file
                    (
                        path_to_csv_file=path_to_monsters_csv_file,
                        tab_amount=tab_amount
                    ),
                    param_type=param_type,
                    string=string,
                    tab_amount=tab_amount
                )
            )[0]
        except:
            print(tab_amount,"ERROR: get_cr_from_precise_monster_search: had a issue trying to get your monster by the",param_type,string)
            print(tab_amount,"monster_row:")
            print(tab_amount +"\t", get_rows_from_dict_on_param_type_and_string(
                spreadsheet_monsters_dict_in_question=get_dict_from_csv_file(path_to_csv_file=path_to_monsters_csv_file, tab_amount=tab_amount),
                param_type=param_type,
                string=string,
                tab_amount=tab_amount + "\t"))
            exit("ERROR: get_cr_from_precise_monster_search: had a issue trying to get your monster")
    else:
        print("ERROR: get_cr_from_precise_monster_search: finding the .csv file is all fucked up.")
    print(tab_amount,"monster_row:")
    print_2d_list_that_contains_dictionaries(list_dict_variable=[monster_row],tab_amount=tab_amount)
    monster_cr = float(monster_row["CR"])
    print(tab_amount,"monster_cr :",monster_cr)
    return monster_cr