from src.dungeons.phase_1.Michelangelo.the_dmv import path_to_monsters_csv_file
from src.universal_functions.get_cr_from_precise_monster_search import get_cr_from_precise_monster_search
from src.universal_functions.get_encounter_difficulty.get_encounter_difficulty_from_cr_values import \
    get_encounter_difficulty_from_cr_values
from universal_functions.enums import spreadsheet_enums
from update_encounter_feedback_spreadsheet import update_encounter_feedback_spreadsheet

path_to_monsters_csv_file = \
    "../../../../sheets/monsters_all_stats_homebrew/monsters_all_stats_homebrew.csv"
path_to_encounter_feedback_csv_file = \
    "../../../../sheets/encounter_feedback/encounter_feedback.csv"

player_levels = \
[
    8,8,8,8
]

def phase_1_the_hero_lvl_1(tab_amount="\t"):
    """
    this starts at the ... elevator whatever

    :param tab_amount:
    :return:
    """

    """
    the airlock 
    3 continuities
    """
    continuity_cr = get_cr_from_precise_monster_search(
        param_type=spreadsheet_enums.SpreadsheetKeysEnums.NAME.value,
        string="calculus monster, continuity",
        path_to_monsters_csv_file=path_to_monsters_csv_file,
        tab_amount=tab_amount
    )
    phase_1_the_hero_the_airlock_cr_values = \
    [
        continuity_cr, continuity_cr, continuity_cr
    ]
    phase_1_the_hero_lvl_1_the_airlock_encounter_dict = get_encounter_difficulty_from_cr_values(
        player_levels=player_levels,
        monster_cr_values=phase_1_the_hero_the_airlock_cr_values,
        encounter_name="phase_1_the_hero_lvl_1_the_airlock_encounter_dict",
        tab_amount=tab_amount
    )

    """
    the pot room
    4 polynomials
    """
    polynomial_cr = get_cr_from_precise_monster_search(
        param_type=spreadsheet_enums.SpreadsheetKeysEnums.NAME.value,
        string="calculus monster, polynomial",
        path_to_monsters_csv_file=path_to_monsters_csv_file,
        tab_amount=tab_amount
    )
    phase_1_the_hero_the_pot_room_cr_values = \
    [
        polynomial_cr, polynomial_cr,
        polynomial_cr, polynomial_cr
    ]
    phase_1_the_hero_lvl_1_the_pot_room_encounter_dict = get_encounter_difficulty_from_cr_values(
        player_levels=player_levels,
        monster_cr_values=phase_1_the_hero_the_pot_room_cr_values,
        encounter_name="phase_1_the_hero_lvl_1_the_pot_room_encounter_dict",
        tab_amount=tab_amount
    )

    """
    the false wall room
    1 dinosaur, spinosaurus, young
    4 dervatives
    """
    dinosaur_spinosaurus_young_cr = get_cr_from_precise_monster_search(
        param_type=spreadsheet_enums.SpreadsheetKeysEnums.NAME.value,
        string="Dinosaur, Spinosaurus, Young",
        path_to_monsters_csv_file=path_to_monsters_csv_file,
        tab_amount=tab_amount
    )
    derivative_cr = get_cr_from_precise_monster_search(
        param_type=spreadsheet_enums.SpreadsheetKeysEnums.NAME.value,
        string="Calculus Monster, Derivative",
        path_to_monsters_csv_file=path_to_monsters_csv_file,
        tab_amount=tab_amount
    )
    phase_1_the_hero_the_false_wall_room_cr_values = \
        [
            dinosaur_spinosaurus_young_cr,
            derivative_cr, derivative_cr,
            derivative_cr, derivative_cr
        ]
    phase_1_the_hero_lvl_1_the_false_wall_room_encounter_dict = get_encounter_difficulty_from_cr_values(
        player_levels=player_levels,
        monster_cr_values=phase_1_the_hero_the_false_wall_room_cr_values,
        encounter_name="phase_1_the_hero_lvl_1_the_false_wall_room_encounter_dict",
        tab_amount=tab_amount
    )

    """
    the boulder room
    3 continuities
    """
    phase_1_boulder_room_cr_values = \
    [
        continuity_cr,continuity_cr,continuity_cr
    ]
    phase_1_the_hero_lvl_1_the_boulder_room_encounter_dict = get_encounter_difficulty_from_cr_values(
        player_levels=player_levels,
        monster_cr_values=phase_1_boulder_room_cr_values,
        encounter_name="phase_1_the_hero_lvl_1_the_boulder_room_encounter_dict",
        tab_amount=tab_amount
    )

    """
    the treasure room
    1 mimic
    """
    mimic_cr = get_cr_from_precise_monster_search(
        param_type=spreadsheet_enums.SpreadsheetKeysEnums.NAME.value,
        string="Mimic",
        path_to_monsters_csv_file=path_to_monsters_csv_file,
        tab_amount=tab_amount
    )
    phase_1_the_hero_cr_values = \
    [
        mimic_cr
    ]
    phase_1_the_hero_lvl_1_the_treasure_room_encounter_dict = get_encounter_difficulty_from_cr_values(
        player_levels=player_levels,
        monster_cr_values=phase_1_the_hero_cr_values,
        encounter_name="phase_1_the_hero_lvl_1_the_treasure_room_encounter_dict",
        tab_amount=tab_amount
    )

    """
    the CRA room
    2 polynomials
    1 CRA
    """
    cra_cr = get_cr_from_precise_monster_search(
        param_type=spreadsheet_enums.SpreadsheetKeysEnums.NAME.value,
        string="calculus monster, CRA",
        path_to_monsters_csv_file=path_to_monsters_csv_file,
        tab_amount=tab_amount
    )
    phase_1_the_hero_cra_room_cr_values = \
        [
            polynomial_cr, polynomial_cr,
            cra_cr
        ]
    phase_1_the_hero_lvl_1_the_cra_room_encounter_dict = get_encounter_difficulty_from_cr_values(
        player_levels=player_levels,
        monster_cr_values=phase_1_the_hero_cra_room_cr_values,
        encounter_name="phase_1_the_hero_lvl_1_the_cra_room_encounter_dict",
        tab_amount=tab_amount
    )

    """
    the bowling alley
    1 bowling ball monster
    """
    bowling_ball_monster_cr = get_cr_from_precise_monster_search(
        param_type=spreadsheet_enums.SpreadsheetKeysEnums.NAME.value,
        string="Bowling ball monster",
        path_to_monsters_csv_file=path_to_monsters_csv_file,
        tab_amount=tab_amount
    )
    phase_1_the_hero_the_bowling_alley_cr_values = \
    [
        bowling_ball_monster_cr
    ]
    phase_1_the_hero_lvl_1_the_bowling_alley_encounter_dict = get_encounter_difficulty_from_cr_values(
        player_levels=player_levels,
        monster_cr_values=phase_1_the_hero_the_bowling_alley_cr_values,
        encounter_name="phase_1_the_hero_lvl_1_the_bowling_alley_encounter_dict",
        tab_amount=tab_amount
    )

    total_encounter_list = \
    [
        phase_1_the_hero_lvl_1_the_airlock_encounter_dict,
        phase_1_the_hero_lvl_1_the_pot_room_encounter_dict,
        phase_1_the_hero_lvl_1_the_false_wall_room_encounter_dict,
        phase_1_the_hero_lvl_1_the_boulder_room_encounter_dict,
        phase_1_the_hero_lvl_1_the_treasure_room_encounter_dict,
        phase_1_the_hero_lvl_1_the_cra_room_encounter_dict,
        phase_1_the_hero_lvl_1_the_bowling_alley_encounter_dict
    ]
    for encounter_dict in total_encounter_list:
        update_encounter_feedback_spreadsheet(
            encounter_dict=encounter_dict,
            path_to_encounter_feedback_csv_file=path_to_encounter_feedback_csv_file,
            tab_amount=tab_amount
        )

