"""
i was losing my marbles over a sorting algorithm.
i did this in sophomore year of high school dawg i can't fumble this bad.
"""
import time
from copy import deepcopy

from universal_functions.display.print_2d_list import print_2d_list


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
        i kinda forgot how to :-/
            I've done this in java a million times. but making a java-like scanner
            is very difficult in python for some reason.
                the muslce memory is faililng.

    :param unsorted_initiative_rolls_list:
    :return:
    """
    print("get_sorted_initiative_rolls_from_greatest_to_least")
    tab_amount = "\t"
    sorted_initiative_rolls_list = deepcopy(unsorted_initiative_rolls_list)

    i = 0
    j = 0

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
                print(tab_amount, "\t\t unsorted_initiative_rolls_list =\n", tab_amount, unsorted_initiative_rolls_list)
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
                print(tab_amount, "\t\t unsorted_initiative_rolls_list =\n", tab_amount, unsorted_initiative_rolls_list)
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

            if sorted_initiative_rolls_list[i][1] < sorted_initiative_rolls_list[j][1]:
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

            # iteration
            print(tab_amount+"\tnum_of_times_iterated :",num_of_times_iterated," + 1 -->",(num_of_times_iterated + 1))
            num_of_times_iterated += 1
            print(tab_amount+"\tj :",j,"+ 1 -->",(j + 1))
            j += 1

            # debug stuff
            if num_of_times_iterated >= 100:
                print("shit")
                exit(999)
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

    return sorted_initiative_rolls_list