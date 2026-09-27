import time


def game_terminal_clear():
    print("\033[2J\033[H", end="")


print("FRAME 1")
print("This is a test.")
print("This is a REALLY REALLY REALLY REALLY REALLY REALLY REALLY REALLY REALLY REALLY REALLY REALLY REALLY REALLY REALLY REALLY REALLY REALLY REALLY REALLY long line.")

time.sleep(2)

game_terminal_clear()

print("FRAME 2")
print("If you can only see FRAME 2, the clear worked.")

time.sleep(2)

game_terminal_clear()

print("FRAME 3")
print("The previous frames should be gone.")