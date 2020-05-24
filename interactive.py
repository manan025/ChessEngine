import time
from time import sleep as delay


def info(p1, p2):
    print(f"---\nHello, {p1}, You are playing as White and you will start the game!\nAll the Best!\n@TeamChess\n---")
    delay(2)
    print(f"---\nHello, {p2}, You are playing as Black!\nBest Wishes!\n@TeamChess\n---")
    delay(2)
    if input("Would you like to take a look at rules? [y/n] ").strip().lower() == any(("y", "yes")):  # TODO: Not Working
        print("Here are the rules, Take a look at them:")
    else:
        print("Let's continue playing!")
