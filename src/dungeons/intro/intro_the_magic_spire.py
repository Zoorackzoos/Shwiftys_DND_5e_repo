from src.universal_functions.display.print_encounter_difficulty_concisely import print_encounter_difficulty_concisely
from src.universal_functions.get_cr_from_precise_monster_search import get_cr_from_precise_monster_search
from src.universal_functions.get_encounter_difficulty.get_encounter_difficulty_from_cr_values import \
    get_encounter_difficulty_from_cr_values
from src.universal_functions.spreadsheet_stuff.spreadsheet_updaters.update_encounter_feedback_spreadsheet import \
    update_encounter_feedback_spreadsheet
from src.universal_functions.vars import spreadsheet_enums

intro_the_magic_spire_path_to_monsters_csv_file = "../../../sheets/monsters_all_stats_homebrew/monsters_all_stats_homebrew.csv"
intro_the_magic_spire_path_to_encounter_csv_file = "../../../sheets/encounter_feedback/encounter_feedback.csv"
player_levels = [5, 5, 5, 5]

def intro_the_magic_spire_lvl_1(tab_amount="\t"):
    print(tab_amount,"intro_the_magic_spire_lvl_1")

    #manes_smokoer_encounter
    """
    manes_cr = get_cr_from_precise_monster_search(
        param_type=spreadsheet_enums.SpreadsheetKeysEnums.NAME.value,
        string="Demon, Manes",
        path_to_csv_file=into_the_magic_spire_path_to_csv_file,
        tab_amount=tab_amount
    )
    """
    hag_green_cr = get_cr_from_precise_monster_search(
        param_type=spreadsheet_enums.SpreadsheetKeysEnums.NAME.value,
        string="Hag, Green",
        path_to_monsters_csv_file=intro_the_magic_spire_path_to_monsters_csv_file,
        tab_amount=tab_amount
    )
    hags_smoke_break_cr_values = \
        [
            hag_green_cr,hag_green_cr,hag_green_cr
        ]
    hags_smoke_break_encounter_difficulty = get_encounter_difficulty_from_cr_values(
        player_levels=player_levels,
        monster_cr_values=hags_smoke_break_cr_values,
        encounter_name="intro_the_magic_spire_hags_smoke_break",
        tab_amount=tab_amount
    )

    #mainframe room
    calculus_monster_limit_cr = get_cr_from_precise_monster_search(
        param_type=spreadsheet_enums.SpreadsheetKeysEnums.NAME.value,
        string="Calculus Monster, Limit",
        path_to_monsters_csv_file=intro_the_magic_spire_path_to_monsters_csv_file,
        tab_amount=tab_amount
    )
    calculus_monster_derivative_cr = get_cr_from_precise_monster_search(
        param_type=spreadsheet_enums.SpreadsheetKeysEnums.NAME.value,
        string="Calculus Monster, Derivative",
        path_to_monsters_csv_file=intro_the_magic_spire_path_to_monsters_csv_file,
        tab_amount=tab_amount
    )
    withering_gnoll_cr = get_cr_from_precise_monster_search(
        param_type=spreadsheet_enums.SpreadsheetKeysEnums.NAME.value,
        string="Gnoll Witherling",
        path_to_monsters_csv_file=intro_the_magic_spire_path_to_monsters_csv_file,
        tab_amount=tab_amount
    )
    mainframe_room_cr_values = \
        [
            calculus_monster_limit_cr, calculus_monster_limit_cr, calculus_monster_limit_cr,
            calculus_monster_limit_cr, calculus_monster_limit_cr, calculus_monster_limit_cr,
            calculus_monster_limit_cr, calculus_monster_limit_cr, calculus_monster_limit_cr,
            calculus_monster_derivative_cr,
            withering_gnoll_cr
        ]
    mainframe_room_encounter_difficulty = get_encounter_difficulty_from_cr_values(
        player_levels=player_levels,
        monster_cr_values=mainframe_room_cr_values,
        encounter_name="intro_the_magic_spire_mainframe_room",
        tab_amount=tab_amount
    )

    #office room
    """
    dreadlock_wight_cr = get_cr_from_precise_monster_search(
        param_type=spreadsheet_enums.SpreadsheetKeysEnums.NAME.value,
        string="Deathlock Wight",
        path_to_csv_file=into_the_magic_spire_path_to_csv_file,
        tab_amount=tab_amount
    )
    """
    embrald_gemstone_guy_cr = get_cr_from_precise_monster_search(
        param_type=spreadsheet_enums.SpreadsheetKeysEnums.NAME.value,
        string="Golem, Gemstone, Emerald",
        path_to_monsters_csv_file=intro_the_magic_spire_path_to_monsters_csv_file,
        tab_amount=tab_amount
    )
    office_room_cr_values = \
        [
            embrald_gemstone_guy_cr
        ]
    office_room_encounter_difficulty = get_encounter_difficulty_from_cr_values(
        player_levels=player_levels,
        monster_cr_values=office_room_cr_values,
        encounter_name="intro_the_magic_spire_office_room",
        tab_amount=tab_amount
    )

    print("\n",tab_amount,"intro_the_magic_spire_lvl_1_encounter_difficulty completed")
    intro_the_magic_spire_lvl_1_encounter_difficulty_list = \
    [
        hags_smoke_break_encounter_difficulty,
        mainframe_room_encounter_difficulty,
        office_room_encounter_difficulty
    ]
    for encounter in intro_the_magic_spire_lvl_1_encounter_difficulty_list:
        print(tab_amount+"\t\t",encounter["encounter_name"])
        print_encounter_difficulty_concisely(
            dict_in_question=encounter,
            tab_amount=tab_amount+"\t\t\t"
        )
        update_encounter_feedback_spreadsheet(
            encounter_dict=encounter,
            path_to_encounter_feedback_csv_file=intro_the_magic_spire_path_to_encounter_csv_file,
            tab_amount=tab_amount + "\t\t\t"
        )

