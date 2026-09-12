import keyboard

from A_GUI_programs.universal_terminal_clear import universal_terminal_clear
from A_GUI_programs.wait_random_buffer import wait_random_buffer


def play_intro_noise():
    wait_random_buffer()
    while True:
        print("start? (y/n)")
        event = keyboard.read_event()
        if event.event_type == keyboard.KEY_DOWN:
            if event.name == "y":
                print("\tstarting...")
            elif event.name == "n":
                print("\tquitting...")
                exit(0)
            else:
                universal_terminal_clear()
                print("you didn't put in 'y' or 'n'. Choose.")

def technodrome_elevator():
    universal_terminal_clear()
    play_intro_noise()

if __name__ == "__main__":
    technodrome_elevator()