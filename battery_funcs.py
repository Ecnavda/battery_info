from os import listdir

def list_battery_dirs(dir):
    bats = []
    for x in listdir(dir):
        if "BAT" in x:
            bats.append(x)

    return bats

def battery_level(dir):
    # Default Value
    batter_bars = 2
    
    #Returning number of lines to skip before drawing bars
    with open(dir + "capacity", 'r') as battery_capacity:
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

    return battery_bars

def get_info(dir): 
    match_list = ["SUPPLY NAME","TECHNOLOGY","CAPACITY","SUPPLY MODEL","MANUFACTURER","SERIAL"]
    info_fields = []
    info_values = []
    with open(dir + "uevent", 'r') as uevent_file:
        count = 0
        for line in uevent_file.readlines(): 
            line = line.replace("_", " ")
            line = line.split("=")
            if match_list[count] in line[0]:
                info_fields.append(line[0])
                info_values.append(line[1])
                count += 1
    return info_fields, info_values

if __name__ == "__main__":
    print(list_battery("/sys/class/power_supply"))
    print(battery_level("/sys/class/power_supply/BAT1/"))
