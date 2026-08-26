from src.universal_functions.get_cr_from_precise_monster_search import get_cr_from_precise_monster_search
from src.universal_functions.get_encounter_difficulty.get_encounter_difficulty_from_cr_values import \
    get_encounter_difficulty_from_cr_values
from src.universal_functions.spreadsheet_stuff.spreadsheet_updaters.update_encounter_feedback_spreadsheet import \
    update_encounter_feedback_spreadsheet
from universal_functions.vars.enums.spreadsheet_enums import SpreadsheetKeysEnums

player_levels = [6, 6, 6, 6]
path_to_monsters_csv_file = "../../../../sheets/monsters_all_stats_homebrew/monsters_all_stats_homebrew.csv"
encounter_feedback_csv_file = "../../../../sheets/encounter_feedback/encounter_feedback.csv"

def phase_1_michelangelo_the_dmv_lvl_1(tab_amount="\t"):
    """
    i hate abbreviations. so instead of hthq it's instead the DMV.
    i am not putting the words ht stands for in my repo dammit

    :param tab_amount:
    :return:
    """
    print(tab_amount,"phase_1_michelangelo_the_dmv_lvl_1")
    tab_amount += "\t"

    """
    the office
    6 purple ninjas
    1 pink ninja
    """
    purple_ninja_cr = get_cr_from_precise_monster_search(
        param_type=SpreadsheetKeysEnums.NAME.value,
        string="phase 1 purple foot clan ninja",
        path_to_monsters_csv_file=path_to_monsters_csv_file,
        tab_amount=tab_amount
    )
    pink_ninja_cr = get_cr_from_precise_monster_search(
        param_type=SpreadsheetKeysEnums.NAME.value,
        string="phase 1 pink foot clan ninja",
        path_to_monsters_csv_file=path_to_monsters_csv_file,
        tab_amount=tab_amount
    )
    phase_1_michelangelo_the_dmv_lvl_1_the_office_cr_values = \
    [
        purple_ninja_cr, purple_ninja_cr, purple_ninja_cr,
        purple_ninja_cr, purple_ninja_cr, purple_ninja_cr,
        pink_ninja_cr
    ]
    phase_1_michelangelo_the_dmv_lvl_1_intial_encounter_dict = get_encounter_difficulty_from_cr_values(
        monster_cr_values=phase_1_michelangelo_the_dmv_lvl_1_the_office_cr_values,
        player_levels=player_levels,
        encounter_name="phase_1_michelangelo_the_dmv_lvl_1_intial_encounter_dict",
        tab_amount=tab_amount
    )

    """
    the elevator, tokka and rahzar
    1 tokka 
    1 rahzar
    """
    tokka_cr = get_cr_from_precise_monster_search(
        param_type=SpreadsheetKeysEnums.NAME.value,
        string="Tokka the evil blue turtle",
        path_to_monsters_csv_file=path_to_monsters_csv_file,
        tab_amount=tab_amount
    )
    rahzar_cr = get_cr_from_precise_monster_search(
        param_type=SpreadsheetKeysEnums.NAME.value,
        string="Rahzar the evil puppy monster",
        path_to_monsters_csv_file=path_to_monsters_csv_file,
        tab_amount=tab_amount
    )
    phase_1_michelangelo_the_dmv_lvl_1_elevator_tokka_and_rahzar_cr_values = \
    [
        tokka_cr, rahzar_cr
    ]
    phase_1_michelangelo_the_dmv_lvl_1_elevator_tokka_and_rahzar_encounter_dict = get_encounter_difficulty_from_cr_values(
        player_levels=player_levels,
        monster_cr_values=phase_1_michelangelo_the_dmv_lvl_1_elevator_tokka_and_rahzar_cr_values,
        encounter_name="phase_1_michelangelo_the_dmv_lvl_1_elevator_tokka_and_rahzar_encounter_dict",
        tab_amount=tab_amount
    )

    encounter_dict_list = \
    [
        phase_1_michelangelo_the_dmv_lvl_1_intial_encounter_dict,
        phase_1_michelangelo_the_dmv_lvl_1_elevator_tokka_and_rahzar_encounter_dict
    ]

    #update_encounter_feedback_spreadsheet loop
    for encounter_dict in encounter_dict_list:
        update_encounter_feedback_spreadsheet(
            encounter_dict=encounter_dict,
            path_to_encounter_feedback_csv_file=encounter_feedback_csv_file,
            tab_amount=tab_amount
        )

