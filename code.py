import time
import sys
import os
import random
def typewriter (text, delay=0.05):
    """Simulates typing effect"""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()
def glitch_effect(duration=2):
    """Simulates a glitch effect in the terminal"""
    glitch_chars = ['#', '%', '&', '$', '@', '!', '?', '*']
    end_time = time.time() + duration
    while time.time() < end_time:
        line = ".join(random.choice(glitch_chars) for _ in range(60))"
        sys.stdout.write("\r" + line)
        sys.stdout.flush()
        time.sleep(0.05)
    print("\r" + " " * 60, end="\r")
def message_box(text, wait_time=0, closable=True):
    """Displays a message box-like event"""
    border = "+" + "-" * (len(text) + 2) + "+"
    print(border)
    print(f"| {text} |")
    print(border)
    if closable:
        input("\n[OK]")
    elif wait_time > 0:
        time.sleep(wait_time)
def easter_egg_event():
    """Main easter egg sequence"""
    typewriter("Restoring Liza...")
    time.sleep(1.5)
    glitch_effect(2)
    typewriter("Liza reappears - her eyes are completely white.", 0.04)
    time.sleep(1)
    glitch_effect(1.5)
    message_box("Just Liza!", closable=True)
    glitch_effect(2)
    message_box("Just Jessica", wait_time=6, closable=False)
    glitch_effect(2)
    typewriter("Liza's presence fades away...")
    time.sleep(1.5)
    typewriter("Jessica has deleted Liza.", 0.05)
    time.sleep(2)
    typewriter("...", 0.3)
    typewriter("End of event.")
def main():
    print("Act 6-7. The room is silent.")
    user_input = input("\n> ").strip()
    user_input.lower() == "liza?"
        easter_egg_event() # properly indented
    else:
        print("Nothing happens.")
if __name__ == "__main__":
    main() # top-level, no extra
