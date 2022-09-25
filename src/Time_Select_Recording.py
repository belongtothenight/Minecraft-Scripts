from multiprocessing.resource_sharer import stop
from time import sleep
from os import system, startfile, remove
from os.path import exists
from time import sleep
from time import time as tt
from sys import exit
from tkinter.filedialog import askdirectory
from pynput.mouse import Controller
import keyboard

# Switch gametime automatically to get best video
'''Default Variables'''
ASADMIN = 'asadmin'
maximum_time = 24000
initial_time = 0
video_path_file = 'Time_Select_Recording-video_path.txt'
instance_check_file = 'Time_Select_Recording-single_run_check-safe_to_delete'
video_path = r'%USERPROFILE%\Videos\Minecraft'

'''Adjustable Variables'''
type_time_interval = 0.1  # to prevent error input to Minecraft
loop_time_interval = 0.1  # to prevent laggy control and even freeze
recording_buff_length = 6  # seconds
overtime = 120  # seconds
time_interval = 250  # minecraft gametime
auto_switch_time_interval = 1.5  # seconds
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
    a = runSingle(instance_check_file)
    system('cls')
    sleep(3)
    keyboard.press_and_release('f3+d')
    input('Press enter to continue.', type_time_interval)
    while not keyboard.is_pressed('enter'):
        sleep(loop_time_interval)
        pass
    input('Start execution.', type_time_interval)
    input('Gameruls need to be set before execution.', type_time_interval)
    input("Press 'shift+q' to quit.", type_time_interval)
    input("Press 'q' to skip.", type_time_interval)


def end():
    input('/kill @e[type=item]', type_time_interval)
    input('Finished execution.', type_time_interval)
    try:
        f = open(video_path_file, 'r', encoding='utf-8')
        video_path = f.read()
        f.close()
    except:
        video_path = r'%USERPROFILE%\Videos'
    try:
        startfile(video_path)
    except:
        pass
    # system('cmd /k')
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
    start = tt()
    while True:
        sleep(loop_time_interval)
        stop = tt()
        if (stop - start) > overtime * (maximum_time / time_interval):
            del start, stop
            input("Overtime, exiting.", type_time_interval)
            end()
        if keyboard.is_pressed('n'):
            time += add
            if time > maximum_time:
                time = time - maximum_time
            cmd1 = 'gametime set ' + str(time)
            cmd2 = '/time set ' + str(time)
            input(cmd1, interval_time)
            input(cmd2, interval_time)
        if keyboard.is_pressed('enter'):
            break
        if keyboard.is_pressed('shift+q'):
            end()
        if keyboard.is_pressed('q'):
            break


def switch_time_auto(add, time, interval_time_1, interval_time_2):
    input("Start automatic time switching.", type_time_interval)
    input("Press 'enter' to record video.", type_time_interval)
    start1 = tt()
    limit = overtime * (maximum_time / time_interval)
    while True:
        sleep(loop_time_interval)
        stop1 = tt()
        if (stop1 - start1) > limit:
            del start1, stop1
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
                del start2, stop2
                break
            if keyboard.is_pressed('enter'):
                return
            if keyboard.is_pressed('shift+q'):
                end()
            if keyboard.is_pressed('q'):
                return


def time_switch():
    input("Press '1' to switch time manually.", type_time_interval)
    input("Press '2' to switch time automatically.", type_time_interval)
    input("Press 'enter' to record video.", type_time_interval)
    input("Press 'shift+q' to quit.", type_time_interval)
    input("Press 'q' to skip.", type_time_interval)
    input("Decide filming angle before next step.", type_time_interval)
    start = tt()
    while True:
        sleep(loop_time_interval)
        stop = tt()
        if (stop - start) > overtime:
            del start, stop
            input("Overtime, exiting.", type_time_interval)
            end()
        if keyboard.is_pressed('1'):
            switch_time_manual(time_interval, initial_time, type_time_interval)
        if keyboard.is_pressed('2'):
            switch_time_auto(time_interval, initial_time,
                             type_time_interval, auto_switch_time_interval)
        if keyboard.is_pressed('enter'):
            break
        if keyboard.is_pressed('shift+q'):
            end()
        if keyboard.is_pressed('q'):
            input("Press 'enter' to record video.", type_time_interval)
            input("Press 'shift+q' to quit.", type_time_interval)
            while True:
                if keyboard.is_pressed('enter'):
                    break
                if keyboard.is_pressed('shift+q'):
                    end()


def record():
    def start_record():
        keyboard.press_and_release('`')
        keyboard.press_and_release('f1')
        keyboard.press_and_release('alt+f9')
        mouse = Controller()
        mouse.scroll(0, -8)

    def stop_record():
        keyboard.press_and_release('alt+f9')
        keyboard.press_and_release('f1')
        keyboard.press_and_release('`')
        sleep(type_time_interval*20)
        input("Recording time: " + str(time), type_time_interval)
        input("Stopped recording.", type_time_interval)
        input("/gamemode creative", type_time_interval)
        input("/data get entity @s Pos", type_time_interval)
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
    sleep(type_time_interval*10)
    input("/gamemode spectator", type_time_interval)
    start_record()
    start = tt()
    while not keyboard.is_pressed('q'):
        sleep(loop_time_interval)
        stop = tt()
        time = stop - start
        if keyboard.is_pressed('shift+q'):
            stop_record()
            del start, stop
            end()
        if time >= recording_buff_length + max_recording_length:
            stop_record()
            return


if __name__ == '__main__':
    start()
    clear_hotbar()
    input("Press 'shift+q' to quit.", type_time_interval)
    while True:
        sleep(loop_time_interval)
        time_switch()
        record()
        if keyboard.is_pressed('shift+q'):
            break
    end()
