import copy
import os
import random
from sympy import true

from A_GUI_programs.universal_terminal_clear import universal_terminal_clear
from A_GUI_programs.wait_random_buffer import wait_random_buffer

BUFFER_TIME_MAX = 2
BUFFER_TIME_MIN = 0.001

"""
================================================
                    display
================================================
"""

def print_2d_list_with_decreasing_buffer\
            (list_in_question,
            buffer_time_max=BUFFER_TIME_MAX,
            buffer_time_min=BUFFER_TIME_MIN,
            tab_amount=""):
    buffer_time_max_editable = buffer_time_max
    buffer_time_min_editable = buffer_time_min


    """
    the intended effect here is that the systems stutters a bit and then shits out the aray
    after the array is shielded then it "solves itself". so it turns into 1s or 0s.
    """
    for row in list_in_question:
        for element in row:
            wait_random_buffer(max=buffer_time_max_editable,min=buffer_time_min_editable,tab_amount=tab_amount)
            print(element, end=" ")
            if (not(buffer_time_min_editable == buffer_time_max_editable)
               or
               not((buffer_time_max_editable / 2) < buffer_time_min_editable)):
                buffer_time_max_editable /= 2
        wait_random_buffer(max=buffer_time_max_editable,min=buffer_time_min_editable,tab_amount=tab_amount)
        print()

def print_2d_list_with_buffer(list_in_question,
                              buffer_time_max=BUFFER_TIME_MAX,
                              buffer_time_min=BUFFER_TIME_MIN,
                              tab_amount=""):
    for row in list_in_question:
        for element in row:
            wait_random_buffer(max=buffer_time_max,min=buffer_time_min,tab_amount=tab_amount)
            print(element, end=" ")
        wait_random_buffer(max=buffer_time_max,min=buffer_time_min,tab_amount=tab_amount)
        print()

"""
=============================================
          random number shenanigans
=============================================
"""

def get_random_numbers_array(tab_amount=""):
    """
    1. make an array that semi depends on the terminal
    2. put random numbers in that array
    3. return

    :param tab_amount:
    :return:
    """
    #creating the thing
    terminal_size = 1

    try:
        terminal_size = os.get_terminal_size()
    except OSError:
        # Fallback to a default size if the handle is invalid
        # or if you're in pycharms run lol
        from collections import namedtuple
        TerminalSize = namedtuple('TerminalSize', ['columns', 'lines'])
        terminal_size = TerminalSize(80, 24)

    #terminal_size_rows = terminal_size.lines
    terminal_size_rows = 50 #i want it to go off the page :-/
    terminal_size_columns = terminal_size.columns
    random_numbers_array = \
    [
        [0 for col in range(terminal_size_columns)]
        for row in range(terminal_size_rows)
    ]

    print()

    #not really :-3. just the dimensions
    print("number of top secrets =",terminal_size_rows)
    print("number of enemies to slay =",terminal_size_rows)
    print()

    #fill the array with random integers
    for row in range(terminal_size_rows):
        for col in range(terminal_size_columns):
            random_int = random.randint(0,9)
            random_numbers_array[row][col] = random_int

    return random_numbers_array

def get_solved_random_numbers_array(array_in_question, tab_amount=""):
    copied_array_in_question = copy.deepcopy(array_in_question)
    row_count = len(copied_array_in_question)
    column_count = len(copied_array_in_question[0])

    for i in range(row_count):
        for j in range(column_count):
            if copied_array_in_question[i][j] >= 5:
                copied_array_in_question[i][j] = 1
            else:
                copied_array_in_question[i][j] = 0
    return copied_array_in_question

"""
====================================================
            dungeon specific functions
====================================================
"""

def print_starting_noise(tab_amount=""):
    """
    it's going to start off as a bunch of random numbers that change every half second or so
    then eventually a random number will turn into either a 1 or a 0

    :param tab_amount:
    :return:
    """
    random_numbers_array = get_random_numbers_array()
    print_2d_list_with_decreasing_buffer(list_in_question=random_numbers_array)
    print("\nwaiting for micro tech slaves...")
    wait_random_buffer()
    wait_random_buffer()
    print("found slaves, dispatching particle whips")
    wait_random_buffer()
    print("particle whips dispatched. configuring duties\n")

    continue_noise_1 = input("continue? (y/n)")
    while not (continue_noise_1 == 'n' or continue_noise_1 == 'y'):
        continue_noise_1 = input("yes or no please: ")
    if continue_noise_1 == 'n':
        universal_terminal_clear()
        exit(0)

    wait_random_buffer()
    solved_random_numbers_array = get_solved_random_numbers_array(array_in_question=random_numbers_array)
    print_2d_list_with_decreasing_buffer(list_in_question=solved_random_numbers_array)
    wait_random_buffer()
    wait_random_buffer()
    print("preparing murder")

    continue_noise_2 = input("continue? (y/n)")
    while not (continue_noise_2 == 'n' or continue_noise_2 == 'y'):
        continue_noise_2 = input("yes or no please: ")
    if continue_noise_2 == 'n':
        universal_terminal_clear()
        exit(0)

    wait_random_buffer()
    wait_random_buffer()
    wait_random_buffer()
    print("murdering...")
    wait_random_buffer()
    wait_random_buffer()
    wait_random_buffer()
    print("murdering...")
    wait_random_buffer()
    wait_random_buffer()
    wait_random_buffer()
    print("murdering...")


