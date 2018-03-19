import curses
from curses import wrapper
from battery_funcs import list_battery_dirs, battery_level, get_info


def main(stdscr):
    # Scanning for BATx directories
    dir = "/sys/class/power_supply/"
    bat_results = list_battery_dirs(dir)
    
    ### File Locations ###
    # Currently only pulling info from first BATx directory
    info_dir = "/sys/class/power_supply/" + bat_results[0] + "/"
    art_file = "battery_ascii"
    
    ### Creating color pairs ###
    # Battery outline
    curses.init_pair(1, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    
    # Charge level
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
    
    # Drawing the battery
    with open(art_file, 'r') as art:
        for line in art.readlines():
            stdscr.addstr(line, curses.color_pair(1))
   
    battery_bars = battery_level(info_dir)
    for y in range(battery_bars, 13):
        stdscr.addstr(y, 3, "/////////////", curses.color_pair(2))

    # Iterating through lines in file, searching for matching phrase
    info_fields, info_values = get_info(info_dir)
    for x in range(len(info_fields)):
        stdscr.addstr(x + 5, 23, info_fields[x] + ":", curses.A_BOLD)
        stdscr.addstr(x + 5, 53, info_values[x], curses.A_BOLD)
    
    # Wait for key press before clearing screen
    stdscr.getkey()

wrapper(main)
