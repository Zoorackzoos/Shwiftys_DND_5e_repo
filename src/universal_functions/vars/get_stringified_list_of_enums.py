def get_stringified_list_of_enums(list_of_enums, tab_amount="\t"):
    """
    this turns list_of_enums into 1 string so it looks better from user perspective

    :param list_of_enums:
    :param tab_amount:
    :return:
    """
    print(tab_amount,"get_stringified_list_of_enums")
    tab_amount += "\t"

    total_string = ""

    for i in range(len(list_of_enums)):
        if i == len(list_of_enums)-1:
            total_string += str(list_of_enums[i])
        else:
            total_string += str(list_of_enums[i]) + ", "

    return total_string