def get_if_credentials_match(username_try, password_try, available_usernames, available_passwords):
    if username_try in available_usernames and password_try in available_passwords:
        if     ((username_try == available_usernames[0] and password_try == available_passwords[0])
                or
                (username_try == available_usernames[1] and password_try == available_passwords[1])
                or
                (username_try == available_usernames[2] and password_try == available_passwords[2])):
            return True
        else:
            return False
    else:
        return False


def login_phase():
    print("LOG IN")
    print("press \'q\' to quit")
    username_try = input("Username: ")
    # every ninja had access to this computer but they're not gonna notice :-/
    available_usernames = \
        [
            "TurtleSlayer73",
            "GoopEnjoyer999",
            "Ao_Suzuki"
        ]
    if username_try == "q":
        exit(0)
    while username_try not in available_usernames:
        if username_try == "q":
            exit(0)
        username_try = input("\tInvalid username, please try again: ")
    print("successful username")

    password_try = input("Password: ")
    available_passwords = \
        [
            "password",
            "Zorblina",
            "tekitaitekibaishu"  # "hostile takeover"
        ]
    if password_try == "q":
        exit(0)
    while not get_if_credentials_match(username_try=username_try,
                                       password_try=password_try,
                                       available_usernames=available_usernames,
                                       available_passwords=available_passwords):
        if password_try == "q":
            exit(0)
        password_try = input("\tInvalid password, please try again: ")
    print("successful password")
    print("logging in...")
    wait_random_buffer()
    wait_random_buffer()
    print("logged in")
    input("press enter to continue: ")
    universal_terminal_clear()
    username_and_password_dict = {"username" : username_try,
                                  "password" : password_try,}
    return username_and_password_dict

def im_in_phase(good_credentials):
    print("you are logged in as: ", good_credentials["username"])
    guide_string = \
        """
        1. make computer scream
        2. unlock door
        3. show most recent diary entry
        4. write diary entry
        q. quit
        """
    print(guide_string)
    userinput = input("what would you like to do?: ")

    while true:
        valid_inputs = ["1","2","3","4","q"]
        universal_terminal_clear()
        if userinput in valid_inputs:
            if userinput == "1":
                #wtf am I doing?
                scream_sounds = \
                [
                    "oww stop <:-(",
                    "stop it!",
                    "stop that hurts!",
                    "you're hurting me!"
                ]
                scream_number = random.randint(0,3)
                print("you are logged in as: ", good_credentials["username"])
                print(guide_string)
                print("\t\t",scream_sounds[scream_number],"\n")
                userinput = input("what would you like to do?: ")
            elif userinput == "2":
                print("you are logged in as: ", good_credentials["username"])
                print(guide_string)
                print("\t\tbeep beep! door's unlocked! \n\t\tyou can go in now\n")
                userinput = input("what would you like to do?: ")
            elif userinput == "3":
                print("you are logged in as: ", good_credentials["username"])
                print(guide_string)
                if good_credentials["username"] == "TurtleSlayer73":
                    print("""\t\t    Why the fuck do we have to write diaries man. 
                    I've got way to much internet to see after I got broadband after dialup man.
                    You know how much porn you can download with broadband internet? 
                    A lot! A lot!
                    And i have that because of shredder so i guess making this diary is worth it. 
                    """)
                elif good_credentials["username"] == "GoopEnjoyer999":
                    print("""\t\t    I know someone probably reads these but i'm thinking about putting my 2 weeks in.
                    It's not putting people in cages or fighting monsters but it's more that I have to do it 
                    with someone like Slayer. Guy's a weirdo. 
                    
                    Also. Fuck the yellow ninjas man. I could do so much better with a bomb. All of them are dickless losers.
                    """)
                elif good_credentials["username"] == "Ao_Suzuki":
                    print("""\t\t    私は私だ。私は変われないし、あなたも変われない。誰も変われない。
    
                    なぜこれを読んでいるんだ？
                    
                    さっさとドアを開けてくれ。
                    
                    まあ、せっかくここまで来たんだから、正直に言おう。ここは嫌いだ。醜い人ばかりだ。唯一まともなのはバーガーキングだけだ。
                    """)
                userinput = input("what would you like to do?: ")
            elif userinput == "4":
                print("you are logged in as: ", good_credentials["username"])
                print(guide_string)
                print("\t\tERROR: write_diary_and_push_to_evil_os_mainframe: word anus is leaking.\n")
                userinput = input("what would you like to do?: ")
            elif userinput == "q":
                exit(0)
        else:
            print("you are logged in as: ", good_credentials["username"])
            print(guide_string)
            print("\nbad input, please try again.\n")
            userinput = input("what would you like to do?")

def DMV_door_minigame(tab_amount=""):
    universal_terminal_clear()
    userInput = input("press enter to continue:")
    if userInput == "FUCK_YOU":
        good_credentials = {"username" : "TurtleSlayer73",
                            "password" : "password"}
        universal_terminal_clear()
        im_in_phase(good_credentials=good_credentials)
    else:
        universal_terminal_clear()
        wait_random_buffer()
        print("initializing Evil Ninja OS...")
        wait_random_buffer()

        #the goofy ahh \0 doesn't show in the terminal. so don't worry about it.
        print_starting_noise()
        wait_random_buffer()
        wait_random_buffer()
        universal_terminal_clear()

        print("finished booting. fucking finally >:-(")
        good_credentials = login_phase()
        im_in_phase(good_credentials)

if __name__ == "__main__":
    DMV_door_minigame()