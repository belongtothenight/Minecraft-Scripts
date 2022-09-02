from time import sleep
from os import system
import keyboard
from timeit import default_timer

# Switch gametime automatically to get best video
'''Default Variables'''
maximum_time = 24000
type_time_interval = 0.1
initial_time = 0
'''Adjustable Variables'''
time_interval = 500
auto_switch_time_interval = 2


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


def switch_time_manual(add, time, interval_time):
    input("Start manual time switching.", type_time_interval)
    input("Press 'q' to quit.", type_time_interval)
    input("Press 'n' to advance.", type_time_interval)
    while True:
        if keyboard.is_pressed('q'):
            end(type_time_interval)
        while keyboard.is_pressed('n'):
            time += add
            print(time)
            if time > maximum_time:
                time = time - maximum_time
            cmd1 = 'gametime set ' + str(time)
            cmd2 = '/time set ' + str(time)
            input(cmd1, interval_time)
            input(cmd2, interval_time)


def switch_time_auto(add, time, interval_time_1, interval_time_2):
    input("Start automatic time switching.", type_time_interval)
    while True:
        time += add
        if time > maximum_time:
            time = time - maximum_time
        cmd1 = 'gametime set ' + str(time)
        cmd2 = '/time set ' + str(time)
        input(cmd1, interval_time_1)
        input(cmd2, interval_time_1)
        start = default_timer()
        while True:
            stop = default_timer()
            if (stop - start) > interval_time_2:
                break
            if keyboard.is_pressed('q'):
                end(type_time_interval)


def entrance():
    input("Press '1' to switch time manually.", type_time_interval)
    input("Press '2' to switch time automatically.", type_time_interval)
    while True:
        if keyboard.is_pressed('1'):
            switch_time_manual(time_interval, initial_time, type_time_interval)
        if keyboard.is_pressed('2'):
            switch_time_auto(time_interval, initial_time,
                             type_time_interval, auto_switch_time_interval)


if __name__ == '__main__':
    start(type_time_interval)
    # switch_time_manual(time_interval, initial_time, type_time_interval)
    # switch_time_auto(time_interval, initial_time, type_time_interval, 2)
    entrance()
    end(type_time_interval)
