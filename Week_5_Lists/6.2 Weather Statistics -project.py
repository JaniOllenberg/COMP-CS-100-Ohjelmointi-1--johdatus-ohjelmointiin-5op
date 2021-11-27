"""
COMP.CS.100 Programming 1
6.2 Project to keep stats of weather and compare them to mean temperature.
Jani Ollenberg
H288244
"""

def get_temperatures():
    """
    Ask how many days and get temp for every day.
    :param: no parameters
    :return: list of daily temperatures
    """
    temperatures = []
    days_to_stat = int(input("Enter amount of days: "))
    for i in range(1, days_to_stat+1):
        temperature = float(input(f"Enter day {i}. temperature in Celcius: "))
        temperatures.append(temperature)
    return temperatures

def calculate_mean(temperatures):
    """
    Calculate average of the temperatures in list.
    :param: list of temperatures
    :return: average aka mean
    """
    sum = 0
    for i in temperatures:
        sum += i
    return sum / len(temperatures)

def calculate_median(temperatures):
    """
    Calculates median of daily temperatures list.
    :param: list of temperatures
    :return: calculated median
    """
    sorted_temperatures = sorted(temperatures)
    if len(sorted_temperatures) % 2 != 0:
        middle_index = len(sorted_temperatures) // 2
        median = sorted_temperatures[middle_index]
    else:
        middle_index = len(sorted_temperatures) // 2 -1
        median = (sorted_temperatures[middle_index]
         + sorted_temperatures[middle_index+1] ) / 2
    return median

def print_over_mean(temperatures, median, mean):
    """
    Print days that were over or at median temperature.
    :param: list of temps and median and mean temperature
    :return: no need for return
    """
    print("Over or at median were: ")
    day_index = 0
    for temperature in temperatures:
        day_index += 1
        if temperature >= median:
            difference_to_mean = temperature - mean
            print(f"Day {day_index:2d}. {temperature:5.1f}C \
difference to mean: {difference_to_mean:5.1f}C")

def print_under_mean(temperatures, median, mean):
    """
    Print days that were under median temperature.
    :param: list of temps and median and mean temperature
    :return: no need for return
    """
    print("Under median were: ")
    day_index = 0
    for temperature in temperatures:
        day_index += 1
        if temperature < median:
            difference_to_mean = temperature - mean
            print(f"Day {day_index:2d}. {temperature:5.1f}C \
difference to mean: {difference_to_mean:5.1f}C")

def main():
    list_of_temperatures = get_temperatures()
    # print(list_of_temperatures)
    print()
    mean = calculate_mean(list_of_temperatures)
    print(f"Temperature mean: {mean:.1f}C")
    median = calculate_median(list_of_temperatures)
    print(f"Temperature median: {median:.1f}C")
    print()
    print_over_mean(list_of_temperatures, median, mean)
    print()
    print_under_mean(list_of_temperatures, median, mean)

if __name__ == "__main__":
    main()