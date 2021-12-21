"""
COMP.CS.100 Programming 1
Life Manager program to track good habits.
Name:   Jani Ollenberg
Student ID: H288244
"""
from tkinter import *
from datetime import datetime, timedelta

class GUI:
    def __init__(self):
        self.__mainWindow = Tk()
        self.__mainWindow.title("Life Manager")
        self.__mainWindow.option_add("*Font", "Verdana 30")

        self.__timer = Timer()
        self.__work_timer_button = Button(self.__mainWindow,
                                          text="Work Timer",
                                          command=self.start_timer)
        self.__work_timer_button.grid()
        self.__work_timer_label = Label(self.__mainWindow,
                                        text=datetime.now())
        self.__work_timer_label.grid()

        self.__cumulative_time_label = Label(self.__mainWindow)
        self.__cumulative_time_label.grid()
        self.__cumulative_time = timedelta(0)

        self.__mainWindow.mainloop()

    def start_timer(self):
        if self.__timer.is_running():
            self.__work_timer_button.configure(text="Start Timer",
                                               fg="#000fff000")
            self.__timer.stop()

            time_difference = datetime.now() - self.__timer.get_start_time()
            self.__cumulative_time += time_difference
            self.__cumulative_time_label["text"] = self.__cumulative_time
            return
        start_time = datetime.now()
        self.__work_timer_label.configure(text=start_time)
        self.__work_timer_button.configure(text="Stop Timer", fg="red")
        self.__timer = Timer(start_time)

class Timer:
    def __init__(self, start_time=0):
        if start_time == 0:
            print(start_time)
            self.__is_running = False
        else:
            self.start(start_time)
    
    def is_running(self):
        return self.__is_running
    
    def start(self, start_time):
        self.__is_running = True
        self.__start_time = start_time
        
    def stop(self):
        self.__is_running = False

    def get_start_time(self):
        return self.__start_time 
    
def main():
    GUI()

if __name__ == "__main__":
    main()