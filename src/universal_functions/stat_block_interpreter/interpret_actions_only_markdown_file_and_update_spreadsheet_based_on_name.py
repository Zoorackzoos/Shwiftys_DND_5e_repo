"""
work pipline is as follows
1. put in action information and the name of the monster i'm interpreting in
    "actions_only_input_file.md"
2. run this file
3. this file
    a. runs interpret_markdown_stat_block.py but doesn't create that file
    b. instead it takes the action key's information and pastes it into
       the all_monsters_homebrew spreadsheet

from there i can better pull the action information for the combat sim and can
make the backend and front end squeaky clean like a slip and slide.
"""
from copy import deepcopy

from universal_functions.display.print_2d_list_that_contains_dictionaries import \
    print_2d_list_that_contains_dictionaries
from universal_functions.display.print_dictionary_nicely import print_dictionary_nicely
from universal_functions.spreadsheet_stuff.dict_based_database_interpretors.get_dict_from_csv_file import \
    get_dict_from_csv_file
from universal_functions.spreadsheet_stuff.dict_based_database_interpretors.get_rows_from_dict_on_param_type_and_string import \
    get_rows_from_dict_on_param_type_and_string
from universal_functions.stat_block_interpreter.interpret_markdown_stat_block import \
    interpret_markdown_stat_block_into_python_file
from universal_functions.vars.spreadsheet_enums import SpreadsheetKeysEnums
from update_homebrew_monster_spreadsheet import update_homebrew_monster_spreadsheet


def interpret_actions_only_markdown_file_and_update_spreadsheet_based_on_name(
        tab_amount="\t",
        temp_monster_file_name="actions_only_input_file",
):
    print(tab_amount,"interpret_actions_only_markdown_file_and_update_spreadsheet_based_on_name")
    tab_amount += "\t"

    """
    get the actions key and it's value 
    this is 1/2 of the puzzle
    """
    smaller_input_monster_properties_dictionary = interpret_markdown_stat_block_into_python_file(
        path_to_markdown_file="temp_monster_directory/" + temp_monster_file_name + ".md",
        path_to_python_file="temp_monster_directory/" + temp_monster_file_name + ".py",
        generate_file=False,
        tab_amount=tab_amount
    )
    print(tab_amount,"smaller_input_monster_properties_dictionary")
    print_dictionary_nicely(
        dict_in_question=smaller_input_monster_properties_dictionary,
        tab_amount=tab_amount+"\t"
    )
    smaller_input_dictionary_actions_only = smaller_input_monster_properties_dictionary["actions"]
    smaller_input_name_only = smaller_input_monster_properties_dictionary["name"]

    """
    get the rest of teh spreadsheet values, form teh spreadsheet
    this is 1/2 of the puzzle
    if we don't do this then the spreadsheet updates without 99% of it's values
    """
    path_to_monsters_csv_file = "../../../sheets/monsters_all_stats_homebrew/monsters_all_stats_homebrew.csv"
    all_monsters_homebrew_dict = get_dict_from_csv_file(
        path_to_csv_file=path_to_monsters_csv_file,
        tab_amount=tab_amount
    )
    legacy_monster_values = get_rows_from_dict_on_param_type_and_string(
        dict_in_question=all_monsters_homebrew_dict,
        param_type=SpreadsheetKeysEnums.NAME.value,
        string=smaller_input_name_only,
        tab_amount=tab_amount
    )

    merged_monster_values = deepcopy(legacy_monster_values[0])
    merged_monster_values["actions"] = smaller_input_dictionary_actions_only

    update_homebrew_monster_spreadsheet(
        monster_dict=legacy_monster_values,
        tab_amount=tab_amount,
        path_to_monsters_csv_file=path_to_monsters_csv_file
    )


if __name__ == "__main__":
    interpret_actions_only_markdown_file_and_update_spreadsheet_based_on_name()