import keyboard

from A_GUI_programs.combat_sim.combat_sim_cycle_combat import confirm_quit_via_keyboard
from A_GUI_programs.universal_terminal_clear import universal_terminal_clear

"""
i'm not so sure this is a good data structure for what is is,
considering the amount of times i have to convert this into a array like structure.
"""
initiative_rolls_dictionary = \
    {
        "Mikey": None,
        "Forest": None,
        "Thalis": None,
        "Micheal": None,
        "Evil": None,  # these are the monsters, AKA the bad guys.
        "Good": None  # these are DM controlled allies. They're not always there so this can be Null.
    }

def get_if_all_rolls_in_initiative_rolls_are_all_none(initiative_rolls_dictionary=initiative_rolls_dictionary):
    for i in list(initiative_rolls_dictionary.values()):
        if i != None:
            return False
    return True

def get_acceptable_initiative_roll_list():
    acceptable_user_input_list = []

    # "The absolute highest initiative roll you can mathematically achieve in D&D 5e is 111."
    # if you manage to get a number greater than 40 i'll eat my fingers
    largest_initiative_roll = 41

    for i in range(largest_initiative_roll):
        if i == 0:
            # do nothing lol
            pass
        else:
            acceptable_user_input_list.insert(0, str(i) + "--")
            acceptable_user_input_list.insert(0, str(i))
            acceptable_user_input_list.insert(0, str(i) + "++")

    """
    what is looks like:

    ['40++', '40', '40--', 
    '39++', '39', '39--', 
    '38++', '38', '38--', 
    '37++', '37', '37--', 
    '36++', '36', '36--',
    '35++', '35', '35--',
    '34++', '34', '34--',
    '33++', '33', '33--',
    '32++', '32', '32--',
    '31++', '31', '31--', 
    '30++', '30', '30--', 
    '29++', '29', '29--', 
    '28++', '28', '28--', '27++', '27', '27--', '26++', '26', '26--', '25++', '25', '25--', '24++', '24', '24--', '23++', '23', '23--', '22++', '22', '22--', '21++', '21', '21--', '20++', '20', '20--', '19++', '19', '19--', '18++', '18', '18--', '17++', '17', '17--', '16++', '16', '16--', '15++', '15', '15--', '14++', '14', '14--', '13++', '13', '13--', '12++', '12', '12--', '11++', '11', '11--', '10++', '10', '10--', '9++', '9', '9--', '8++', '8', '8--', '7++', '7', '7--', '6++', '6', '6--', '5++', '5', '5--', '4++', '4', '4--', '3++', '3', '3--', '2++', '2', '2--', '1++', '1', '1--']
    """

    return acceptable_user_input_list


def get_if_initiative_input_is_failed_input(user_input):
    """
    this is kinda fucky because we need to allow things like "10--" and "10++"
    so we can't just say if it's a integer let it pass.
    so the bastard thing i'm gonna do is make a list of acceptable answers.
    and if our user_input is not in the array, throw a hissy fit.

    false = acceptable input
    true = NOT acceptable input

    :param user_input:
    :return:
    """
    acceptable_user_input_list = get_acceptable_initiative_roll_list()
    if user_input in acceptable_user_input_list:
        return False
    else:
        return True

def get_if_selected_roll_taker_index_is_beyond_limits(selected_roll_taker_index,modifier):
    least_limit = 0
    greatest_limit = len(initiative_rolls_dictionary)
    modified_selected_roll_taker_index = selected_roll_taker_index + modifier
    return least_limit <= modified_selected_roll_taker_index < greatest_limit

def update_initiative_roles_screen_and_return_user_input(
        failed_initiative_input_bool,
        duplicate_initiative_input_bool,
        roll_off_respected_bool,
        selected_roll_taker_index=0
):
    universal_terminal_clear(tab_amount="")

    take_initiative_roles_intro_text = """take_initiative_roles
    we need to take initiative roles.
    the '→' character indicates which PC / NPC you have selected.
    use the UP and DOWN arrow keys to swap from PC / NPC.
    press RIGHT ARROW to register a integer in a initiative role.
        press it again when you're done putting the integer in to register it.
    press the ENTER key to finalize the initiative rolls.
        if a player is absent, or there's no good or bad NPCs
        controlled by the DM, leave that parameter blank
"""

    print(take_initiative_roles_intro_text)

    for key,value in initiative_rolls_dictionary.items():
        if key == list(initiative_rolls_dictionary.keys())[selected_roll_taker_index]:
            print("\t →", key, ": ",value)
        else:
            print("\t  ", key, ": ",value)

    if roll_off_respected_bool == True:
        print("you have a non- ++ or -- and a ++ or -- value of the same integer at the same time. this cannot be. one must be ++ and the other --. ")
    if duplicate_initiative_input_bool == True:
        print("your input was a duplicate of another, you must change one. if someone won the roll off make them X++, and the loser X--.")
    if failed_initiative_input_bool == True:
        print("your input wasn't in the acceptable_user_input_list. please try again.")

