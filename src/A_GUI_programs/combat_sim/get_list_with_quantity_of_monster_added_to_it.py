import copy


def get_list_with_quantity_of_monster_added_to_it(
        list_to_be_returned,
        monster_dict,
        quantity
):
    """
    if you have dictionaries of the same name then when you edit their
    * hp
    * life status
    they'll share a health pool. which is bad.

    :param list_to_be_returned:
    :param monster_dict:
    :param quantity:
    :return:
    """
    for i in range(quantity):
        list_to_be_returned.append( copy.deepcopy(monster_dict) )
    return list_to_be_returned