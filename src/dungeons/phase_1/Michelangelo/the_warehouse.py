from src.universal_functions.get_cr_from_precise_monster_search import get_cr_from_precise_monster_search
from src.universal_functions.get_encounter_difficulty.get_encounter_difficulty_from_cr_values import \
    get_encounter_difficulty_from_cr_values
from src.universal_functions.spreadsheet_stuff.spreadsheet_updaters.update_encounter_feedback_spreadsheet import \
    update_encounter_feedback_spreadsheet
from universal_functions.enums.spreadsheet_enums import SpreadsheetKeysEnums

player_levels = [6, 6, 6, 6]
path_to_monsters_csv_file = "../../../../sheets/monsters_all_stats_homebrew/monsters_all_stats_homebrew.csv"
path_to_encounter_feedback_csv_file = "../../../../sheets/encounter_feedback/encounter_feedback.csv"

def phase_1_michelangelo_the_warehouse_lvl_1(tab_amount="\t"):
    """
    each encounter in the warehouse i proportional to the levels
    so 1 encounter per level

    1 purple ninja
    2 orange ninjas
    2 white ninjas

    :param tab_amount:
    :return:
    """
    print(tab_amount,"phase_1_michelangelo_the_warehouse_lvl_1")
    tab_amount += "\t"

    purple_ninja_cr = get_cr_from_precise_monster_search(
        param_type=SpreadsheetKeysEnums.NAME.value,
        string="phase 1 purple foot clan ninja",
        path_to_monsters_csv_file=path_to_monsters_csv_file,
        tab_amount=tab_amount
    )
    orange_ninja_cr = get_cr_from_precise_monster_search(
        param_type=SpreadsheetKeysEnums.NAME.value,
        string="phase 1 orange foot clan ninja",
        path_to_monsters_csv_file=path_to_monsters_csv_file,
        tab_amount=tab_amount
    )
    white_ninja_cr = get_cr_from_precise_monster_search(
        param_type=SpreadsheetKeysEnums.NAME.value,
        string="phase 1 white foot clan ninja",
        path_to_monsters_csv_file=path_to_monsters_csv_file,
        tab_amount=tab_amount
    )

    phase_1_michelangelo_the_warehouse_lvl_1_cr_values = \
    [
        purple_ninja_cr,
        orange_ninja_cr, orange_ninja_cr,
        white_ninja_cr, white_ninja_cr
    ]

    phase_1_michelangelo_the_warehouse_lvl_1_difficulty_dict = get_encounter_difficulty_from_cr_values(
        player_levels=player_levels,
        monster_cr_values=phase_1_michelangelo_the_warehouse_lvl_1_cr_values,
        encounter_name="phase_1_michelangelo_the_warehouse_lvl_1_difficulty_dict",
        tab_amount=tab_amount
    )

    update_encounter_feedback_spreadsheet(
        encounter_dict=phase_1_michelangelo_the_warehouse_lvl_1_difficulty_dict,
        path_to_encounter_feedback_csv_file=path_to_encounter_feedback_csv_file,
        tab_amount=tab_amount
    )

def phase_1_michelangelo_the_warehouse_lvl_2(tab_amount="\t"):
    """
    6 mausers
    4 green ninjas

    :param tab_amount:
    :return:
    """
    print(tab_amount,"phase_1_michelangelo_the_warehouse_lvl_2")
    tab_amount += "\t"

    mauser_cr = get_cr_from_precise_monster_search(
        param_type=SpreadsheetKeysEnums.NAME.value,
        string="mauser",
        path_to_monsters_csv_file=path_to_monsters_csv_file,
        tab_amount=tab_amount
    )
    green_ninja_cr = get_cr_from_precise_monster_search(
        param_type=SpreadsheetKeysEnums.NAME.value,
        string="phase 1 green foot clan ninja",
        path_to_monsters_csv_file=path_to_monsters_csv_file,
        tab_amount=tab_amount
    )

    phase_1_michelangelo_the_warehouse_lvl_2_cr_values = \
    [
        mauser_cr, mauser_cr, mauser_cr,
        mauser_cr, mauser_cr, mauser_cr,
        green_ninja_cr, green_ninja_cr, green_ninja_cr, green_ninja_cr
    ]

    phase_1_michelangelo_the_warehouse_lvl_2_encounter_dict = get_encounter_difficulty_from_cr_values(
        player_levels=player_levels,
        monster_cr_values=phase_1_michelangelo_the_warehouse_lvl_2_cr_values,
        encounter_name="phase_1_michelangelo_the_warehouse_lvl_2_encounter_dict",
        tab_amount=tab_amount
    )

    update_encounter_feedback_spreadsheet(
        encounter_dict=phase_1_michelangelo_the_warehouse_lvl_2_encounter_dict,
        path_to_encounter_feedback_csv_file=path_to_encounter_feedback_csv_file,
        tab_amount=tab_amount
    )

