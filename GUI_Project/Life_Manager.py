"""
COMP.CS.100 Programming 1
Life Manager program to track good habits.
Name:   Jani Ollenberg
Student ID: H288244
"""
from os import error
from tkinter import *
from datetime import datetime, timedelta
import winsound

# Import classes I've created
from Excercise import Excercise
import Select_User

class GUI:
    def __init__(self, user_data, username):
        self.__mainWindow = Tk()
        self.__mainWindow.title("Life Manager")
        self.__mainWindow.option_add("*Font", "Verdana 30")

        self.__user_data = user_data
        # print(self.__user_data)
        self.__username = username

        self.__timer = Timer()

        self.__clock = Label(self.__mainWindow)
        self.__clock.grid()

        self.__work_timer_label = Label(self.__mainWindow,
                                        text="Work Timer")
        self.__work_timer_label.grid()
        self.__work_timer_button = Button(self.__mainWindow,
                                          text="Start",
                                          command=self.start_timer,
                                          fg="#000fff000")
        self.__work_timer_button.grid()

        self.__current_timer_label = Label(self.__mainWindow,
                                           text="0:00:00.00000")
        self.__current_timer_label.grid(row=2, column=1)

        self.__work_timer_stop = Button(self.__mainWindow, text="Stop",
                                        command=self.stop_timer,
                                        fg="red",
                                        state=DISABLED)
        self.__work_timer_stop.grid()

        self.__todays_working_time_label = Label(self.__mainWindow,
                                                 text="Total Work Time Today:")
        self.__todays_working_time_label.grid(row=4, column=0)

        self.__cumulative_time_label = Label(self.__mainWindow)
        self.__cumulative_time_label.grid(row=4, column=1)

        # Excercising
        self.__excercise_label = Label(text="Excercise:")
        self.__excercise_label.grid(row=5, rowspan=4, column=0)
        
        self.__pushups = Excercise("pushups")
        self.__pushups_label = Button(text="Pushups", command=self.add_pushups)
        # self.__pushups_entry = Entry()
        # self.__pushups_label = Button(text="Pushups", command=self.__pushups.add(self))
        self.__pushups_label.grid(row=6, column=1)
        self.__pushups_entry = Entry()
        self.__pushups_entry.grid(row=6, column=2)
        self.__pushups_total_today = Label(text=self.__pushups.get_todays_total(user_data))
        self.__pushups_total_today.grid(row=6, column=3)

        self.__pullups = Excercise("pullups")
        self.__pullups_label = Button(text="Pullups", command=self.add_pullups)
        self.__pullups_label.grid(row=7, column=1)
        self.__pullups_entry = Entry()
        self.__pullups_entry.grid(row=7, column=2)
        self.__pullups_total_today = Label(text=self.__pullups.get_todays_total(user_data))
        self.__pullups_total_today.grid(row=7, column=3)

        self.__squats = Excercise("squats")
        self.__squats_label = Button(text="Squats", command=self.add_squats)
        self.__squats_label.grid(row=8, column=1)
        self.__squats_entry = Entry()
        self.__squats_entry.grid(row=8, column=2)
        self.__squats_total_today = Label(text=self.__squats.get_todays_total(user_data))
        self.__squats_total_today.grid(row=8, column=3)

        # self.__cumulative_time = timedelta(0)
        self.__cumulative_time = self.get_todays_cumulative()
        # "error" returned if daily timer is over 24hrs
        if self.__cumulative_time == "error":
            self.__cumulative_time_label["text"] = "Error in work timer, fix logs."

        self.clock()
        self.current_timer()
        self.todays_working_time()
        self.__mainWindow.mainloop()

    def get_todays_cumulative(self):
        cumulative_timer = timedelta(0)
        for event in self.__user_data:
            if event[1] == "cumulative_timer":
                day = event[0]
                day = day.split(" ")
                if day[0] == datetime.today().strftime('%Y-%m-%d'):
                    timer_delta = event[2].split(":")
                    hours = timer_delta[0]
                    minutes = timer_delta[1]
                    seconds, microseconds = timer_delta[2].split(".")
                    try:
                        cumulative_timer = timedelta(hours=int(hours),
                                            minutes=int(minutes),
                                            seconds=int(seconds), 
                                            microseconds=int(microseconds))
                    except:
                        return "error"
        return cumulative_timer

    def write_data(self, data_type, data, time=0):
        if time == 0:
            time = datetime.now()
        file = open(self.__username+"_data.txt", mode="a")
        file.write("\n")
        file.write(str(time)+';')
        file.write(str(data_type)+';')
        file.write(str(data))
        file.close()

    def clock(self):
        self.__clock.configure(text=datetime.now())
        self.__clock.after(1, self.clock)

    def current_timer(self):
        if self.__timer.is_running():
            self.__current_timer_label.configure(text=self.__timer.get_running_time())
            if self.__timer.get_running_time() > timedelta(minutes=25):
                winsound.PlaySound("ringer_alarm.wav", winsound.SND_FILENAME)
        self.__current_timer_label.after(10, self.current_timer)

    def start_timer(self):
        start_time = datetime.now()
        self.__work_timer_label.configure(text=start_time)
        self.__work_timer_button.configure(state=DISABLED)
        self.__timer = Timer(start_time)
        self.__work_timer_stop["state"] = NORMAL

    def stop_timer(self):
        if self.__timer.is_running():
            self.__work_timer_button.configure(state=NORMAL)
            self.__work_timer_stop["state"] = DISABLED
            self.__timer.stop()
            time_now = datetime.now()

            # test for midnight
            # seems to work fine
            # time_now = datetime.now() + timedelta(days=1)
            # print(time_now)

            time_difference = time_now - self.__timer.get_start_time()

            # splice timer at midnight
            if time_now.strftime('%Y-%m-%d') !=\
                    self.__timer.get_start_time().strftime('%Y-%m-%d'):

                print("Timer started yesterday. Fixing logs.")

                midnight = datetime(year=time_now.year,
                                    month=time_now.month,
                                    day=time_now.day,
                                    hour=0, minute=0, second=0, microsecond=0)
                print(time_now - midnight)
                midnight_next = datetime(year=time_now.year,
                                        month=time_now.month,
                                        day=time_now.day+1,
                                        hour=0, minute=0,
                                        second=0, microsecond=0)
                print("until midnight:", midnight_next - time_now)
                midnight_yesterday = datetime(year=time_now.year,
                                month=time_now.month,
                                day=time_now.day-1,
                                hour=23, minute=59, second=59,
                                microsecond=999999)

                # record timer until midnight for yesterday
                time_to_midnight = midnight_yesterday -\
                                         self.__timer.get_start_time()
                self.__cumulative_time += time_to_midnight
                self.__user_data.append([midnight_yesterday,
                                         "cumulative_timer",
                                         self.__cumulative_time])            
                self.write_data("cumulative_timer",
                                self.__cumulative_time,
                                midnight_yesterday)

                # record timer from midnight
                time_from_midnight = time_now - midnight
                self.__cumulative_time = time_from_midnight
                self.__user_data.append([time_now,
                                         "cumulative_timer",
                                         time_from_midnight])
                self.write_data("cumulative_timer", time_from_midnight)
                return

            # use this if midnight wasn't during the timer run
            self.__cumulative_time += time_difference
            self.__cumulative_time_label["text"] = self.__cumulative_time
            self.__user_data.append([time_now,
                                     "cumulative_timer",
                                     self.__cumulative_time])
            self.write_data("cumulative_timer", self.__cumulative_time)
            return
    
    def todays_working_time(self):
        if self.__timer.is_running():
            timer = self.__cumulative_time + self.__timer.get_running_time()
        else: timer = self.__cumulative_time
        self.__cumulative_time_label["text"] = timer
        self.__cumulative_time_label.after(10, self.todays_working_time)

    def add_pushups(self):
        try:
            amount = int(self.__pushups_entry.get())
        except:
            self.__pushups_entry.delete(0, END)
            self.__pushups_entry.insert(0,"Enter amount")
            return
        self.write_data("pushups", amount)
        self.__user_data = read_data(self.__username)
        self.__pushups_total_today["text"] = self.__pushups.\
                                             get_todays_total(self.__user_data)
    
    def add_pullups(self):
        try:
            amount = int(self.__pullups_entry.get())
        except:
            self.__pullups_entry.delete(0, END)
            self.__pullups_entry.insert(0, "+-number")
            return
        self.write_data("pullups", amount)
        self.__user_data = read_data(self.__username)
        self.__pullups_total_today["text"] = self.__pullups.\
                                             get_todays_total(self.__user_data)
    
    def add_squats(self):
        try:
            amount = int(self.__squats_entry.get())
        except:
            self.__squats_entry.delete(0, END)
            self.__squats_entry.insert(0, "+-number")
            return
        self.write_data("squats", amount)
        self.__user_data = read_data(self.__username)
        self.__squats_total_today.configure(text=self.__squats.\
                                             get_todays_total(self.__user_data))
        
    def get_pushups_entry(self):
        return self.__pushups_entry.get()
          
class Timer:
    def __init__(self, start_time=0):
        if start_time == 0:
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
    
    def get_running_time(self):
        if self.is_running():
            return datetime.now() - self.__start_time
        else:
            return "Timer not running."

def select_user():
    user = Select_User.Select_user_GUI()
    return user.get_user()

def read_data(username):
    data = open(username + "_data.txt", mode="r")
    data_lines = data.readlines()
    data.close()
    data_list = []
    for line in data_lines:
        # print(line)
        line = line.rstrip()
        recorded_event = line.split(";")
        data_list.append(recorded_event)
    return data_list

def main():
    username = select_user()
    print(username)
    user_data = read_data(username)
    GUI(user_data, username)

if __name__ == "__main__":
    main()