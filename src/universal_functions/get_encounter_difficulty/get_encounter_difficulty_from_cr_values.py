from src.universal_functions.get_encounter_difficulty.get_encounter_difficulty_from_xp_values import \
    get_encounter_difficulty_from_xp_values
from src.universal_functions.get_xp_from_single_enemy_CR import get_xp_from_single_enemy_cr


def get_encounter_difficulty_from_cr_values(player_levels,
                                            monster_cr_values,
                                            encounter_name="NOT_NAMED",
                                            tab_amount="\t"):
    """
    main end goal of this repo.
    The actual function takes in xp values, so this is a helper function that takes Cr values instead
    #TODO: make the encounter name parameter auto-fill with the variable that contains the result of this function. consult a clanker because that sounds impossible.

    :param player_levels: list of integers
    :param monster_cr_values: list of doubles
    :param encounter_name: string
    :param tab_amount: variations of "\t". like "\t\t" or "\t\t\t"
    :return: encounter_dict
    """
    print(tab_amount, "get_encounter_difficulty_from_cr_values")
    tab_amount += "\t"

    monster_xp_values = []

    for cr in monster_cr_values:
        monster_xp_values.append(
            get_xp_from_single_enemy_cr(cr=cr,tab_amount=tab_amount)
        )

    return get_encounter_difficulty_from_xp_values(
        player_levels=player_levels,
        monster_xp_values=monster_xp_values,
        encounter_name=encounter_name,
        tab_amount=tab_amount
    )