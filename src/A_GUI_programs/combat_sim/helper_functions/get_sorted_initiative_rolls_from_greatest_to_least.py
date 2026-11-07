"""
i was losing my marbles over a sorting algorithm.
i did this in sophomore year of high school dawg i can't fumble this bad.
"""
import time
from copy import deepcopy

from coverage.data import sorted_lines

from A_GUI_programs.combat_sim.helper_functions.get_minus_minus_and_plus_plus_available_initiative_rolls_dictionary import \
    get_minus_minus_and_plus_plus_available_initiative_rolls_list
from universal_functions.display.print_2d_list import print_2d_list


def get_sorted_initiative_rolls_from_greatest_to_least(
        unsorted_initiative_rolls_list,
        tab_amount="\t",
        show_prints=True
):
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
        i kinda forgot how to :-/
            I've done this in java a million times. but making a java-like scanner
            is very difficult in python for some reason.
                the muscle memory is failing.

    :param show_prints:
    :param tab_amount:
    :param unsorted_initiative_rolls_list:
    :return:
    """
    if show_prints:
        print(tab_amount,"get_sorted_initiative_rolls_from_greatest_to_least")
    tab_amount += "\t"

    """
    # sort initiative roles based from first to last. 20 means first 1 means last.
    #   to do this i'm going to have 'the structure that contains this' to be:
    #   a list
    #   that contains lists 
    #       with the 1st value in the sub-list be the PC / NPC's name
    #       the 2nd will be their roll (integer)
    """
    sorted_initiative_rolls_list = deepcopy(unsorted_initiative_rolls_list)

    if show_prints:
        print(tab_amount,"sorted_initiative_rolls_list = ",sorted_initiative_rolls_list)

    decimalify_the_sorted_initiative_rolls_list_bool = False
    for sublist in sorted_initiative_rolls_list:
        # if we had a roll off...
        if sublist[1] is not None:
            if sublist[1][-2:] == "--" or sublist[1][-2:] == "++":
                #...rewrite the sorted_intiative_rolls_list to be decimals instead.
                decimalify_the_sorted_initiative_rolls_list_bool = True
                break

    if show_prints:
        print(tab_amount,"decimalify_the_sorted_initiative_rolls_list_bool = ",decimalify_the_sorted_initiative_rolls_list_bool)

    if decimalify_the_sorted_initiative_rolls_list_bool:
        decimalified_sorted_initiative_rolls_list = []
        for sublist in sorted_initiative_rolls_list:
            if sublist[1] is not None:
                if sublist[1][-2:] == "--":
                    decimalified_sorted_initiative_rolls_list.append([sublist[0], float(sublist[1][:-2]) + 0.25])
                elif sublist[1][-2:] == "++":
                    decimalified_sorted_initiative_rolls_list.append([sublist[0], float(sublist[1][:-2]) + 0.75])
                else:
                    decimalified_sorted_initiative_rolls_list.append([sublist[0],float(sublist[1])])
            else:
                # this is just None :-/
                decimalified_sorted_initiative_rolls_list.append([sublist[0], sublist[1]])
        sorted_initiative_rolls_list = deepcopy(decimalified_sorted_initiative_rolls_list)

    i = 0

    """
    completely geeked if i should have had a - 1 on this or not.
    """
    length_of_unsorted_initiative_rolls_list = len(unsorted_initiative_rolls_list)# - 1
    print(tab_amount,"unsorted_initiative_rolls_list =\n",tab_amount,unsorted_initiative_rolls_list)
    print(tab_amount,"length_of_unsorted_initiative_rolls_list =",length_of_unsorted_initiative_rolls_list)
    print()

    num_of_times_iterated = 0
    modified_list_bool = False

    print(tab_amount,"beginning loop")
    tab_amount += "\t"
    while i < length_of_unsorted_initiative_rolls_list:
        # after the greatest value is found, we don't want the slot 0 to be slot 1 again.
        j = i
        while j < length_of_unsorted_initiative_rolls_list:

            #debug / display
            print(tab_amount,num_of_times_iterated)
            print(tab_amount+"\tsorted_initiative_rolls_list[",i,"]",sorted_initiative_rolls_list[i])
            print(tab_amount+"\tsorted_initiative_rolls_list[",j,"]",sorted_initiative_rolls_list[j])

            if sorted_initiative_rolls_list[i][1] == None:
                print(tab_amount, "\t\t Popping / Removing")
                print(tab_amount, "\t\t sorted_initiative_rolls_list[",i,"]",sorted_initiative_rolls_list[i])
                sorted_initiative_rolls_list.pop(i)
                length_of_unsorted_initiative_rolls_list = len(unsorted_initiative_rolls_list) - 1
                print(tab_amount, "\t\t unsorted_initiative_rolls_list =\n\t\t", tab_amount, unsorted_initiative_rolls_list)
                print(tab_amount, "\t\t length_of_unsorted_initiative_rolls_list =",
                      length_of_unsorted_initiative_rolls_list)

                print(tab_amount + "\t\t modified_list_bool =", modified_list_bool)
                print(tab_amount + "\t\t i =",i)
                print(tab_amount + "\t\t j =",j)
                print(tab_amount + "\t\t -->", )
                modified_list_bool = True
                i = 0
                j = 0
                print(tab_amount + "\t\t modified_list_bool =", modified_list_bool)
                print(tab_amount + "\t\t i =", i)
                print(tab_amount + "\t\t j =", j)

            if sorted_initiative_rolls_list[j][1] == None:
                print(tab_amount, "\t\t Popping / Removing")
                print(tab_amount, "\t\t sorted_initiative_rolls_list[",j,"]",sorted_initiative_rolls_list[j])
                sorted_initiative_rolls_list.pop(j)
                length_of_unsorted_initiative_rolls_list = len(unsorted_initiative_rolls_list) - 1
                print(tab_amount, "\t\t unsorted_initiative_rolls_list =\n\t\t", tab_amount, unsorted_initiative_rolls_list)
                print(tab_amount, "\t\t length_of_unsorted_initiative_rolls_list =",
                      length_of_unsorted_initiative_rolls_list)

                print(tab_amount + "\t\t modified_list_bool =", modified_list_bool)
                print(tab_amount + "\t\t i =", i)
                print(tab_amount + "\t\t j =", j)
                print(tab_amount + "\t\t -->", )
                modified_list_bool = True
                i = 0
                j = 0
                print(tab_amount + "\t\t modified_list_bool =", modified_list_bool)
                print(tab_amount + "\t\t i =", i)
                print(tab_amount + "\t\t j =", j)

            if int(sorted_initiative_rolls_list[i][1]) < int(sorted_initiative_rolls_list[j][1]):
                print(tab_amount + "\t\t Moving")
                print(tab_amount + "\t\t sorted_initiative_rolls_list[", i, "] = ",sorted_initiative_rolls_list[i])
                print(tab_amount + "\t\t sorted_initiative_rolls_list[", j, "] = ",sorted_initiative_rolls_list[j])
                print(tab_amount + "\t\t sorted_initiative_rolls_list[", i, "][1] = ", sorted_initiative_rolls_list[i][1])
                print(tab_amount + "\t\t sorted_initiative_rolls_list[", j, "][1] = ", sorted_initiative_rolls_list[j][1])
                print(tab_amount + "\t\t",sorted_initiative_rolls_list[i][1], "<",sorted_initiative_rolls_list[j][1])
                temp_i = sorted_initiative_rolls_list[i]
                temp_j = sorted_initiative_rolls_list[j]
                sorted_initiative_rolls_list[i] = temp_j
                sorted_initiative_rolls_list[j] = temp_i
                print(tab_amount + "\t\t sorted_initiative_rolls_list =\n\t\t\t",tab_amount,sorted_initiative_rolls_list)

                print(tab_amount + "\t\t modified_list_bool =",modified_list_bool)
                print(tab_amount + "\t\t i =", i)
                print(tab_amount + "\t\t j =", j)
                print(tab_amount + "\t\t -->",)
                modified_list_bool = True

                print(tab_amount + "\t\t modified_list_bool =",modified_list_bool)
                print(tab_amount + "\t\t i =", i)
                print(tab_amount + "\t\t j =", j)
            else:
                """
                #i had a issue where the numbers were compared as 
                if they were strings. this is here as a legacy debug feature
                """
                print(tab_amount + "\t\tnot moving")
                print(tab_amount + "\t\t sorted_initiative_rolls_list[", i, "] = ", sorted_initiative_rolls_list[i])
                print(tab_amount + "\t\t sorted_initiative_rolls_list[", j, "] = ", sorted_initiative_rolls_list[j])
                print(tab_amount + "\t\t sorted_initiative_rolls_list[", i, "][1] = ",sorted_initiative_rolls_list[i][1])
                print(tab_amount + "\t\t sorted_initiative_rolls_list[", j, "][1] = ",sorted_initiative_rolls_list[j][1])
                print(tab_amount + "\t\t", sorted_initiative_rolls_list[i][1], "<", sorted_initiative_rolls_list[j][1])
                print(tab_amount + "\t\t", "sorted_initiative_rolls_list[i][1] < sorted_initiative_rolls_list[j][1]")
                print(tab_amount + "\t\t", sorted_initiative_rolls_list[i][1] < sorted_initiative_rolls_list[j][1])

            # iteration
            print(tab_amount+"\tnum_of_times_iterated :",num_of_times_iterated," + 1 -->",(num_of_times_iterated + 1))
            num_of_times_iterated += 1
            print(tab_amount+"\tj :",j,"+ 1 -->",(j + 1))
            j += 1

            # debug stuff
            if num_of_times_iterated >= 100:
                print("ERROR: get_sorted_initiative_rolls_from_greatest_to_least: num_of_times_iterated exceeded 100")
                exit(1)
        # iteration
        print(tab_amount+"i:",i,"+ 1 -->",(i + 1))
        i += 1
        print(tab_amount+"j:",j,"--> 0")
        j = 0

        if modified_list_bool == True:
            print(tab_amount,"\t\tresetting  modified_list_bool from True to False")
            modified_list_bool = False

    print(tab_amount,"i < length_of_unsorted_initiative_rolls_list")
    print(tab_amount,i, "<", length_of_unsorted_initiative_rolls_list)
    print(tab_amount,i < length_of_unsorted_initiative_rolls_list)
    #print(sorted_initiative_rolls_list)

    print()

    print(tab_amount,"sorted them. look at it!")
    print_2d_list(list_in_question=sorted_initiative_rolls_list, tab_amount="\t\t")
    time.sleep(1)  # this "hey i did it :DDD" text will be pasted over by another function anyway.

    """
    for the 11++ and 11-- roll of rule we have. 
    i have to convert it from 11++ --> 11.75 --> 11++
    i do the 1st conversion in combat_sim_initaitve.
    this function call is the conversion back.
        kinda munted but it's either this or like a table lookup.
    """
    print(tab_amount,"sorted_initiative_rolls_list =")
    print(tab_amount+"\t",sorted_initiative_rolls_list)

    plus_plus_and_minus_minus_compliant_sorted_initiative_rolls_dictionary = (
        get_minus_minus_and_plus_plus_available_initiative_rolls_list(
            sorted_initiative_rolls_list=sorted_initiative_rolls_list,
            show_prints=show_prints,
            tab_amount=tab_amount
    ))

    print(tab_amount,"plus_plus_and_minus_minus_compliant_sorted_initiative_rolls_dictionary =")
    print(tab_amount+"\t",plus_plus_and_minus_minus_compliant_sorted_initiative_rolls_dictionary)

    return plus_plus_and_minus_minus_compliant_sorted_initiative_rolls_dictionary

if __name__ == "__main__":
    initiative_rolls_unsorted = \
    [
        ["player 1", "11--"],
        ["player 2", "11++"],
        ["player 3", "9"],
        ["player 4", "12"],
    ]
    get_sorted_initiative_rolls_from_greatest_to_least(
        unsorted_initiative_rolls_list=initiative_rolls_unsorted,
        show_prints=True,
        tab_amount=""
    )