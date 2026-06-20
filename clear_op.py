import os
import time

def woosh(t=3):
    print("The previous outputs will clear soon.")
    time.sleep(1)

    # Count down in place
    for i in range(t, 0, -1):
        print(f"\rClearing in {i}...", end="", flush=True)
        time.sleep(1)

    os.system('cls' if os.name == 'nt' else 'clear')
    