def phase_1_the_hero_lvl_2(tab_amount="\t"):
    """

    :param tab_amount:
    :return:
    """

    """
    the east intersection room
    2 product rules
    2 continuties
    1 derivative
    """
    product_rule_cr = get_cr_from_precise_monster_search(
        param_type=spreadsheet_enums.SpreadsheetKeysEnums.NAME.value,
        string="Calculus monster, product rule",
        path_to_monsters_csv_file=path_to_monsters_csv_file,
        tab_amount=tab_amount
    )
    continuity_cr = get_cr_from_precise_monster_search(
        param_type=spreadsheet_enums.SpreadsheetKeysEnums.NAME.value,
        string="calculus monster, continuity",
        path_to_monsters_csv_file=path_to_monsters_csv_file,
        tab_amount=tab_amount
    )
    derivative_cr = get_cr_from_precise_monster_search(
        param_type=spreadsheet_enums.SpreadsheetKeysEnums.NAME.value,
        string="calculus monster, derivative",
        path_to_monsters_csv_file=path_to_monsters_csv_file,
        tab_amount=tab_amount
    )
    phase_1_the_hero_the_east_intersection_room_cr_values = \
    [
        product_rule_cr, product_rule_cr,
        continuity_cr, continuity_cr,
        derivative_cr
    ]
    phase_1_the_hero_lvl_2_the_east_intersection_room_encounter_dict = get_encounter_difficulty_from_cr_values(
        player_levels=player_levels,
        monster_cr_values=phase_1_the_hero_the_east_intersection_room_cr_values,
        encounter_name="phase_1_the_hero_lvl_2_the_east_intersection_room_encounter_dict",
        tab_amount=tab_amount
    )

    """
    the tube room
    2 continuities
    1 product rule
    2 poisonous flesh turret
    """
    poisonous_flesh_turret_cr = get_cr_from_precise_monster_search(
        param_type=spreadsheet_enums.SpreadsheetKeysEnums.NAME.value,
        string="evil generator, poison flesh turret",
        path_to_monsters_csv_file=path_to_monsters_csv_file,
        tab_amount=tab_amount
    )
    phase_1_the_hero_the_tube_room_cr_values = \
    [
        continuity_cr, continuity_cr,
        product_rule_cr,
        poisonous_flesh_turret_cr, poisonous_flesh_turret_cr
    ]
    phase_1_the_hero_lvl_2_the_tube_room_encounter_dict = get_encounter_difficulty_from_cr_values(
        player_levels=player_levels,
        monster_cr_values=phase_1_the_hero_the_tube_room_cr_values,
        encounter_name="phase_1_the_hero_lvl_2_the_tube_room_encounter_dict",
        tab_amount=tab_amount
    )

    """
    the tiny center room
    2 poisonous flesh turret
    """
    the_hero_the_tiny_center_room_cr_values = \
    [
        poisonous_flesh_turret_cr,poisonous_flesh_turret_cr
    ]
    phase_1_the_hero_lvl_2_the_tiny_center_room_encounter_dict = get_encounter_difficulty_from_cr_values(
        player_levels=player_levels,
        monster_cr_values=the_hero_the_tiny_center_room_cr_values,
        encounter_name="phase_1_the_hero_lvl_2_the_tiny_center_room_encounter_dict",
        tab_amount=tab_amount
    )

    """
    the central treasure room
    2 poisonous flesh turret
    """
    the_hero_the_central_treasure_room_cr_values = \
        [
            poisonous_flesh_turret_cr,poisonous_flesh_turret_cr
        ]
    phase_1_the_hero_lvl_2_the_central_treasure_room_encounter_dict = get_encounter_difficulty_from_cr_values(
        player_levels=player_levels,
        monster_cr_values=the_hero_the_central_treasure_room_cr_values,
        encounter_name="phase_1_the_hero_lvl_2_the_central_treasure_room_encounter_dict",
        tab_amount=tab_amount
    )

    """
    the contained mid term room
    1 midterm
    """
    midterm_cr = get_cr_from_precise_monster_search(
        param_type=spreadsheet_enums.SpreadsheetKeysEnums.NAME.value,
        string="calculus monster, midterm",
        path_to_monsters_csv_file=path_to_monsters_csv_file,
        tab_amount=tab_amount
    )
    the_hero_the_contained_midterm_cr_values = \
        [
            midterm_cr
        ]
    phase_1_the_hero_lvl_2_the_contained_midterm_encounter_dict = get_encounter_difficulty_from_cr_values(
        player_levels=player_levels,
        monster_cr_values=the_hero_the_contained_midterm_cr_values,
        encounter_name="phase_1_the_hero_lvl_2_the_contained_midterm_encounter_dict",
        tab_amount=tab_amount
    )

    """
    the evil church
    4 limits
    1 quotient rule
    """
    limit_cr = get_cr_from_precise_monster_search(
        param_type=spreadsheet_enums.SpreadsheetKeysEnums.NAME.value,
        string="Calculus Monster, Limit",
        path_to_monsters_csv_file=path_to_monsters_csv_file,
        tab_amount=tab_amount
    )
    quotient_rule_cr = get_cr_from_precise_monster_search(
        param_type=spreadsheet_enums.SpreadsheetKeysEnums.NAME.value,
        string="calculus monster, quotient rule",
        path_to_monsters_csv_file=path_to_monsters_csv_file,
        tab_amount=tab_amount
    )
    the_hero_the_evil_church_cr_values = \
    [
        limit_cr,limit_cr,limit_cr,limit_cr,
        quotient_rule_cr
    ]
    phase_1_the_hero_lvl_2_the_evil_church_encounter_dict = get_encounter_difficulty_from_cr_values(
        player_levels=player_levels,
        monster_cr_values=the_hero_the_evil_church_cr_values,
        encounter_name="phase_1_the_hero_lvl_2_the_evil_church_encounter_dict",
        tab_amount=tab_amount
    )

    total_encounters_list = \
    [
        phase_1_the_hero_lvl_2_the_east_intersection_room_encounter_dict,
        phase_1_the_hero_lvl_2_the_tube_room_encounter_dict,
        phase_1_the_hero_lvl_2_the_tiny_center_room_encounter_dict,
        phase_1_the_hero_lvl_2_the_central_treasure_room_encounter_dict,
        phase_1_the_hero_lvl_2_the_contained_midterm_encounter_dict,
        phase_1_the_hero_lvl_2_the_evil_church_encounter_dict
    ]
    for encounter_dict in total_encounters_list:
        update_encounter_feedback_spreadsheet(
            encounter_dict=encounter_dict,
            path_to_encounter_feedback_csv_file=path_to_encounter_feedback_csv_file,
            tab_amount=tab_amount
        )

