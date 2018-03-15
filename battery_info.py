import os.path
import curses
from curses import wrapper


def main(stdscr):
    # Location of Battery Info
    BAT = "BAT0"
    if os.path.isdir("/sys/class/power_supply/" + BAT):
        pass
    else:
        BAT = "BAT1"
    ### File Locations ###
    info_dir = "/sys/class/power_supply/" + BAT + "/"
    info_file = info_dir + "uevent"
    capacity_file = info_dir + "capacity"
    art_file = "battery_ascii"
    match_list = ["SUPPLY NAME","TECHNOLOGY","CAPACITY","SUPPLY MODEL","MANUFACTURER","SERIAL"]
    ### Creating color pairs ###
    # Battery outline
    curses.init_pair(1, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    # Charge level
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
    # Drawing the battery
    with open(art_file, 'r') as art:
        for line in art.readlines():
            stdscr.addstr(line, curses.color_pair(1))
    
    # Drawing battery charge level
    battery_bars = 2
    
    with open(capacity_file, 'r') as battery_capacity:
        battery_capacity = int(battery_capacity.readline())
        if battery_capacity >= 90:
            battery_bars = 2
        elif 89 >= battery_capacity >= 80:
            battery_bars = 4
        elif 79 >= battery_capacity >= 70:
            battery_bars = 5
        elif 69 >= battery_capacity >= 60:
            battery_bars = 6
        elif 59 >= battery_capacity >= 50:
            battery_bars = 7
        elif 49 >= battery_capacity >= 40:
            battery_bars = 8
        elif 39 >= battery_capacity >= 30:
            battery_bars = 9
        elif 29 >= battery_capacity >= 20:
            battery_bars = 10
        elif 19 >= battery_capacity >= 10:
            battery_bars = 11
        elif 9 >= battery_capacity >= 0:
            battery_bars = 12
    
    for y in range(battery_bars, 13):
        stdscr.addstr(y, 3, "/////////////", curses.color_pair(2))

    # Iterating through lines in file, searching for matching phrase
    with open(info_file, 'r') as info:
        count = 0
        for line in info.readlines():
            line = line.replace("_", " ")
            line = line.split("=")
            if match_list[count] in line[0]:
                stdscr.addstr(count + 5, 23, line[0], curses.A_BOLD)
                stdscr.addstr(count + 5, 53, line[1], curses.A_BOLD)
                count += 1
    
    # Wait for key press before clearing screen
    stdscr.getkey()

wrapper(main)
