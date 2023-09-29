import pyautogui
import time
from pynput.keyboard import *

#  ======== settings ========
delay = 0.5  # in seconds
resume_key = Key.f1
pause_key = Key.f2
exit_key = Key.esc
#  ==========================

pause = True
running = True
keyboard = Controller()

def on_press(key):
    global running, pause

    if key == resume_key:
        pause = False
        print("[Resumed]")
    elif key == pause_key:
        pause = True
        print("[Paused]")
    elif key == exit_key:
        running = False
        print("[Exit]")


def display_controls():
    print("// AutoClicker by iSayChris")
    print("// - Settings: ")
    print("\t delay = " + str(delay) + ' sec' + '\n')
    print("// - Controls:")
    print("\t F1 = Resume")
    print("\t F2 = Pause")
    print("\t F3 = Exit")
    print("-----------------------------------------------------")
    print('Press F1 to start ...')


def main():
    lis = Listener(on_press=on_press)
    lis.start()

    display_controls()
    while running:
        if not pause:
            #
            pyautogui.click(pyautogui.position())
            time.sleep(0.01)

            keyboard.press('i')
            time.sleep(0.01)
            keyboard.release('i')
            time.sleep(0.01)


            keyboard.press('b')
            time.sleep(0.01)
            keyboard.release('b')
            time.sleep(0.01)

            keyboard.press('n')
            time.sleep(0.01)
            keyboard.release('n')
            time.sleep(0.01)

            keyboard.press('m')
            time.sleep(0.01)
            keyboard.release('m')
            time.sleep(0.01)

            keyboard.press('o')
            time.sleep(0.01)
            keyboard.release('o')
            time.sleep(0.01)

            keyboard.press('z')
            time.sleep(0.01)
            keyboard.release('z')
            time.sleep(0.01)

            keyboard.press('x')
            time.sleep(0.01)
            keyboard.release('x')
            time.sleep(0.01)

            #keyboard.press('c')
            time.sleep(0.01)
            #keyboard.release('c')
            time.sleep(0.01)

            pyautogui.PAUSE = delay
    lis.stop()


if __name__ == "__main__":
    main()