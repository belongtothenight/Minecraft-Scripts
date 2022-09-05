from time import sleep
from os import system, startfile, remove
from os.path import exists, abspath
from time import sleep
from time import time as tt
from sys import exit, argv
from tkinter.filedialog import askdirectory
import win32comext.shell.shell as shell
import keyboard

# Switch gametime automatically to get best video
'''Default Variables'''
ASADMIN = 'asadmin'
maximum_time = 24000
type_time_interval = 0.1  # to prevent error input to Minecraft
loop_time_interval = 0.1  # to prevent laggy control and even freeze
initial_time = 0
recording_buff_length = 6  # seconds
overtime = 20  # seconds
video_path_file = 'Time_Selection_Recording-video_path.txt'
video_path = r'%USERPROFILE%\\Videos\\Minecraft'

'''Adjustable Variables'''
time_interval = 500  # minecraft gametime
auto_switch_time_interval = 2  # seconds
max_recording_length = 180  # seconds (default 180)


class runSingle:
    # https://stackoverflow.com/questions/61219355/prevent-my-python-script-to-be-executed-twice-at-same-time
    def __init__(self, fileName) -> None:
        with open(fileName, "w") as self.f:
            pass
        self.f.close()
        try:
            remove(fileName)
            self.f = open(fileName, "w")
        except WindowsError:
            exit()


def input(command, time):
    keyboard.press_and_release('t')
    sleep(time)
    keyboard.write(command)
    sleep(time)
    keyboard.press_and_release('enter')
    sleep(time)


def start():
    a = runSingle("Time_Selection_Recording-single_run_check-safe_to_delete")
    system('cls')
    sleep(3)
    keyboard.press_and_release('f3+d')
    input('Press enter to continue.', type_time_interval)
    while not keyboard.is_pressed('enter'):
        sleep(loop_time_interval)
        pass
    input('Start execution.', type_time_interval)
    input('Gameruls need to be set before execution.', type_time_interval)
    input("Press 'q' to quit.", type_time_interval)


def end():
    input('/kill @e[type=item]', type_time_interval)
    input('Finished execution.', type_time_interval)
    try:
        f = open(video_path_file, 'r', encoding='utf-8')
        video_path = f.read()
        f.close()
    except:
        video_path = r'%USERPROFILE%\\Videos'
    startfile(video_path)
    exit()


def clear_hotbar():
    input('Make sure hotbar slot 1 and 2 are empty.', type_time_interval)
    sleep(type_time_interval*5)
    input("Clearing hotbar.", type_time_interval)
    keyboard.press_and_release('1')
    keyboard.press_and_release('q')
    keyboard.press_and_release('2')
    keyboard.press_and_release('q')
    input('/kill @e[type=item]', type_time_interval)
    input("Finished clearing hotbar.", type_time_interval)


def switch_time_manual(add, time, interval_time):
    input("Start manual time switching.", type_time_interval)
    input("Press 'n' to advance.", type_time_interval)
    input("Press 'enter' to record video.", type_time_interval)
    input("Press 'q' to quit.", type_time_interval)
    start = tt()
    while True:
        sleep(loop_time_interval)
        stop = tt()
        if (stop - start) > overtime * (maximum_time / time_interval) * 0.25:
            input("Overtime, exiting.", type_time_interval)
            end()
        if keyboard.is_pressed('n'):
            time += add
            print(time)
            if time > maximum_time:
                time = time - maximum_time
            cmd1 = 'gametime set ' + str(time)
            cmd2 = '/time set ' + str(time)
            input(cmd1, interval_time)
            input(cmd2, interval_time)
        if keyboard.is_pressed('enter'):
            break
        if keyboard.is_pressed('q'):
            end()


def switch_time_auto(add, time, interval_time_1, interval_time_2):
    input("Start automatic time switching.", type_time_interval)
    input("Press 'enter' to record video.", type_time_interval)
    input("Press 'q' to quit.", type_time_interval)
    start1 = tt()
    limit = overtime * (maximum_time / time_interval) * 0.25
    while True:
        sleep(loop_time_interval)
        stop1 = tt()
        if (stop1 - start1) > limit:
            input("Overtime, exiting.", type_time_interval)
            end()
        time += add
        if time > maximum_time:
            time = time - maximum_time
        cmd1 = 'gametime set ' + str(time)
        cmd2 = '/time set ' + str(time)
        input(cmd1, interval_time_1)
        input(cmd2, interval_time_1)
        start2 = tt()
        while True:
            sleep(loop_time_interval)
            stop2 = tt()
            if (stop2 - start2) > interval_time_2:
                break
            if keyboard.is_pressed('enter'):
                return
            if keyboard.is_pressed('q'):
                end()


def time_switch():
    input("Press '1' to switch time manually.", type_time_interval)
    input("Press '2' to switch time automatically.", type_time_interval)
    input("Press 'enter' to record video.", type_time_interval)
    input("Press 'q' to quit.", type_time_interval)
    input("Decide filming angle before next step.", type_time_interval)
    start = tt()
    while True:
        sleep(loop_time_interval)
        stop = tt()
        if (stop - start) > overtime:
            input("Overtime, exiting.", type_time_interval)
            end()
        if keyboard.is_pressed('1'):
            switch_time_manual(time_interval, initial_time, type_time_interval)
        if keyboard.is_pressed('2'):
            switch_time_auto(time_interval, initial_time,
                             type_time_interval, auto_switch_time_interval)
        if keyboard.is_pressed('enter'):
            break
        if keyboard.is_pressed('q'):
            end()


def record():
    if exists(video_path_file):
        pass
    else:
        video_path = askdirectory()
        f = open(video_path_file, 'w', encoding='utf-8')
        f.write(video_path)
        f.close()
    line = "Start recording for {} seconds.".format(max_recording_length)
    input(line, type_time_interval)
    input("Make sure it's currently in FullScreen Mode.", type_time_interval)
    input("Press 'q' to quit.", type_time_interval)
    sleep(1)
    input("/gamemode spectator", type_time_interval)
    keyboard.press_and_release('`')
    keyboard.press_and_release('f1')
    keyboard.press_and_release('alt+f9')
    start = tt()
    while not keyboard.is_pressed('q'):
        sleep(loop_time_interval)
        end = tt()
        time = end - start
        if time >= recording_buff_length + max_recording_length:
            keyboard.press_and_release('alt+f9')
            keyboard.press_and_release('f1')
            keyboard.press_and_release('`')
            break
    keyboard.press_and_release('alt+f9')
    keyboard.press_and_release('f1')
    keyboard.press_and_release('`')
    input("Recording time: " + str(time), type_time_interval)
    input("Stopped recording.", type_time_interval)
    input("/gamemode creative", type_time_interval)
    input("/data get entity @s Pos", type_time_interval)


if __name__ == '__main__':
    start()
    clear_hotbar()
    input("Press 'q' to quit.", type_time_interval)
    while True:
        sleep(loop_time_interval)
        time_switch()
        record()
        if keyboard.is_pressed('q'):
            break
    end()
