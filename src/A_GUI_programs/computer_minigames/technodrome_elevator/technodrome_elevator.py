import os
import random
from typing import Literal

import keyboard

from A_GUI_programs.computer_minigames.DMV_door_minigame.DMV_door_minigame import get_random_numbers_array
from A_GUI_programs.computer_minigames.technodrome_elevator.animation_frames.technodrome_animation_minigame_frames import \
    list_of_technodrome_elevator_animation_minigame_frames
from A_GUI_programs.computer_minigames.technodrome_elevator.animation_frames.technodrome_fix_your_teeth_animation_frames import \
    list_of_technodrome_elevator_fix_your_teeth_minigame_frames_no_cleaning, \
    list_of_technodrome_elevator_fix_your_teeth_minigame_frames_cleaning
from A_GUI_programs.confirm_quit_via_keyboard import confirm_quit_via_keyboard
from A_GUI_programs.universal_terminal_clear import universal_terminal_clear
from A_GUI_programs.wait_random_buffer import wait_random_buffer


def prompt_start_of_program():
    start_of_program_bool = True

    print("start? (y/n)")
    user_input = input()
    while start_of_program_bool:
        if user_input == "y" or user_input == "FUCK_YOU":
            print("\tstarting...")
            print("\tinitializing Evil Ninja OS...")
            start_of_program_bool = False
        elif user_input == "n":
            print("\tquitting...")
            exit(0)
        else:
            universal_terminal_clear()
            print("start? (y/n)")
            print("you didn't put in 'y' or 'n'. Choose.")
            user_input = input()

    return user_input

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
    random_numbers_array = \
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
        row_string = ""
        for number in row:
            row_string += str(number)

        if counter >= 2:
            wait_random_buffer(min=0.001,max=0.1)
            print(row_string)
        else:
            wait_random_buffer()
            wait_random_buffer()
            print(row_string)
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

    while main_question_choose_loop_bool:
        question_confirmation_loop_bool = True

        event = keyboard.read_event()
        if event.event_type == keyboard.KEY_DOWN:

            if keyboard.is_pressed("q"):
                if confirm_quit_via_keyboard():
                    print("quiting...")
                    exit(0)

            if event.name == "1":
                print("You've chosen 'animation'. Are you sure? (y/n)")
                while question_confirmation_loop_bool:
                    event = keyboard.read_event()
                    if event.event_type == keyboard.KEY_DOWN:
                        if event.name == "y":
                            question_confirmation_loop_bool = False
                            main_question_choose_loop_bool = False
                            animation_question()
                        if event.name == "n":
                            question_confirmation_loop_bool = False

                            universal_terminal_clear()
                            print(question_choose_string)

            if event.name == "2":
                print("You've chosen 'fix your teeth'. Are you sure? (y/n)")
                while question_confirmation_loop_bool:
                    event = keyboard.read_event()
                    if event.event_type == keyboard.KEY_DOWN:
                        if event.name == "y":
                            question_confirmation_loop_bool = False
                            main_question_choose_loop_bool = False
                            fix_your_teeth_question()
                        if event.name == "n":
                            question_confirmation_loop_bool = False

                            universal_terminal_clear()
                            print(question_choose_string)



def animation_question():
    universal_terminal_clear()
    animation_question_intro_string = \
"""
animation
    I'm going to play a video. But since this is in a terminal it will be hard to see. 
    I need you to tell me what you saw. if it's correct. I can power the elevator. if you got it wrong.

    I'm not sure what happens if you get it wrong. just get it right.
    I can only play this once.
    
    are you ready? (y/n)
"""
    print(animation_question_intro_string)
    user_input = input()

    temp_user_input_loop_bool = True

    while temp_user_input_loop_bool:
        if user_input == "y":
            temp_user_input_loop_bool = False
        elif user_input == "n":
            if confirm_quit_via_keyboard():
                exit(0)
        else:
            print(animation_question_intro_string)
            user_input = input()

    for frame in list_of_technodrome_elevator_animation_minigame_frames:
        universal_terminal_clear()
        print(frame)
        wait_random_buffer(min=2.0,max=2.0)

    animation_question_prompt_question_and_answer_string = \
"""
    Can you tell me what you saw?
    Put in a number corrosponding to what you saw.
    
    1. Man jumping
    2. Man running on a horse
    3. 2 people fighting
    4. Man getting shot
    5. Man drinking soda
    6. Girl playing vollyball
"""
    print(animation_question_prompt_question_and_answer_string)
    user_input = input()

    temp_user_input_loop_bool = True
    while temp_user_input_loop_bool:
        if user_input != 1:
            print(":-( ")
        elif user_input == 4:
            print(":-) ")
            temp_user_input_loop_bool = False

    universal_terminal_clear()
    print("starting up elevator")
    wait_random_buffer()
    print("brrrrrrr......")
    wait_random_buffer()
    wait_random_buffer()
    print("lobotomzing program.")
    exit(0)

