from src.universal_functions.display.print_2d_list_that_contains_dictionaries import \
    print_2d_list_that_contains_dictionaries
from src.universal_functions.spreadsheet_stuff.dict_based_database_interpretors.get_dict_from_csv_file import get_dict_from_csv_file


def get_rows_from_dict_on_param_type_and_string(dict_in_question, param_type, string, tab_amount="\t"):
    """
    everything in the .tsv and .csv spreadsheet is a string. so there's no type errors when
    i compare the string variable, and the spreadsheet's cell values.
        This function has to be fed a dictionary. just a big ahh dictionary.
            the way you get that is from calling "get_dict_from_csv_file"
            function in the file beforehand

    

    :param dict_in_question:
    :param param_type:
    :param string:
    :param tab_amount:
    :return:
    """
    print(tab_amount, "get_rows_from_dict_on_param_type_and_string")
    tab_amount += "\t"

    return_rows = []

    #print(tab_amount,dict_in_question[0].keys())
    #print(tab_amount,dict_in_question[0].values())
    for i in range(len(dict_in_question)):
        if param_type in dict_in_question[i]:
            if string.lower() == dict_in_question[i][param_type].lower():
                return_rows.append(dict_in_question[i])

    """
    if this wasn't here, you would be returning a blank list anyway.
    That's bad!
    """
    if len(return_rows) == 0:
        """
        "204 when the page is present and the query got properly processed
        but produced no results AND THAT'S OK

        (e.g. searching users by date of birth and it just so happens that
        no user has this date of birth. That's not an error, an empty result
        is just one possible result -- and will just display an empty results
        table in the frontend)"
        https://stackoverflow.com/questions/5604816/whats-the-most-appropriate-http-status-code-for-an-item-not-found-error-page
        """
        exit(204)

    print(tab_amount, "the string \"", string, "\" showed up", len(return_rows), "times in the param_type", param_type)

    return return_rows

if __name__ == "__main__":
    tab_amount = "\t"
    path_to_csv_file = "../../../../sheets/monsters_all_stats_homebrew/monsters_all_stats_homebrew.csv"
    monsters_all_stats_homebrew_dict = get_dict_from_csv_file(path_to_csv_file=path_to_csv_file, tab_amount=tab_amount)
    rows_for_humanoid = get_rows_from_dict_on_param_type_and_string(dict_in_question=monsters_all_stats_homebrew_dict,
                                                                    param_type="Type",
                                                                    string="Humanoid",
                                                                    tab_amount=tab_amount)
    print_2d_list_that_contains_dictionaries(list_dict_variable=rows_for_humanoid,tab_amount=tab_amount)
    print(rows_for_humanoid[0]["CR"])