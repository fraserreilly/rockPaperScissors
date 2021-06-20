from pynput import keyboard
import random

print("Please choose Rock, Paper or Scissors by clicking 1, 2 or 3 respectively. To exit the game click escape.")


def on_press(key):
    if key == keyboard.KeyCode(char='1'):
        userMove = 1
        rps(userMove)
    elif key == keyboard.KeyCode(char='2'):
        userMove = 2
        rps(userMove)
    elif key == keyboard.KeyCode(char='3'):
        userMove = 3
        rps(userMove)
    else:
        if keyboard.Key.esc:
            pass
        else:
            print("Please click either 1, 2 or 3.")


def on_release(key):
    if key == keyboard.Key.esc:
        return False


def rps(userMove):
    computerMove = random.randint(1, 3)
    if userMove == computerMove:
        print("Tie game, Play again or exit.")
    elif userMove or computerMove == 1 & computerMove or userMove == 3:
        if userMove == 1:
            print("You win! Play again or exit.")
        else:
            print("You lose! Play again or exit.")
    elif userMove or computerMove == 3 & computerMove or userMove == 2:
        if userMove == 3:
            print("You win! Play again or exit.")
        else:
            print("You lose! Play again or exit.")
    elif userMove or computerMove == 2 & computerMove or userMove == 1:
        if userMove == 2:
            print("You win! Play again or exit.")
        else:
            print("You lose! Play again or exit.")


with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()
