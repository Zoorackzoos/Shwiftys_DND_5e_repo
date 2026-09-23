from A_GUI_programs.combat_sim.get_monster_list_based_on_list_of_strings_and_ints import \
    get_monster_list_based_on_list_of_strings_and_ints


def get_one_ancient_gold_dragon(
    spreadsheet_monsters_dict_in_question
):
    strings_and_integer_list = \
    [
        ["Dragon, Metallic, Gold, Ancient",1]
    ]
    monster_list = get_monster_list_based_on_list_of_strings_and_ints(
        list_of_strings_and_ints=strings_and_integer_list,
        spreadsheet_monsters_dict_in_question=spreadsheet_monsters_dict_in_question,
    )
    return monster_list