def fix_your_teeth_question():
    universal_terminal_clear()
    print("fix your teeth")
    print("loading person to enslave...")
    wait_random_buffer()

    current_frame_selection = 0
    continue_fixing_teeth_bool = True
    teeth_selection_context_string = \
"""
    You need to fix this guy's teeth. 
    input his teeth as if it were a array. so the first tooth is "[0][0]".
    bad looking things need to be scrubed. 
    good looking things don't need to be scrubed. and also can't be scrubed. 
    I'm kind've stupid so don't make syntax mistakes or i won't know what you're on about.
"""
    teeth_cleaning_context_string = \
"""
    use the arrow keys to bring the toothbruth back and forth to clean his teeth.
"""

    while continue_fixing_teeth_bool:
        universal_terminal_clear()
        print("fixing your teeth")
        print(teeth_selection_context_string)
        print(list_of_technodrome_elevator_fix_your_teeth_minigame_frames_no_cleaning[current_frame_selection])
        user_input = input()
        if user_input == "[0][0]" and current_frame_selection == 0:
            current_frame_selection = initiate_cleaning_sub_minigame_and_increment_frame(current_frame_selection,
                                                                                         teeth_cleaning_context_string)
        elif user_input == "[0][2]" and current_frame_selection == 1:
            current_frame_selection = initiate_cleaning_sub_minigame_and_increment_frame(current_frame_selection,
                                                                                         teeth_cleaning_context_string)
        elif user_input == "[0][3]" and current_frame_selection == 2:
            current_frame_selection = initiate_cleaning_sub_minigame_and_increment_frame(current_frame_selection,
                                                                                         teeth_cleaning_context_string)
        elif user_input == "[0][4]" and current_frame_selection == 3:
            current_frame_selection = initiate_cleaning_sub_minigame_and_increment_frame(current_frame_selection,
                                                                                     teeth_cleaning_context_string)
        elif user_input == "[0][5]" and current_frame_selection == 4:
            current_frame_selection = initiate_cleaning_sub_minigame_and_increment_frame(current_frame_selection,
                                                                                         teeth_cleaning_context_string)
        elif user_input == "[0][6]" and current_frame_selection == 5:
            current_frame_selection = initiate_cleaning_sub_minigame_and_increment_frame(current_frame_selection,
                                                                                         teeth_cleaning_context_string)
        elif user_input == "[1][2]" and current_frame_selection == 6:
            current_frame_selection = initiate_cleaning_sub_minigame_and_increment_frame(current_frame_selection,
                                                                                         teeth_cleaning_context_string)
        elif user_input == "[1][4]" and current_frame_selection == 7:
            current_frame_selection = initiate_cleaning_sub_minigame_and_increment_frame(current_frame_selection,
                                                                                         teeth_cleaning_context_string)

    print("fix your teeth")
    print(list_of_technodrome_elevator_fix_your_teeth_minigame_frames_no_cleaning[current_frame_selection])
    print("you did it.")
    print("brrrr....")
    print("lobotomzing program.")
    exit(0)

def initiate_cleaning_sub_minigame_and_increment_frame(
    current_frame_selection,
   teeth_cleaning_context_string: str
):
    current_frame_selection += 1
    still_cleaning_int = random.randint(3, 5)
    times_cleaned = 0
    current_frame_cleaning = 1

    print("fix your teeth")
    print(teeth_cleaning_context_string)
    print(list_of_technodrome_elevator_fix_your_teeth_minigame_frames_cleaning[current_frame_cleaning])

    while still_cleaning_int > times_cleaned:
        event = keyboard.read_event()
        if event.event_type == keyboard.KEY_DOWN:
            if event.name == "left" and current_frame_cleaning != 0:
                current_frame_cleaning = 0
                print(list_of_technodrome_elevator_fix_your_teeth_minigame_frames_cleaning[current_frame_cleaning])
                times_cleaned += 1
            elif event.name == "right" and current_frame_cleaning != 2:
                current_frame_cleaning = 2
                print(list_of_technodrome_elevator_fix_your_teeth_minigame_frames_cleaning[current_frame_cleaning])
                times_cleaned += 1
    return current_frame_selection


def technodrome_elevator():
    universal_terminal_clear()
    wait_random_buffer()
    user_input = prompt_start_of_program()

    if user_input == "FUCK_YOU":
        universal_terminal_clear()
        let_user_choose_and_answer_question()
    else:
        universal_terminal_clear()
        wait_random_buffer()
        play_intro_noise()

        universal_terminal_clear()
        wait_random_buffer()
        let_user_choose_and_answer_question()

if __name__ == "__main__":
    technodrome_elevator()