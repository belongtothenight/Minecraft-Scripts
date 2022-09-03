from os import system
from time import sleep
import keyboard
import mouse
import pyperclip
from timeit import default_timer
system('cls')


type_time_interval = 0.1
recording_buff_length = 5  # seconds
max_recording_length = 0  # 180  # seconds


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


def record():
    input("Start recording.", type_time_interval)
    input("Make sure it's currently in FullScreen Mode.", type_time_interval)
    input("Press 'q' to quit.", type_time_interval)
    sleep(1)
    keyboard.press_and_release('f1')
    keyboard.press_and_release('alt+f9')
    start = default_timer()
    while not keyboard.is_pressed('q'):
        end = default_timer()
        time = end - start
        if time >= recording_buff_length + max_recording_length:
            input(str(time), type_time_interval)
            break
    keyboard.press_and_release('alt+f9')
    input("Stop recording.", type_time_interval)
    input("/data get entity @s Pos", type_time_interval)
    keyboard.press_and_release('f1')

    # https://stackoverflow.com/questions/7529991/disable-or-lock-mouse-and-keyboard-in-python


if __name__ == '__main__':
    start(type_time_interval)
    record()
    end(type_time_interval)