def get_if_initiative_input_is_duplicate_input(
        initiative_value,
        selected_dictionary_key,
        initiative_rolls_dictionary
):
    if initiative_value == initiative_rolls_dictionary[selected_dictionary_key]:
        return False
    for value in initiative_rolls_dictionary.values():
        if value == initiative_value:
            return True
    return False

def get_roll_off_respected_bool(initiative_value):
    """
    detect if there is a ++ or a -- and if the incoming value, initiative_value is a normal integer

    1. scan the present values for ++es or --es that match the initiative value
        a. if there's both a ++ and a -- for the initiative value then just return value because both the values are taken.
        b. if there's only one, then see if the initiative value is a normie. if it's a normie return false
        c. if there's only one, then see if the initiative matches the persisting ++ or --.

    :param initiative_value:
    :return: roll_off_respected_bool, true = bad, false = good
    """
    plus_plus_present = False
    minus_minus_present = False

    #check if pre-existing ++ and -- pair
    for value in initiative_rolls_dictionary.values():
        if value is not None and len(value) ==2:
            if list(value)[1] == "+":
                plus_plus_present = True
                for value_two in initiative_rolls_dictionary.values():
                    if value_two is not None:
                        if list(value_two)[1] == "-" and list(value_two)[0] == list(value)[0]:
                            minus_minus_present = True
            if list(value)[1] == "-":
                minus_minus_present = True
                for value_two in initiative_rolls_dictionary.values():
                    if value_two is not None:
                        if list(value_two)[1] == "+" and list(value_two)[0] == list(value)[0]:
                            plus_plus_present = True

    #if there are no ++ or --es then just return false
    if plus_plus_present == False and minus_minus_present == False:
        return False

    if len(list(initiative_value)) == 1:
        if plus_plus_present == True or minus_minus_present == True:
            return True

    #if the intuitive doesn't match the current ++ or --
    if plus_plus_present == True and list(initiative_value)[1] == "+":
        return True
    if minus_minus_present == True and list(initiative_value)[1] == "-":
        return True

    return False

def get_if_some_of_player_or_evil_values_are_not_present():
    for key,value in initiative_rolls_dictionary.items():
        if (value is None and
            key != "Good"):
            return True
    return False