def phase_1_michelangelo_the_warehouse_lvl_3(tab_amount="\t"):
    """
    4 orange ninjas
    1 yellow ninja
    then bebop and rocksteady. count them separately.

    :param tab_amount:
    :return:
    """
    print(tab_amount,"phase_1_michelangelo_the_warehouse_lvl_3")
    tab_amount += "\t"

    orange_ninja_cr = get_cr_from_precise_monster_search(
        param_type=SpreadsheetKeysEnums.NAME.value,
        string="phase 1 orange foot clan ninja",
        path_to_monsters_csv_file=path_to_monsters_csv_file,
        tab_amount=tab_amount
    )
    yellow_ninja_cr = get_cr_from_precise_monster_search(
        param_type=SpreadsheetKeysEnums.NAME.value,
        string="phase 1 yellow foot clan ninja",
        path_to_monsters_csv_file=path_to_monsters_csv_file,
        tab_amount=tab_amount
    )

    phase_1_michelangelo_the_warehouse_lvl_3_minions_cr_values = \
    [
        orange_ninja_cr, orange_ninja_cr, orange_ninja_cr, orange_ninja_cr,
        yellow_ninja_cr
    ]
    phase_1_michelangelo_the_warehouse_lvl_3_minions_encounter_dict = get_encounter_difficulty_from_cr_values(
        player_levels=player_levels,
        monster_cr_values=phase_1_michelangelo_the_warehouse_lvl_3_minions_cr_values,
        encounter_name="phase_1_michelangelo_the_warehouse_lvl_3_minions_encounter_dict",
        tab_amount=tab_amount
    )

    bebop_cr = get_cr_from_precise_monster_search(
        param_type=SpreadsheetKeysEnums.NAME.value,
        string="Bebop the Warthog",
        path_to_monsters_csv_file=path_to_monsters_csv_file,
        tab_amount=tab_amount
    )
    rocksteady_cr = get_cr_from_precise_monster_search(
        param_type=SpreadsheetKeysEnums.NAME.value,
        string="Rocksteady the Rhinovirus",
        path_to_monsters_csv_file=path_to_monsters_csv_file,
    )
    bebop_and_rocksteady_cr_values = \
    [
        bebop_cr, rocksteady_cr
    ]
    phase_1_michelangelo_the_warehouse_lvl_3_bebop_and_rocksteady_dict = get_encounter_difficulty_from_cr_values(
        player_levels=player_levels,
        monster_cr_values=bebop_and_rocksteady_cr_values,
        encounter_name="phase_1_michelangelo_the_warehouse_lvl_3_bebop_and_rocksteady_dict",
        tab_amount=tab_amount
    )

    update_encounter_feedback_spreadsheet(
        encounter_dict=phase_1_michelangelo_the_warehouse_lvl_3_minions_encounter_dict,
        path_to_encounter_feedback_csv_file=path_to_encounter_feedback_csv_file,
        tab_amount=tab_amount
    )
    update_encounter_feedback_spreadsheet(
        encounter_dict=phase_1_michelangelo_the_warehouse_lvl_3_bebop_and_rocksteady_dict,
        path_to_encounter_feedback_csv_file=path_to_encounter_feedback_csv_file,
        tab_amount=tab_amount
    )

if __name__ == '__main__':
    tab_amount =" \t"
    phase_1_michelangelo_the_warehouse_lvl_1(tab_amount=tab_amount)
    phase_1_michelangelo_the_warehouse_lvl_2(tab_amount=tab_amount)
    phase_1_michelangelo_the_warehouse_lvl_3(tab_amount=tab_amount)