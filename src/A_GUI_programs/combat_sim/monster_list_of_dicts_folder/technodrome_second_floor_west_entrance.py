from A_GUI_programs.combat_sim.helper_functions.get_monster_list_based_on_list_of_strings_and_ints import \
    get_monster_list_based_on_list_of_strings_and_ints


def get_monster_list(
    spreadsheet_monsters_dict_in_question
):
    list_of_strings_and_ints = \
        [
            ["Zombie, Cat",5],
            ["Goblin",5],
            ["Slime, Rad",4],
            ["Troll, Greatmaw",2],
            ["Devil, Chain",3],
            ["Misc. Creature, Giant Rat",3]
        ]
    monster_list = get_monster_list_based_on_list_of_strings_and_ints(
        list_of_strings_and_ints=list_of_strings_and_ints,
        spreadsheet_monsters_dict_in_question=spreadsheet_monsters_dict_in_question
    )
    return monster_list