def take_initiative_roles():
    """
    # this takes in integers.

    ## if players get the same integer
    in situations in which 2 players get the same integer,
    they roll again and whoever gets the bigger number gets higher integrative by a half.
    represented by a ++ or a -- penning on if you won or lost the roll off.

    for example.
        Mikey and Forest both get 10
        they roll off, Mikey gets 12, Forest gets 9
        Mikey is 10++, Forest is 10--

    ## GUI statement
    this is supposed to emulate google docs very minorly.
    * you cannot edit the text where it says the character's names
    * if you enter letters or poor integer syntax the system asks for initiative roles again.
    * "Good" can be None, but "Evil" and the other 4 inputs cannot be None.
    * you can swap from character input to character input freely using the arrow keys
    * press enter on the keyboard or the rightward arrow key to continue through the combat sim

    ## implementation
    * i tried asking claude how to do this and:
        * the library (curses) it initially used was pissy pant and didn't work on pycharm very well.
          how tf people use that library when it's such a pain in the ass when
            windows + pycharm
          idk. and i don't care.
        * it then tried to use somethign else and the code it made was shit
        * so clanking this bitch isn't worked so i have to make somethign more archaic.

    make it look like this:
    ```
    take_initiative_roles
        we need to take initiative roles
        use the UP and DOWN arrow keys to swap from input to input
        press ENTER to register a integer in a initiative role
        press the RIGHT ARROW button to continue
            if a player is absent, or there's no good or bad NPCs
            controlled by the DM, leave that parameter blank

        → Mikey:
          Forest:
          Thalis:
          Micheal:
          Evil:
          Good:
    ```
    :return: modified initiative_roles_dictionary variable that contains initiative roles
    """
    selected_roll_taker_index = 0
    update_initiative_roles_screen_and_return_user_input(
        failed_initiative_input_bool=False,
        duplicate_initiative_input_bool=False,
        roll_off_respected_bool=False,
        selected_roll_taker_index=selected_roll_taker_index
    )
    initiative_keep_program_running_bool = True

    while initiative_keep_program_running_bool:
        in_loop_failed_initiative_input_bool = False
        in_loop_duplicate_initiative_input_bool = False
        in_loop_roll_off_respected_bool = False

        #these 2 lines are so duplicate inputs aren't recorded / holding down the key does nothing
        event = keyboard.read_event()
        if event.event_type == keyboard.KEY_DOWN:

            if keyboard.is_pressed("q"):
                if confirm_quit_via_keyboard():
                    print("\tquitting...")
                    exit(0)

            #the arrow keys
            if keyboard.is_pressed("up"):
                modifier = -1
                if get_if_selected_roll_taker_index_is_beyond_limits(selected_roll_taker_index=selected_roll_taker_index,
                                                                     modifier=modifier):
                    selected_roll_taker_index += modifier
                    update_initiative_roles_screen_and_return_user_input(
                        duplicate_initiative_input_bool=in_loop_duplicate_initiative_input_bool,
                        failed_initiative_input_bool=in_loop_failed_initiative_input_bool,
                        roll_off_respected_bool=in_loop_roll_off_respected_bool,
                        selected_roll_taker_index=selected_roll_taker_index
                    )
                """
                else:
                    print("selected_roll_taker_index :",selected_roll_taker_index)
                    print("modifier :",modifier)
                """
            elif keyboard.is_pressed("down"):
                modifier = 1
                if get_if_selected_roll_taker_index_is_beyond_limits(selected_roll_taker_index=selected_roll_taker_index,
                                                                     modifier=modifier):
                    selected_roll_taker_index += modifier
                    update_initiative_roles_screen_and_return_user_input(
                        failed_initiative_input_bool=in_loop_failed_initiative_input_bool,
                        duplicate_initiative_input_bool=in_loop_duplicate_initiative_input_bool,
                        roll_off_respected_bool=in_loop_roll_off_respected_bool,
                        selected_roll_taker_index=selected_roll_taker_index
                    )
                """
                else:
                    print("selected_roll_taker_index :", selected_roll_taker_index)
                    print("modifier :", modifier)
                """
            elif keyboard.is_pressed("enter"):
                initiative_keep_program_running_bool = False

            #actually inputting initative values
            elif keyboard.is_pressed("right"):
                """
                what it did here instead of doing input()
                chat did keyboard library shit instead.
                    wow :DDDD
                """
                selected_dictionary_key = list(initiative_rolls_dictionary.keys())[selected_roll_taker_index]

                initiative_input_clarification_text = (
                        "\t → " + selected_dictionary_key + " : "
                )

                initiative_value = ""

                print(initiative_input_clarification_text, end="", flush=True)

                while True:
                    event = keyboard.read_event()

                    if event.event_type == keyboard.KEY_DOWN:
                        if event.name == "left":
                            break

                        # Numbers
                        if (event.name.isdigit() or
                                event.name == "+" or
                                event.name == "-"):
                            initiative_value += event.name
                            print(event.name, end="", flush=True)

                        # Backspace
                        elif event.name == "backspace":
                            if initiative_value:
                                initiative_value = initiative_value[:-1]
                                print("\b \b", end="", flush=True)

                        # Enter = finish entering this initiative
                        elif event.name == "right":
                            if get_if_initiative_input_is_failed_input(initiative_value):
                                initiative_value = None
                                in_loop_failed_initiative_input_bool = True
                                break
                            elif get_if_initiative_input_is_duplicate_input(
                                    initiative_value=initiative_value,
                                    selected_dictionary_key=selected_dictionary_key,
                                    initiative_rolls_dictionary=initiative_rolls_dictionary
                            ):
                                initiative_value = None
                                in_loop_duplicate_initiative_input_bool = True
                                break
                            elif get_roll_off_respected_bool(initiative_value):
                                initiative_value = None
                                in_loop_roll_off_respected_bool = True
                                break
                            else:
                                break

                if initiative_value == "":
                    initiative_rolls_dictionary[selected_dictionary_key] = None
                else:
                    initiative_rolls_dictionary[selected_dictionary_key] = initiative_value

                update_initiative_roles_screen_and_return_user_input(
                    duplicate_initiative_input_bool=in_loop_duplicate_initiative_input_bool,
                    failed_initiative_input_bool=in_loop_failed_initiative_input_bool,
                    roll_off_respected_bool=in_loop_roll_off_respected_bool,
                    selected_roll_taker_index=selected_roll_taker_index
                )

    if get_if_all_rolls_in_initiative_rolls_are_all_none():
        print("all of the values in the intiative_rolls_dictionary is blank. That's bad.")
    if get_if_some_of_player_or_evil_values_are_not_present():
        print("some of the values in the initiative_rolls_dictionary are blank. That's questionable, i hope you know what you're doing.")

    #print(initiative_rolls_dictionary)
    return initiative_rolls_dictionary