def intro_the_magic_spire_lvl_2(tab_amount="\t"):
    #break room
    """
    troglidyte_cr = get_cr_from_precise_monster_search(
        param_type=spreadsheet_enums.SpreadsheetKeysEnums.NAME.value,
        string="Troglodyte",
        path_to_csv_file=into_the_magic_spire_path_to_csv_file,
        tab_amount=tab_amount
    )
    """
    troll_cr = get_cr_from_precise_monster_search(
        param_type=spreadsheet_enums.SpreadsheetKeysEnums.NAME.value,
        string="Troll",
        path_to_monsters_csv_file=intro_the_magic_spire_path_to_monsters_csv_file,
        tab_amount=tab_amount
    )
    derro_savant_cr = get_cr_from_precise_monster_search(
        param_type=spreadsheet_enums.SpreadsheetKeysEnums.NAME.value,
        string="Derro Savant",
        path_to_monsters_csv_file=intro_the_magic_spire_path_to_monsters_csv_file,
        tab_amount=tab_amount
    )
    break_room_cr_values = \
    [
        troll_cr,
        derro_savant_cr
    ]
    break_room_encounter_difficulty = get_encounter_difficulty_from_cr_values(
        player_levels=player_levels,
        monster_cr_values=break_room_cr_values,
        encounter_name="intro_the_magic_spire_break_room",
        tab_amount=tab_amount
    )

    #dining room
    animated_armour_cr = get_cr_from_precise_monster_search(
        param_type=spreadsheet_enums.SpreadsheetKeysEnums.NAME.value,
        string="Animated Object, Armor",
        path_to_monsters_csv_file=intro_the_magic_spire_path_to_monsters_csv_file,
        tab_amount=tab_amount
    )
    bulette_cr = get_cr_from_precise_monster_search(
        param_type=spreadsheet_enums.SpreadsheetKeysEnums.NAME.value,
        string="Bulette",
        path_to_monsters_csv_file=intro_the_magic_spire_path_to_monsters_csv_file,
        tab_amount=tab_amount
    )
    dining_room_monster_cr_values = \
    [
        animated_armour_cr,
        bulette_cr
    ]
    dining_room_encounter_difficulty = get_encounter_difficulty_from_cr_values(
        player_levels=player_levels,
        monster_cr_values=dining_room_monster_cr_values,
        encounter_name="intro_the_magic_spire_dining_room",
        tab_amount=tab_amount
    )

    #kitchen
    """
    lizard_cr = get_cr_from_precise_monster_search(
        param_type=spreadsheet_enums.SpreadsheetKeysEnums.NAME.value,
        string="Misc. Creature, Lizard",
        path_to_csv_file=into_the_magic_spire_path_to_csv_file,
        tab_amount=tab_amount
    )
    """
    giant_lizard_cr = get_cr_from_precise_monster_search(
        param_type=spreadsheet_enums.SpreadsheetKeysEnums.NAME.value,
        string="Misc. Creature, Giant Lizard",
        path_to_monsters_csv_file=intro_the_magic_spire_path_to_monsters_csv_file,
        tab_amount=tab_amount
    )
    lizard_monarch_cr = get_cr_from_precise_monster_search(
        param_type=spreadsheet_enums.SpreadsheetKeysEnums.NAME.value,
        string="Lizard King/Queen",
        path_to_monsters_csv_file=intro_the_magic_spire_path_to_monsters_csv_file,
        tab_amount=tab_amount
    )
    kitchen_cr_values = \
    [
        giant_lizard_cr, giant_lizard_cr,
        giant_lizard_cr, giant_lizard_cr,
        giant_lizard_cr, giant_lizard_cr,
        lizard_monarch_cr
    ]
    kitchen_encounter_difficulty = get_encounter_difficulty_from_cr_values(
        player_levels=player_levels,
        monster_cr_values=kitchen_cr_values,
        encounter_name="intro_the_magic_spire_kitchen",
        tab_amount=tab_amount
    )

    # flower conference room. official flower busniess
    tri_flower_frond_cr = get_cr_from_precise_monster_search(
        param_type=spreadsheet_enums.SpreadsheetKeysEnums.NAME.value,
        string="Tri-Flower Frond",
        path_to_monsters_csv_file=intro_the_magic_spire_path_to_monsters_csv_file,
        tab_amount=tab_amount
    )
    """
    corpse_flower_cr = get_cr_from_precise_monster_search(
        param_type=spreadsheet_enums.SpreadsheetKeysEnums.NAME.value,
        string="Corpse Flower",
        path_to_csv_file=into_the_magic_spire_path_to_csv_file,
        tab_amount=tab_amount
    )
    """
    flower_conference_room_cr_values = \
        [
            tri_flower_frond_cr, tri_flower_frond_cr,
            tri_flower_frond_cr, tri_flower_frond_cr
        ]
    flower_conference_room_encounter_difficulty = get_encounter_difficulty_from_cr_values(
        player_levels=player_levels,
        monster_cr_values=flower_conference_room_cr_values,
        encounter_name="intro_the_magic_spire_flower_conference_room",
        tab_amount=tab_amount
    )

    # bottom left conference room
    drop_bear_cr = get_cr_from_precise_monster_search(
        param_type=spreadsheet_enums.SpreadsheetKeysEnums.NAME.value,
        string="Drop Bear",
        path_to_monsters_csv_file=intro_the_magic_spire_path_to_monsters_csv_file,
        tab_amount=tab_amount
    )
    hunting_cactus_cr = get_cr_from_precise_monster_search(
        param_type=spreadsheet_enums.SpreadsheetKeysEnums.NAME.value,
        string="Cactus, Hunting",
        path_to_monsters_csv_file=intro_the_magic_spire_path_to_monsters_csv_file,
        tab_amount=tab_amount
    )
    bottom_left_conference_room_cr_values = \
        [
            hunting_cactus_cr, hunting_cactus_cr,
            drop_bear_cr, drop_bear_cr, drop_bear_cr
        ]
    bottom_left_encounter_difficulty = get_encounter_difficulty_from_cr_values(
        player_levels=player_levels,
        monster_cr_values=bottom_left_conference_room_cr_values,
        encounter_name="intro_the_magic_spire_bottom_left_conference_room",
        tab_amount=tab_amount
    )

    # teal key room
    spectator_cr = get_cr_from_precise_monster_search(
        param_type=spreadsheet_enums.SpreadsheetKeysEnums.NAME.value,
        string="Beholder, Spectator",
        path_to_monsters_csv_file=intro_the_magic_spire_path_to_monsters_csv_file,
        tab_amount=tab_amount
    )
    teal_key_cr_values = \
        [
            spectator_cr
        ]
    teal_key_room_encounter_difficulty = get_encounter_difficulty_from_cr_values(
        player_levels=player_levels,
        monster_cr_values=teal_key_cr_values,
        encounter_name="intro_the_magic_spire_teal_key",
        tab_amount=tab_amount
    )

    #movie room
    """
    wolf_cr = get_cr_from_precise_monster_search(
        param_type=spreadsheet_enums.SpreadsheetKeysEnums.NAME.value,
        string="Misc. Creature, Wolf",
        path_to_csv_file=into_the_magic_spire_path_to_csv_file,
        tab_amount=tab_amount
    )
    """
    dire_wolf_cr = get_cr_from_precise_monster_search(
        param_type=spreadsheet_enums.SpreadsheetKeysEnums.NAME.value,
        string="Misc. Creature, Dire Wolf",
        path_to_monsters_csv_file=intro_the_magic_spire_path_to_monsters_csv_file,
        tab_amount=tab_amount
    )
    movie_room_cr_values = \
    [
        dire_wolf_cr, dire_wolf_cr, dire_wolf_cr,
        dire_wolf_cr, dire_wolf_cr, dire_wolf_cr
    ]
    movie_room_encounter_difficulty = get_encounter_difficulty_from_cr_values(
        player_levels=player_levels,
        monster_cr_values=movie_room_cr_values,
        encounter_name="intro_the_magic_spire_movie_room",
        tab_amount=tab_amount
    )

    intro_the_magic_spire_lvl_2_encounters_list = \
    [
        break_room_encounter_difficulty,
        dining_room_encounter_difficulty,
        kitchen_encounter_difficulty,
        flower_conference_room_encounter_difficulty,
        bottom_left_encounter_difficulty,
        teal_key_room_encounter_difficulty,
        movie_room_encounter_difficulty,
    ]
    print("\n",tab_amount+"\tintro_the_magic_spire_lvl_2_encounters completed")
    for encounter in intro_the_magic_spire_lvl_2_encounters_list:
        print(tab_amount+"\t\t",encounter["encounter_name"])
        print_encounter_difficulty_concisely(
            dict_in_question=encounter,
            tab_amount=tab_amount+"\t\t\t"
        )
        update_encounter_feedback_spreadsheet(
            encounter_dict=encounter,
            path_to_encounter_feedback_csv_file=intro_the_magic_spire_path_to_encounter_csv_file,
            tab_amount=tab_amount + "\t\t\t"
        )

