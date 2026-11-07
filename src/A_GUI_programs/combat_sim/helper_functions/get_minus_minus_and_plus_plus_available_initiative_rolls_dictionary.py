import copy


def get_minus_minus_and_plus_plus_available_initiative_rolls_list(
    sorted_initiative_rolls_list,
    tab_amount="\t",
    show_prints=True
):
    """
    example string:
    [['player 4', 12.0], ['player 2', 11.75], ['player 1', 11.25], ['player 3', 9.0]]

    :param sorted_initiative_rolls_list:
    :param tab_amount:
    :param show_prints:
    :return:
    """
    if show_prints:
        print(tab_amount,"get_minus_minus_and_plus_plus_available_initiative_rolls_dictionary")
    tab_amount += "\t"

    plus_plus_minus_minus_initiative_rolls_list = copy.deepcopy(sorted_initiative_rolls_list)

    if show_prints:
        print(tab_amount,"plus_plus_minus_minus_initiative_rolls_list = ",plus_plus_minus_minus_initiative_rolls_list)

    for sub_list in plus_plus_minus_minus_initiative_rolls_list:
        if sub_list[1] is None:
            pass
        else:
            if str(sub_list[1])[-2:] == "75":
                sub_list[1] -= 0.75
                sub_list[1] = str(int(sub_list[1])) + "++"
            elif str(sub_list[1])[-2:] == "25":
                sub_list[1] -= 0.25
                sub_list[1] = str(int(sub_list[1])) + "--"
            else:
                sub_list[1] = str(int(sub_list[1]))

    return plus_plus_minus_minus_initiative_rolls_list