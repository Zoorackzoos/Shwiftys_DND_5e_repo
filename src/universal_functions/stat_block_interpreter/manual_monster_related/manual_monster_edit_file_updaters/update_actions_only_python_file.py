from copy import deepcopy

from universal_functions.enums import markdown_interpreter_related_enums
from universal_functions.enums.markdown_interpreter_related_enums import ActionKeyEnums
from universal_functions.enums.spreadsheet_enums import SpreadsheetKeysEnums
from universal_functions.spreadsheet_stuff.convert_csv_file_into_tsv_file import convert_csv_file_into_tsv_file
from universal_functions.spreadsheet_stuff.dict_based_database_interpretors.get_dict_from_csv_file import \
    get_dict_from_csv_file
from universal_functions.spreadsheet_stuff.dict_based_database_interpretors.get_rows_from_dict_on_param_type_and_string import \
    get_rows_from_dict_on_param_type_and_string
from universal_functions.stat_block_interpreter.manual_monster_related.manual_monster_edit_files.actions_only_input_file import \
    actions_only_input_file_monster_dict
from update_homebrew_monster_spreadsheet import update_homebrew_monster_spreadsheet


def update_actions_only_python_file(
        tab_amount="\t"
):
    path_to_monsters_csv_file = \
        "../../../../../sheets/monsters_all_stats_homebrew/monsters_all_stats_homebrew.csv"

    # the variable we're pulling from, is:
    #     actions_only_input_file_monster_dict

    all_monsters_homebrew_dict = get_dict_from_csv_file(
        path_to_csv_file=path_to_monsters_csv_file,
        tab_amount=tab_amount
    )
    legacy_monster_values = get_rows_from_dict_on_param_type_and_string(
        dict_in_question=all_monsters_homebrew_dict,
        param_type=SpreadsheetKeysEnums.NAME.value,
        string=actions_only_input_file_monster_dict[SpreadsheetKeysEnums.NAME.value],
        tab_amount=tab_amount
    )[0]

    merged_monster_values = deepcopy(legacy_monster_values)
    merged_monster_values[SpreadsheetKeysEnums.ACTIONS.value] = (
        actions_only_input_file_monster_dict)[SpreadsheetKeysEnums.ACTIONS.value]

    update_homebrew_monster_spreadsheet(
        monster_dict=merged_monster_values,
        path_to_monsters_csv_file=path_to_monsters_csv_file,
        tab_amount=tab_amount,
    )

    path_to_tsv_file = "../../../../../sheets/monsters_all_stats_homebrew/monsters_all_stats_homebrew.tsv"
    convert_csv_file_into_tsv_file(
        path_to_csv_file=path_to_monsters_csv_file,
        path_to_tsv_file=path_to_tsv_file,
    )

if __name__ == "__main__":
    update_actions_only_python_file()