def intro_the_magic_spire_lvl_3(tab_amount="\t"):
    """
    it's just one big barracks.
    cockroach people live in there

    :param tab_amount:
    :return:
    """
    #barracks
    polar_bear_cr = get_cr_from_precise_monster_search(
        param_type=spreadsheet_enums.SpreadsheetKeysEnums.NAME.value,
        string="Misc. Creature, Polar Bear",
        path_to_monsters_csv_file=intro_the_magic_spire_path_to_monsters_csv_file,
        tab_amount=tab_amount
    )
    barracks_cr_value = \
    [
        polar_bear_cr, polar_bear_cr, polar_bear_cr
    ]
    barracks_encounter_difficulty = get_encounter_difficulty_from_cr_values(
        player_levels=player_levels,
        monster_cr_values=barracks_cr_value,
        encounter_name="intro_the_magic_spire_barracks",
        tab_amount=tab_amount
    )

    intro_the_magic_spire_lvl_3_encounters_list = \
        [
            barracks_encounter_difficulty
        ]
    print("\n", tab_amount + "\tintro_the_magic_spire_lvl_3_encounters completed")
    for encounter in intro_the_magic_spire_lvl_3_encounters_list:
        print(tab_amount + "\t\t", encounter["encounter_name"])
        print_encounter_difficulty_concisely(
            dict_in_question=encounter,
            tab_amount=tab_amount+"\t\t\t"
        )
        update_encounter_feedback_spreadsheet(
            encounter_dict=encounter,
            path_to_encounter_feedback_csv_file=intro_the_magic_spire_path_to_encounter_csv_file,
            tab_amount=tab_amount+"\t\t\t"
        )

if __name__ == "__main__":
    tab_amount = "\t"
    print("begin program")
    intro_the_magic_spire_lvl_1(tab_amount=tab_amount)
    intro_the_magic_spire_lvl_2(tab_amount=tab_amount)
    intro_the_magic_spire_lvl_3(tab_amount=tab_amount)
    print("end program")