from os import system
from time import sleep
import keyboard
import mouse
from timeit import default_timer
from ctypes import *


'''Default Variables'''
type_time_interval = 0.1


def input(command, time):
    keyboard.press_and_release('t')
    sleep(time)
    keyboard.write(command)
    sleep(time)
    keyboard.press_and_release('enter')
    sleep(time)


def start(time):
    system('cls')
    sleep(3)
    input('Press enter to continue.', time)
    while True:
        event = keyboard.read_event()
        if event.event_type == 'down' and event.name == 'enter':
            break
    input('Start execution.', time)


def end(time):
    input('/kill @e[type=item]', time)
    input('Finished execution.', time)
    exit()


def mouse_lock_1():
    # only work in windows not ingame
    pos = mouse.get_position()
    print(pos)
    while not keyboard.is_pressed('q'):
        mouse.move(pos[0], pos[1], absolute=True, duration=0)
        # print('continue')


def mouse_lock_2():
    input("Start mouse lock.", type_time_interval)
    input("Press 'q' to quit.", type_time_interval)
    ok = windll.user32.BlockInput(True)  # enable block
    while not keyboard.is_pressed('q'):
        pass
    ok = windll.user32.BlockInput(False)  # disable block

    # https://stackoverflow.com/questions/7529991/disable-or-lock-mouse-and-keyboard-in-python


if __name__ == '__main__':
    start(type_time_interval)
    mouse_lock_2()
    end(type_time_interval)
