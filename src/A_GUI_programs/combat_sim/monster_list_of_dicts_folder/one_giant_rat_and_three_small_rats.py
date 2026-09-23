from A_GUI_programs.combat_sim.get_monster_list_based_on_list_of_strings_and_ints import \
    get_monster_list_based_on_list_of_strings_and_ints


def get_one_giant_rat_and_three_small_rats(
    spreadsheet_monsters_dict_in_question
):
    string_and_quantity_parent_list = \
    [
        ["Misc. Creature, Rat",3],
        ["Misc. Creature, Giant Rat",1]
    ]
    monster_list = get_monster_list_based_on_list_of_strings_and_ints(
        list_of_strings_and_ints=string_and_quantity_parent_list,
        spreadsheet_monsters_dict_in_question=spreadsheet_monsters_dict_in_question
    )

    return monster_list