def phase_1_michelangelo_the_dmv_lvl_2(tab_amount="\t"):
    """

    :param tab_amount:
    :return:
    """
    print(tab_amount,"phase_1_michelangelo_the_dmv_lvl_2")
    tab_amount += "\t"

    """
    the airlock
    3 purple ninjas
    1 blue ninja
    """
    purple_ninja_cr = get_cr_from_precise_monster_search(
        param_type=SpreadsheetKeysEnums.NAME.value,
        string="phase 1 purple foot clan ninja",
        path_to_monsters_csv_file=path_to_monsters_csv_file,
        tab_amount=tab_amount
    )
    blue_ninja_cr = get_cr_from_precise_monster_search(
        param_type=SpreadsheetKeysEnums.NAME.value,
        string="phase 1 blue foot clan ninja",
        path_to_monsters_csv_file=path_to_monsters_csv_file,
        tab_amount=tab_amount
    )
    phase_1_michelangelo_the_dmv_lvl_2_airlock_cr_values = \
        [
            purple_ninja_cr, purple_ninja_cr, purple_ninja_cr,
            blue_ninja_cr
        ]
    phase_1_michelangelo_the_dmv_lvl_2_airlock_encounter_dict = get_encounter_difficulty_from_cr_values(
        player_levels=player_levels,
        monster_cr_values=phase_1_michelangelo_the_dmv_lvl_2_airlock_cr_values,
        encounter_name="phase_1_michelangelo_the_dmv_lvl_2_airlock_encounter_dict",
        tab_amount=tab_amount
    )

    """
    showers
    4 green ninjas
    """
    green_ninja_cr = get_cr_from_precise_monster_search(
        param_type=SpreadsheetKeysEnums.NAME.value,
        string="phase 1 green foot clan ninja",
        path_to_monsters_csv_file=path_to_monsters_csv_file,
        tab_amount=tab_amount
    )
    phase_1_michelangelo_the_dmv_lvl_2_showers_cr_values = \
        [
            green_ninja_cr, green_ninja_cr, green_ninja_cr, green_ninja_cr,
        ]
    phase_1_michelangelo_the_dmv_lvl_2_showers_difficulty_dict = get_encounter_difficulty_from_cr_values(
        player_levels=player_levels,
        monster_cr_values=phase_1_michelangelo_the_dmv_lvl_2_showers_cr_values,
        encounter_name="phase_1_michelangelo_the_dmv_lvl_2_showers_difficulty_dict",
        tab_amount=tab_amount
    )

    """
    cells
    2 purple ninjas
    1 yellow ninja
    """
    yellow_ninja_cr = get_cr_from_precise_monster_search(
        param_type=SpreadsheetKeysEnums.NAME.value,
        string="phase 1 yellow foot clan ninja",
        path_to_monsters_csv_file=path_to_monsters_csv_file,
        tab_amount=tab_amount
    )
    phase_1_michelangelo_the_dmv_lvl_2_cells_cr_values = \
        [
            purple_ninja_cr, purple_ninja_cr,
            yellow_ninja_cr
        ]
    phase_1_michelangelo_the_dmv_lvl_2_cells_difficulty_dict = get_encounter_difficulty_from_cr_values(
        player_levels=player_levels,
        monster_cr_values=phase_1_michelangelo_the_dmv_lvl_2_cells_cr_values,
        encounter_name="phase_1_michelangelo_the_dmv_lvl_2_cells_difficulty_dict",
        tab_amount=tab_amount
    )

    """
    break room
    2 white ninjas
    2 blue ninjas
    """
    white_ninja_cr = get_cr_from_precise_monster_search(
        param_type=SpreadsheetKeysEnums.NAME.value,
        string="phase 1 white foot clan ninja",
        path_to_monsters_csv_file=path_to_monsters_csv_file,
        tab_amount=tab_amount
    )
    phase_1_michelangelo_the_dmv_lvl_2_break_room_cr_values = \
        [
            white_ninja_cr, white_ninja_cr,
            blue_ninja_cr, blue_ninja_cr
        ]
    phase_1_michelangelo_the_dmv_lvl_2_break_room_difficulty_dict = get_encounter_difficulty_from_cr_values(
        player_levels=player_levels,
        monster_cr_values=phase_1_michelangelo_the_dmv_lvl_2_break_room_cr_values,
        encounter_name="phase_1_michelangelo_the_dmv_lvl_2_break_room_difficulty_dict",
        tab_amount=tab_amount
    )

    """
    robotics
    3 evil ninja cyborgs
    4 purple ninjas
    """
    evil_cyborg_ninja = get_cr_from_precise_monster_search(
        param_type=SpreadsheetKeysEnums.NAME.value,
        string="evil foot clan ninja cyborg",
        path_to_monsters_csv_file=path_to_monsters_csv_file,
        tab_amount=tab_amount
    )
    phase_1_michelangelo_the_dmv_lvl_2_robotics_cr_values = \
        [
            evil_cyborg_ninja, evil_cyborg_ninja, evil_cyborg_ninja, evil_cyborg_ninja,
            purple_ninja_cr, purple_ninja_cr, purple_ninja_cr, purple_ninja_cr
        ]
    phase_1_michelangelo_the_dmv_lvl_2_robotics_difficulty_dict = get_encounter_difficulty_from_cr_values(
        player_levels=player_levels,
        monster_cr_values=phase_1_michelangelo_the_dmv_lvl_2_robotics_cr_values,
        encounter_name="phase_1_michelangelo_the_dmv_lvl_2_robotics_difficulty_dict",
        tab_amount=tab_amount
    )

    encounter_dict_list = \
    [
        phase_1_michelangelo_the_dmv_lvl_2_airlock_encounter_dict,
        phase_1_michelangelo_the_dmv_lvl_2_showers_difficulty_dict,
        phase_1_michelangelo_the_dmv_lvl_2_cells_difficulty_dict,
        phase_1_michelangelo_the_dmv_lvl_2_break_room_difficulty_dict,
        phase_1_michelangelo_the_dmv_lvl_2_robotics_difficulty_dict
    ]

    # update_encounter_feedback_spreadsheet loop
    for encounter_dict in encounter_dict_list:
        update_encounter_feedback_spreadsheet(
            encounter_dict=encounter_dict,
            path_to_encounter_feedback_csv_file=encounter_feedback_csv_file,
            tab_amount=tab_amount
        )

