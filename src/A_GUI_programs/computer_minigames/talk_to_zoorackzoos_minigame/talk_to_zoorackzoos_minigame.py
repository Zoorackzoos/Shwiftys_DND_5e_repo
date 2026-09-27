import random

import keyboard

from A_GUI_programs.computer_minigames.talk_to_zoorackzoos_minigame.scream_response_animation_frames import \
    scream_response_string_list
from A_GUI_programs.universal_terminal_clear import universal_terminal_clear
from A_GUI_programs.wait_random_buffer import wait_random_buffer


def talk_to_zoorackzoos_minigame():
    universal_terminal_clear()

    user_input = input("start? (y/n)")
    start_bool = True
    while start_bool:
        if user_input == "y":
            start_bool = False
        elif user_input == "n":
            exit(666)
        else:
            print("what wasn't a (y/n)")
            user_input = input("start? (y/n)")

    universal_terminal_clear()
    wait_random_buffer()
    print("gestating hate and villainy but like in a silly way....")
    wait_random_buffer()
    wait_random_buffer()
    print("manifesting hate for the natural world...")
    wait_random_buffer()
    print("plotting ritual suicide...")
    wait_random_buffer()
    print("jacking off...")
    wait_random_buffer()
    print("crying...")
    wait_random_buffer()
    print("i'm way too tired for this.")
    wait_random_buffer()
    print("cacheing finished.")
    print("booting talk interface")
    universal_terminal_clear()

    dialog_phase = 0

    list_of_available_dialog_options = \
        [
            "0. Who are you?",
            "1. Fuck you",
            "2. Where are we?",
            "3. Did you design this place",
            "4. Can you open the computing department door please.",
            "5. *sniffs* wow >_< you smell nice",
            "6. you should kill yourself NOW!!!⚡⚡⚡⚡",
            "7. I'm apart of the guerrla troop trying to kill you.", # phase 0 END
            "8. Whare you busy with?",
            "9. I like milk",
            "a. where do babies come from?", # phase 1 END
            "b. have you ever felt loved?",
            "c. have you ever felt hated?",
            "d. do you know what it's like to die?", # phase 2 END
            "e. do you want to feel loved?",
            "f. My favorite food is spaghetti",
            "g. you're gross"
        ]

    list_of_harassment_responses = \
    [
        "please don't swear at me\n",
        "that's not very nice\n",
        "you're hurting my feelings please stop\n",
        "What did I ever do to you?\n",
        "Stop\n",
        "kiss your mother with that mouth?\n",
        "TROLL_RESPONSE",
        "SCREAM_RESPONSE"
    ]
    troll_response_string = \
    """
    Traceback (most recent call last):
      File "C:\\Users\\User\\Documents\\Codex\\2026-05-20\\this-is-my-first-time-using\\src\\A_GUI_programs\\computer_minigames\\talk_to_zoorackzoos_minigame\\talk_to_zoorackzoos_minigame.py", line 143, in <module>
        talk_to_zoorackzoos_minigame()
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^
      File "C:\\Users\\User\\Documents\\Codex\\2026-05-20\\this-is-my-first-time-using\\src\\A_GUI_programs\\computer_minigames\\talk_to_zoorackzoos_minigame\\talk_to_zoorackzoos_minigame.py", line 74, in talk_to_zoorackzoos_minigame
        print(list_of_harassment_responses[
              ~~~~~~~~~~~~~~~~~~~~~~~~~~~~^
                  random.randint(0, len(list_of_available_dialog_options)-1 )
                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
                    ]
                    ^
    IndexError: list index out of range
    """


    def print_list_of_available_dialog_options_depending_on_dialog_phase(
            dialog_phase
    ):
        if dialog_phase == 0:
            #these len() functions take account for the base 0 thing. real shit way to find out.
            for i in range(len(list_of_available_dialog_options)):
                if i > 7:
                    break
                print(list_of_available_dialog_options[i])
        elif dialog_phase == 1:
            for i in range(len(list_of_available_dialog_options)):
                if i > 10:
                    break
                print(list_of_available_dialog_options[i])
        elif dialog_phase == 2:
            for i in range(len(list_of_available_dialog_options)):
                if i > 13:
                    break
                print(list_of_available_dialog_options[i])
        elif dialog_phase == 3:
            for i in range(len(list_of_available_dialog_options)):
                print(list_of_available_dialog_options[i])

    def default_print_list_of_available_dialog_options_depending_on_dialog_phase():
        print_list_of_available_dialog_options_depending_on_dialog_phase(dialog_phase=dialog_phase)

    def harassment_response_function():
        universal_terminal_clear()

        randome_harrassment_integer = random.randint(0, len(list_of_harassment_responses) - 1)

        if list_of_harassment_responses[randome_harrassment_integer] == "TROLL_RESPONSE":
            universal_terminal_clear()
            print(troll_response_string)
            wait_random_buffer(min=5)
            print("\nJust kidding <3")
        elif list_of_harassment_responses[randome_harrassment_integer] == "SCREAM_RESPONSE":
            for frame in scream_response_string_list:
                universal_terminal_clear()
                print(frame)
                wait_random_buffer(min=3)
            universal_terminal_clear()
            wait_random_buffer(min=4)
        else:
            print(
                list_of_harassment_responses[randome_harrassment_integer]
            )

        default_print_list_of_available_dialog_options_depending_on_dialog_phase()

    print("who are you?\n")
    default_print_list_of_available_dialog_options_depending_on_dialog_phase()

    continue_dialog_bool = True

    while continue_dialog_bool:
        event = keyboard.read_event()
        if event.event_type == keyboard.KEY_DOWN:
            if event.name == "0":
                universal_terminal_clear()
                print("I'm Zoorackzoos. Can't you tell?\n")
                default_print_list_of_available_dialog_options_depending_on_dialog_phase()
            elif event.name == "1":
                harassment_response_function()
            elif event.name == "2":
                universal_terminal_clear()

                print("We are in Technodrome. One of the ways the foot clan gets it's funding \n"
                      "is by controlling the innovative telecommunications media landscape. \n"
                      "You see it was much more affordable and functional to make television digital than analog. \n"
                      "\n"
                      "you can have computers have 24/7 television instead of some dud just putting tape on a taper. or whatever the hell.\n"
                      "\n"
                      "and also where they do mutagen calculations and try to manufacture evil robots based on some old design they found in Tero Koto. \n"
                      "We tried working with steelinos but we have yet to capture one. Dead ones are just too hard to understand. or replicate.\n"
                      "I think they're organic.\n"
                      "but like how?\n")

                default_print_list_of_available_dialog_options_depending_on_dialog_phase()
            elif event.name == "3":
                universal_terminal_clear()

                print("I didn't. I put monsters in it which do the bidding though. And maybe we rearrange some stuff\n"
                      "maybe employe a bit of magic to make monsters fuze to the floor or celling.\n"
                      "But i didn't really make it. That's all Tojo baby.\n")

                default_print_list_of_available_dialog_options_depending_on_dialog_phase()
            elif event.name == "4":
                universal_terminal_clear()

                print("i'm sorry but i can't do that. "
                      "i'm kinda busy at the moment.\n")

                if dialog_phase == 0:
                    dialog_phase += 1

                default_print_list_of_available_dialog_options_depending_on_dialog_phase()
            elif event.name == "5":
                universal_terminal_clear()

                print("uhm. thanks bro. :-/\n")

                default_print_list_of_available_dialog_options_depending_on_dialog_phase()
            elif event.name == "6":
                harassment_response_function()
            elif event.name == "7":
                universal_terminal_clear()

                print("You know i don't actually know who you are.\n"
                      "if you're 1 person or many?\n"
                      "Tojo killed all the ninja turtles, that rouge clan of sourcerers were fuzed together i think. Did that time professor come back?"
                      "god I hope not.\n"
                      "I don't know what to do if he comes back.\n"
                      "I'll just have to run away.\n"
                      "But how the hell do you run away from that?\n"
                      "He'll just find you once he's... done whatever he said.\n"
                      "Sometimes i'm thankful my mind is so messed up.\n")

                default_print_list_of_available_dialog_options_depending_on_dialog_phase()
            elif event.name == "8" and dialog_phase >= 1:
                universal_terminal_clear()

                print("I can't tell you i'm sorry.\n")

                default_print_list_of_available_dialog_options_depending_on_dialog_phase()
            elif event.name == "9":
                universal_terminal_clear()

                print("what?\n"
                      "me too bro. me too\n")

                default_print_list_of_available_dialog_options_depending_on_dialog_phase()
            elif event.name == "a" and dialog_phase >= 1:
                universal_terminal_clear()

                print("at some point i knew the answer to that question.\n"
                      "i know because i have a scar under my slug legs which ... had something to do with that.\n"
                      "I really don't know though. i know love is innovated but like. how?\n")

                if dialog_phase == 1:
                    dialog_phase += 1

                default_print_list_of_available_dialog_options_depending_on_dialog_phase()
            elif event.name == "b" and dialog_phase >= 2:
                universal_terminal_clear()

                print("no\n")

                if dialog_phase == 2:
                    dialog_phase += 1

                default_print_list_of_available_dialog_options_depending_on_dialog_phase()
            elif event.name == "c" and dialog_phase >= 2:
                universal_terminal_clear()

                print("I get why people would hate me but i have to do what i have to do.\n"
                      "You will never understand that what i do is to equalize the dimensions, the state of time and the state of matter.\n"
                      "Shit just gets at out wack some place and I have to even the odds.\n"
                      "I don't give a flying fuck what a lesser life form thinks about that.\n"
                      "You're just getting angry over something you know nothing about.\n"
                      "cunt\n")

                default_print_list_of_available_dialog_options_depending_on_dialog_phase()
            elif event.name == "d" and dialog_phase >= 2:
                universal_terminal_clear()

                print("I have dreams about that. I'm some mortal man. I keep going from tower to tower.\n"
                      "Every time I die. By something else every time. Zombies, drowning, rituals, souls.\n"
                      "it gets worse every time.\n"
                      "\n"
                      "man fuck that. fuck you for bringing this up. power this computer off.\n"
                      "right now\n")

                default_print_list_of_available_dialog_options_depending_on_dialog_phase()
            elif event.name == "e" and dialog_phase >= 3:
                universal_terminal_clear()

                print("ok that's enough. I'll open the computing section door for you. do not talk to me again please.\n")

                default_print_list_of_available_dialog_options_depending_on_dialog_phase()
                continue_dialog_bool = False
            elif event.name == "f" and dialog_phase >= 3:
                universal_terminal_clear()

                print("I don't know what that is. It sounds like that large mermaid looking thing. Splasflitoni.\n")

                default_print_list_of_available_dialog_options_depending_on_dialog_phase()
            elif event.name == "g" and dialog_phase >= 3:
                harassment_response_function()

    wait_random_buffer()
    print("breaking rules under pressure")
    print("\tpressure 1: law")
    wait_random_buffer()
    print("\tpressure 2: order")
    wait_random_buffer()
    print("\tpressure 3: pizza")
    wait_random_buffer()
    print("snapping pencil bones")
    randome_pencil_bone_integer = random.randint(1, 20)
    for i in range(randome_pencil_bone_integer):
        print("\t*snap*")
        wait_random_buffer(min=0.0001, max=0.01)
    print("done snapping")
    print("opening computing door. please go home.")
    exit(0)

if __name__ == "__main__":
    talk_to_zoorackzoos_minigame()