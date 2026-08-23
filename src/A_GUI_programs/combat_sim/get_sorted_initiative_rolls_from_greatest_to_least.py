"""
i was losing my marbles over a sorting algorithm.
i did this in sophomore year of high school dawg i can't fumble this bad.
"""

def get_sorted_initiative_rolls_from_greatest_to_least(unsorted_initiative_rolls_list):
    """
    sorts the unsorted_initiative_rolls_list and returns the sorted initiative rolls.. list

    # example usage
    _
    _
    1 2 3 4 5 None
        nothing

    _
      _
    1 2 3 4 5 None
        swap 1 with 2
    2 1 3 4 5

    _
    _
    2 1 3 4 5 None
        nothing

    _
      _
    2 1 3 4 5 None
        nothing

    _
        _
    2 1 3 4 5 None
        swap 2 with 3
    3 1 2 4 5 None

    _
    _
    3 1 2 4 5 None
        nothing

    you get it?
        the syntax of this is challenging.
        recursion makes more sense because when
        you reset to [0][0] it' just easier to call the function again

        i've done this without recursion before. almost 10 years ago....
        

    :param unsorted_initiative_rolls_list:
    :return:
    """

    print("get_sorted_initiative_rolls_from_greatest_to_least")
    print("\tsorted them. look at it!")
    print_2d_list(list_in_question=sorted_initiative_rolls_list, tab_amount="\t\t")
    time.sleep(1)  # this "hey i did it :DDD" text will be pasted over by another function anyway.

    return sorted_initiative_rolls_list