from time import sleep
from os import system
import keyboard

# Ouo_shrine_remove_above_above_ground_blocks

sakura_forest = [
    'pink_wool',
    'white_wool',
    'snow',
    'pink_stained_glass',
    'pink_stained_glass_pane',
    'white_stained_glass',
    'white_stained_glass_pane',
    'spruce_log',
    'spruce_wood',
    'spruce_leaves',
    'spruce_fence',
    'dark_oak_fence',
]

flower = [
    'oxeye_daisy',
    'poppy',
    'red_tulip',
    'orange_tulip',
    'cornflower',
    'blue_orchid',
    'allium',
    'pink_tulip',
    'lily_of_the_valley',
    'white_tulip',
    'dandelion',
    'grass',
    'tall_grass',
    'rose_bush',
    'peony',
    'lilac',
]


def input(command, time):
    keyboard.press_and_release('t')
    sleep(time)
    keyboard.write(command)
    sleep(time)
    keyboard.press_and_release('enter')
    sleep(time)


def wait_for_enter(time):
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
    sleep(0.1)


'''splittPress'''


def replace_air(block, time):
    if keyboard.is_pressed('q'):
        exit()
    for element in block:
        input(element + ' ==>air', time)
        input('//replace ' + element + ' air', time)


if __name__ == '__main__':
    wait_for_enter(0.1)
    replace_air(sakura_forest, 0.1)
    replace_air(flower, 0.1)
    end(0.1)