def phase_1_the_hero_lvl_3(tab_amount="\t"):
    """
    just one encounter. the inflamed CRA.

    :param tab_amount:
    :return:
    """

    """
    the inflamed CRA
    1 CRA
    """
    cra_cr = get_cr_from_precise_monster_search(
        param_type=spreadsheet_enums.SpreadsheetKeysEnums.NAME.value,
        string="calculus monster, CRA",
        path_to_monsters_csv_file=path_to_monsters_csv_file,
        tab_amount=tab_amount
    )
    phase_1_the_hero_lvl_3_the_inflamed_cra_cr_values = \
    [
        cra_cr
    ]
    phase_1_the_hero_lvl_3_the_inflamed_cra_encounter_dict = get_encounter_difficulty_from_cr_values(
        player_levels=player_levels,
        monster_cr_values=phase_1_the_hero_lvl_3_the_inflamed_cra_cr_values,
        encounter_name="phase_1_the_hero_lvl_3_the_inflamed_cra_encounter_dict",
        tab_amount=tab_amount
    )
    update_encounter_feedback_spreadsheet(
        encounter_dict=phase_1_the_hero_lvl_3_the_inflamed_cra_encounter_dict,
        path_to_encounter_feedback_csv_file=path_to_encounter_feedback_csv_file,
        tab_amount=tab_amount
    )

if __name__ == "__main__":
    tab_amount = "\t"
    phase_1_the_hero_lvl_1(tab_amount=tab_amount)
    phase_1_the_hero_lvl_2(tab_amount=tab_amount)
    phase_1_the_hero_lvl_3(tab_amount=tab_amount)
