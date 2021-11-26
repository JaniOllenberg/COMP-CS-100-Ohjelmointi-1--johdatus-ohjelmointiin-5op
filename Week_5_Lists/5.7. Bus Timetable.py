"""
COMP.CS.100 Programming 1
5.7. Ask for time and print 3 next bus times.
Jani Ollenberg
H288244
"""

def main():
    next_bus_index = 0
    bus_timetable = [630, 1015, 1415, 1620, 1720, 2000]
    current_time = int(input("Enter the time (as an integer): "))
    print("The next buses leave: ")
    index = -1
    for time in bus_timetable:
        index += 1
        if time >= current_time:
            next_bus_index = index
            break
    print_this_many_next_times = 3
    for i in range(0,print_this_many_next_times):
        print(bus_timetable[next_bus_index])
        if next_bus_index < 5:
            next_bus_index += 1
        else:
            next_bus_index = 0
            
if __name__ == "__main__":
    main()