def phase_1_michelangelo_the_dmv_lvl_3(tab_amount="\t"):
    print(tab_amount,"phase_1_michelangelo_the_dmv_lvl_3")
    tab_amount += "\t"
    """
    lab
    5 roadkill rodneys
    """
    roadkill_rodney_cr = get_cr_from_precise_monster_search(
        param_type=SpreadsheetKeysEnums.NAME.value,
        string="Roadkill Rodney",
        path_to_monsters_csv_file=path_to_monsters_csv_file,
        tab_amount=tab_amount
    )
    phase_1_michelangelo_the_dmv_lvl_3_lab_cr_values = \
    [
        roadkill_rodney_cr, roadkill_rodney_cr
    ]
    phase_1_michelangelo_the_dmv_lvl_3_lab_encounter_dict = get_encounter_difficulty_from_cr_values(
        player_levels=player_levels,
        monster_cr_values=phase_1_michelangelo_the_dmv_lvl_3_lab_cr_values,
        encounter_name="phase_1_michelangelo_the_dmv_lvl_3_lab_encounter_dict",
        tab_amount=tab_amount
    )

    """
    gene banks
    2 yellow ninjas
    4 green ninjas
    """
    yellow_ninja_cr = get_cr_from_precise_monster_search(
        param_type=SpreadsheetKeysEnums.NAME.value,
        string="phase 1 yellow foot clan ninja",
        path_to_monsters_csv_file=path_to_monsters_csv_file,
        tab_amount=tab_amount
    )
    green_ninja_cr = get_cr_from_precise_monster_search(
        param_type=SpreadsheetKeysEnums.NAME.value,
        string="phase 1 green foot clan ninja",
        path_to_monsters_csv_file=path_to_monsters_csv_file,
    )
    phase_1_michelangelo_the_dmv_lvl_3_gene_banks_cr_values = \
        [
            yellow_ninja_cr,yellow_ninja_cr,
            green_ninja_cr, green_ninja_cr,
            green_ninja_cr,green_ninja_cr,
        ]
    phase_1_michelangelo_the_dmv_lvl_3_gene_banks_encounter_dict = get_encounter_difficulty_from_cr_values(
        player_levels=player_levels,
        monster_cr_values=phase_1_michelangelo_the_dmv_lvl_3_gene_banks_cr_values,
        encounter_name="phase_1_michelangelo_the_dmv_lvl_3_gene_banks_encounter_dict",
        tab_amount=tab_amount
    )

    """
    metalhead encounter
    1 metalhead
    """
    metalhead_cr = get_cr_from_precise_monster_search(
        param_type=SpreadsheetKeysEnums.NAME.value,
        string="Metalhead",
        path_to_monsters_csv_file=path_to_monsters_csv_file,
        tab_amount=tab_amount
    )
    phase_1_michelangelo_the_dmv_lvl_3_metalhead_cr_values = \
    [
        metalhead_cr
    ]
    phase_1_michelangelo_the_dmv_lvl_3_metalhead_encounter_dict = get_encounter_difficulty_from_cr_values(
        player_levels=player_levels,
        monster_cr_values=phase_1_michelangelo_the_dmv_lvl_3_metalhead_cr_values,
        encounter_name="phase_1_michelangelo_the_dmv_lvl_3_metalhead_encounter_dict",
        tab_amount=tab_amount
    )

    encounter_dict_list = \
    [
        phase_1_michelangelo_the_dmv_lvl_3_lab_encounter_dict,
        phase_1_michelangelo_the_dmv_lvl_3_gene_banks_encounter_dict,
        phase_1_michelangelo_the_dmv_lvl_3_metalhead_encounter_dict
    ]

    # update_encounter_feedback_spreadsheet loop
    for encounter_dict in encounter_dict_list:
        update_encounter_feedback_spreadsheet(
            encounter_dict=encounter_dict,
            path_to_encounter_feedback_csv_file=encounter_feedback_csv_file,
            tab_amount=tab_amount
        )

if __name__ == "__main__":
    tab_amount="\t"
    #phase_1_michelangelo_the_dmv_lvl_1(tab_amount=tab_amount)
    #phase_1_michelangelo_the_dmv_lvl_2(tab_amount=tab_amount)
    phase_1_michelangelo_the_dmv_lvl_3(tab_amount=tab_amount)