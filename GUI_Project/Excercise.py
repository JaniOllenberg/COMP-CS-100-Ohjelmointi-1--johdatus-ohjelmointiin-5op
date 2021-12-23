"""
COMP.CS.100 Programming 1
Excercise class for Life Manager
Jani Ollenberg
H288244
"""

from datetime import datetime


class Excercise:
    def __init__(self, excercise_type):
        self.__excercise_type = excercise_type

    def get_todays_total(self, data):
        sum = 0
        for line in data:
            try:
                if line[1] == self.__excercise_type:
                    day = line[0].split(" ")
                    if day[0] == datetime.today().strftime("%Y-%m-%d"):
                        sum += int(line[2])
            except:
                sum = "error"
        return sum

    # def add(self, gui):
    #     amount = gui.get_pushups_entry()
    #     print(amount)