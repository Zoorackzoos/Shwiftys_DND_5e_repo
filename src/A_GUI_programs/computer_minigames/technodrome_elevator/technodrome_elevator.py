import os
import random

import keyboard

from A_GUI_programs.computer_minigames.DMV_door_minigame.DMV_door_minigame import get_random_numbers_array
from A_GUI_programs.confirm_quit_via_keyboard import confirm_quit_via_keyboard
from A_GUI_programs.universal_terminal_clear import universal_terminal_clear
from A_GUI_programs.wait_random_buffer import wait_random_buffer


def prompt_start_of_program():
    print("start? (y/n)")
    while True:
        event = keyboard.read_event()
        if event.event_type == keyboard.KEY_DOWN:
            if event.name == "y":
                print("\tstarting...")
                print("\tinitializing Evil Ninja OS...")
                break
            elif event.name == "n":
                print("\tquitting...")
                exit(0)
            else:
                universal_terminal_clear()
                print("start? (y/n)")
                print("you didn't put in 'y' or 'n'. Choose.")

def play_intro_noise():
    print("fuck man don't make me do my job.")
    wait_random_buffer()
    wait_random_buffer()
    wait_random_buffer()
    wait_random_buffer()
    print("omfg. i don't get paid enough for this shit.")
    wait_random_buffer()
    print("jerking off number penises...")
    wait_random_buffer()
    print("incoming...")
    wait_random_buffer()
    wait_random_buffer()
    wait_random_buffer()
    wait_random_buffer()
    wait_random_buffer()

    amount_of_times_program_pretends_to_fail = random.randint(3,5)

    print("need to guess system hash:")
    wait_random_buffer()
    print("\tguessing")
    wait_random_buffer()

    counter = 0
    #this is supposed to be a computer talking. i never speak to people in this way.
    failure_swear_text_list = \
    [
        "FUCK!",
        "dammit",
        "piece of shit!",
        "What are you made of?!? fucking aluminum?",
        "I'm gonna fucking sodomize you, you stupid bitch",
        "fuckin- DUDE I COULD HAVE BEEN A FUCKING TAVERN OWNER. NOW I'M HERE. I HOPE YOU ALL GET SENT TO HELL FOREVER.",
        "cunt",
        "ass"
    ]

    while counter < amount_of_times_program_pretends_to_fail:
        print("\t\ttry: ",random.randint(-1000,1000))
        wait_random_buffer()
        wait_random_buffer()
        wait_random_buffer()
        counter += 1
        if counter >= amount_of_times_program_pretends_to_fail:
            print("\t\t\tfinally")
            wait_random_buffer()
            wait_random_buffer()
        else:
            print("\t\t\t",failure_swear_text_list[random.randint(0,len(failure_swear_text_list)-1)])
            wait_random_buffer()
            wait_random_buffer()
            wait_random_buffer()

    #this is the part where the system just shits out numbers
    try:
        terminal_size = os.get_terminal_size()
    except OSError:
        # Fallback to a default size if the handle is invalid
        # or if you're in pycharms run lol
        from collections import namedtuple
        TerminalSize = namedtuple('TerminalSize', ['columns', 'lines'])
        terminal_size = TerminalSize(80, 24)

    terminal_size_rows = terminal_size.lines
    terminal_size_columns = terminal_size.columns
    random_numbers_array = random_numbers_array = \
    [
        [0 for col in range(terminal_size_columns)]
        for row in range(terminal_size_rows)
    ]
    # fill the array with random integers
    for row in range(terminal_size_rows):
        for col in range(terminal_size_columns):
            random_int = random.randint(0, 9)
            random_numbers_array[row][col] = random_int

    counter = 0
    for row in random_numbers_array:
        if counter >= 2:
            wait_random_buffer(min=0.001,max=0.1)
            print(row)
        else:
            wait_random_buffer()
            wait_random_buffer()
            print(row)
            counter += 1

    print("proceed? (y/n)")
    while True:
        event = keyboard.read_event()
        if event.event_type == keyboard.KEY_DOWN:
            if event.name == "y":
                print("\tstarting...")
                break
            elif event.name == "n":
                print("\tquitting...")
                exit(0)
            else:
                universal_terminal_clear()
                print("proceed? (y/n)")
                print("you didn't put in 'y' or 'n'. Choose.")

def let_user_choose_and_answer_question():
    question_choose_string = \
"""
In order to make the elevator go up you must answer one of the two questions.
The 'realness' of the questions should not be brought into question for your own mental health.
If that's something you prioritize anyway.

pick the number corresponding to the question type, to select it. 
I'll.
i mean, then the system will give you a confirmation message

question types are the following
1. animation
2. fix your teeth
"""
    print(question_choose_string)

    main_question_choose_loop_bool = True
    question_confirmation_loop_bool = True

    while main_question_choose_loop_bool:
        event = keyboard.read_event()
        if event.event_type == keyboard.KEY_DOWN:

            if keyboard.is_pressed("q"):
                if confirm_quit_via_keyboard():
                    print("quiting...")
                    exit(0)

            if event.name == "1":
                print("You've chosen 'animation'. Are you sure?")
                while question_confirmation_loop_bool:
                    event = keyboard.read_event()
                    if event.event_type == keyboard.KEY_DOWN:
                        if event.name == "y":
                            animation_question()
                            question_confirmation_loop_bool = False
                            main_question_choose_loop_bool = False
                        if event.name == "n":
                            question_confirmation_loop_bool = False

            if event.name == "2":
                print("You've chosen 'fix your teeth'. Are you sure?")
                while question_confirmation_loop_bool:
                    event = keyboard.read_event()
                    if event.event_type == keyboard.KEY_DOWN:
                        if event.name == "y":
                            fix_your_teeth_question()
                            question_confirmation_loop_bool = False
                            main_question_choose_loop_bool = False
                        if event.name == "n":
                            question_confirmation_loop_bool = False



def animation_question():
    pass

def fix_your_teeth_question():
    pass

def technodrome_elevator():
    universal_terminal_clear()
    wait_random_buffer()
    prompt_start_of_program()

    universal_terminal_clear()
    wait_random_buffer()
    play_intro_noise()

    universal_terminal_clear()
    wait_random_buffer()
    let_user_choose_and_answer_question()

if __name__ == "__main__":
    technodrome_elevator()