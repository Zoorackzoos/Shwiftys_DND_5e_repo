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
from universal_functions.display.print_2d_list_that_contains_dictionaries import \
    print_2d_list_that_contains_dictionaries
from universal_functions.display.print_dictionary_nicely import print_dictionary_nicely
from universal_functions.stat_block_interpreter.interpret_markdown_stat_block import \
    interpret_markdown_stat_block_into_python_file
from update_homebrew_monster_spreadsheet import update_homebrew_monster_spreadsheet


def interpret_actions_only_markdown_file_and_update_spreadsheet_based_on_name(
        tab_amount="\t",
        temp_monster_file_name="actions_only_input_file",
):
    print(tab_amount,"interpret_actions_only_markdown_file_and_update_spreadsheet_based_on_name")
    tab_amount += "\t"
    raw_monster_properties_dictionary = interpret_markdown_stat_block_into_python_file(
        path_to_markdown_file="temp_monster_directory/" + temp_monster_file_name + ".md",
        path_to_python_file="temp_monster_directory/" + temp_monster_file_name + ".py",
        generate_file=False,
        tab_amount=tab_amount
    )
    print(tab_amount,"raw_monster_properties_dictionary")
    print_dictionary_nicely(
        dict_in_question=raw_monster_properties_dictionary,
        tab_amount=tab_amount+"\t"
    )
    raw_monster_properties_dictionary_actions_only = raw_monster_properties_dictionary["actions"]

    print(tab_amount,"these are the actions of the monster known as \""+raw_monster_properties_dictionary["name"]+"\"")
    print_2d_list_that_contains_dictionaries(
        list_dict_variable=raw_monster_properties_dictionary_actions_only,
        tab_amount=tab_amount+"\t"
    )

    tiny_monster_dict = \
        {
            "name" : raw_monster_properties_dictionary["name"],
            "actions" : raw_monster_properties_dictionary_actions_only
        }

    print(tab_amount,"tiny_monster_dict")
    print_dictionary_nicely(
        dict_in_question=tiny_monster_dict,
        tab_amount=tab_amount+"\t"
    )

    path_to_monsters_csv_file = "../../../sheets/monsters_all_stats_homebrew/monsters_all_stats_homebrew.csv"
    update_homebrew_monster_spreadsheet(
        monster_dict=tiny_monster_dict,
        tab_amount=tab_amount,
        path_to_monsters_csv_file=path_to_monsters_csv_file
    )


if __name__ == "__main__":
    interpret_actions_only_markdown_file_and_update_spreadsheet_based_on_name()