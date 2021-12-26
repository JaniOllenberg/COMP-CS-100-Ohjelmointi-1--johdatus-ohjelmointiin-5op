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
import threading

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

        # flags for playing alarm sound. These are needed for the sound thread.
        self.__play_alarm = False
        self.__alarm_playing = False

        self.__clock = Label(self.__mainWindow)
        self.__clock.grid(row=0, column=0)

        # Button to open minimal GUI to see timer on top of other windows
        self.__minimal_gui_button = Button(self.__mainWindow,
                                           text="Minimal GUI",
                                           command=self.minimal_GUI)
        self.__minimal_gui_button.grid(row=0,column=2)

        self.__work_timer_label = Label(self.__mainWindow,
                                        text="Work Timer")
        self.__work_timer_label.grid(row=1, column=0)

        self.__work_timer_started_label = Label(self.__mainWindow, text="0:00:00.0000")
        self.__work_timer_started_label.grid(row=1, column=1)
        
        self.__work_timer_button = Button(self.__mainWindow,
                                          text="Start",
                                          command=self.start_timer,
                                          fg="#000fff000")
        self.__work_timer_button.grid(row=2, column=0)

        self.__current_timer_label = Label(self.__mainWindow,
                                           text="0:00:00.00000")
        self.__current_timer_label.grid(row=2, column=1)

        self.__work_timer_stop = Button(self.__mainWindow, text="Stop",
                                        command=self.stop_timer,
                                        fg="red",
                                        state=DISABLED)
        self.__work_timer_stop.grid(row=3, column=0)

        self.__todays_working_time_label = Label(self.__mainWindow,
                                                 text="Total Work Time Today:")
        self.__todays_working_time_label.grid(row=4, column=0)

        self.__cumulative_time_label = Label(self.__mainWindow)
        self.__cumulative_time_label.grid(row=4, column=1)

        # break timer
        self.__break_timer = Timer()
        self.__break_timer_button = Button(text="Break Timer", command=self.break_timer)
        self.__break_timer_button.grid(row=2, column=2)
        self.__break_timer_label = Label(text="5 minutes")
        self.__break_timer_label.grid(row=3, column=2)

        self.__break_variable = IntVar()
        self.__break_variable.set(5) # default to 5 minute break time
        self.__break_5min_radiobutton = Radiobutton(self.__mainWindow,
                                                    text="5 mins",
                                                    variable=self.__break_variable,
                                                    value=5,
                                                    command=self.break_timer_length)
        self.__break_5min_radiobutton.grid(row=2, column=3)
        self.__break_15min_radiobutton = Radiobutton(self.__mainWindow,
                                                     text="15 mins",
                                                     variable=self.__break_variable,
                                                     value=15,
                                                     command=self.break_timer_length)
        self.__break_15min_radiobutton.grid(row=2, column=4)

        # Excercising
        self.__excercise_label = Label(text="Excercise:")
        self.__excercise_label.grid(row=5, rowspan=4, column=0, sticky=E)
        
        self.__excercise_added_label = Label(self.__mainWindow, text="Add +-number")
        self.__excercise_added_label.grid(row=4,column=2)

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

        # averages
        self.__averages_label = Button(text="Daily\nAverage",
                                       command=self.update_averages)
        self.__averages_label.grid(row=3, column=4)
        self.__timer_daily_average = Label(text=self.daily_average("cumulative_timer"))
        self.__timer_daily_average.grid(row=4, column=4)
        self.__pushups_daily_average = Label(text=f'{self.daily_average("pushups"):.2f}')
        self.__pushups_daily_average.grid(row=6, column=4)
        self.__pullups_daily_average = Label(text=f'{self.daily_average("pullups"):.2f}')
        self.__pullups_daily_average.grid(row=7, column=4)
        self.__squats_daily_average = Label(text=f'{self.daily_average("squats"):.2f}')
        self.__squats_daily_average.grid(row=8, column=4)

        # self.__cumulative_time = timedelta(0)
        self.__cumulative_time = self.get_todays_cumulative()
        # "error" returned if daily timer is over 24hrs
        if self.__cumulative_time == "error":
            self.__cumulative_time_label["text"] = "Error in work timer, fix logs."

        # display earned pomodoros for today
        self.__earned_pomodoros_label = Label(self.__mainWindow,
                                              text="Earned Pomodoros:")
        self.__earned_pomodoros_label.grid(row=8, column=0)
        self.__pomodoro_image = PhotoImage(file="pomodoro75pixels.png")
        self.__earned_pomodoros = self.__cumulative_time // timedelta(minutes=25)
        print(self.__earned_pomodoros)
        self.__pomodoro_label = []

        self.update_earned_pomodoros()

        self.clock()
        self.current_timer()
        self.current_break_timer()
        self.todays_working_time()
        self.__mainWindow.mainloop()
    
    def minimal_GUI(self):
        self.__minimal_GUI = Tk()
        self.__minimal_GUI.title("Minimal GUI")
        self.__minimal_GUI.option_add("*Font", "Verdana 16")
        self.__minimal_GUI.geometry("+1600+850")
        self.__minimal_timer = Label(self.__minimal_GUI, text="00:00:00.0000")
        self.__minimal_timer.pack()

        #window stays on top of everything
        self.__minimal_GUI.wm_attributes("-topmost", 1)
        # self.__minimal_GUI.resizable(False, False)
        # self.__minimal_GUI.update_idletasks()
        # self.__minimal_GUI.overrideredirect(True)
        self.minimal_GUI_timer()
        
        self.__minimal_GUI.mainloop()

    def minimal_GUI_timer(self):
        if self.__timer.is_running():
            print_timer = datetime(year=2021, month=12, day=25, hour=0, minute=0, second=0) + self.__timer.get_running_time()
            print_timer = print_timer.strftime("%M:%S")
            self.__minimal_timer.configure(text=print_timer)
            # play ringer alarm after 25mins
            # if self.__timer.get_running_time() > timedelta(minutes=0, seconds= 5):
            #     if self.__timer.is_running() and not self.__alarm_playing:
            #         if self.__play_alarm == True:
            #             thread_for_sound = threading.Thread(target=self.play_sound)
            #             thread_for_sound.start()
            #             self.__alarm_playing = True
            #     # winsound.PlaySound("ringer_alarm.wav", winsound.SND_FILENAME)
        self.__minimal_timer.after(1000, self.minimal_GUI_timer)

    def break_timer_length(self):
        self.__break_timer_length = self.__break_variable.get()
        self.__break_timer_label.configure(text=f"{self.__break_timer_length} minutes")
        
    
    def update_earned_pomodoros(self):
        self.__earned_pomodoros = self.__cumulative_time // timedelta(minutes=25)
        self.__pomodoro_label = []
        for pomodoro in range(0,self.__earned_pomodoros):
            self.__pomodoro_label.append(Label(self.__mainWindow, 
                                        image=self.__pomodoro_image))
            if pomodoro < 5:
                self.__pomodoro_label[pomodoro].grid(row=9+pomodoro, column=0)
            if 4 < pomodoro < 10:
                self.__pomodoro_label[pomodoro].grid(row=9+pomodoro-5, column=1)
            if 9 < pomodoro < 15:
                self.__pomodoro_label[pomodoro].grid(row=9+pomodoro-10, column=2)
            if 14 < pomodoro < 20:
                self.__pomodoro_label[pomodoro].grid(row=9+pomodoro-15, column=3)
            if 19 < pomodoro < 24:
                self.__pomodoro_label[pomodoro].grid(row=9+pomodoro-20, column=4)
            if pomodoro > 23:
                self.__pomodoro_label[pomodoro] = Label(self.__mainWindow,
                                                        text=f"+{pomodoro-23}")
                self.__pomodoro_label[pomodoro].grid(row=13, column=4)
        if len(self.__pomodoro_label) == 0:
            self.__pomodoro_label.append(Label(self.__mainWindow,
                                               text="No Pomodoros Earned."))
        self.__earned_pomodoros_label["text"] = f"Earned Pomodoros:     {self.__earned_pomodoros}"
        self.__earned_pomodoros_label.after(10000, self.update_earned_pomodoros)

    def break_timer(self):
        self.__play_alarm = True
        self.__break_timer.reverse_start(self.__break_variable.get())
        self.__break_timer_button.configure(text="Stop break",
                                            command=self.stop_break)

    def stop_break(self):
        self.__play_alarm = False
        self.__break_timer.stop()
        self.__break_timer_button.configure(text="Break Timer",
                                            command=self.break_timer)
        # self.__break_timer_label["text"] = "5 minutes"
    
    def update_averages(self):
        self.__timer_daily_average["text"] = self.daily_average("cumulative_timer")
        self.__pushups_daily_average["text"] = f'{self.daily_average("pushups"):.2f}'
        self.__pullups_daily_average["text"] = f'{self.daily_average("pullups"):.2f}'
        self.__squats_daily_average["text"] = f'{self.daily_average("squats"):.2f}'

    def daily_average(self, event):
        previous_day = None
        daily_sum = 0
        daily_sums_list = []
        last_cumulative_list = []
        last_cumulative = None
        number_of_new_days = 0
        for line in self.__user_data:
            day, timestamp = line[0].split(" ")
            if day != previous_day: # a new day
                previous_day = day
                number_of_new_days += 1
                if event == "cumulative_timer":
                    last_cumulative_list.append(last_cumulative)
                else:
                    daily_sums_list.append(daily_sum)
                    daily_sum = 0
            if line[1] == event:
                if event == "cumulative_timer":
                    last_cumulative = line[2]
                else:    
                    daily_sum += int(line[2])

        # calculate average from dailies list            
        last_cumulative_list.append(last_cumulative) # add last day also
        if event == "cumulative_timer":
            last_cumulative_list.pop(0)
            last_cumulative_list.pop(0) #remove the initialization line
            timedelta_list = []
            try:
                for timer in last_cumulative_list:
                    timer = str(timer)
                    hours, minutes, seconds = timer.split(":")
                    seconds, microseconds = seconds.split(".")
                    timer_timedelta = timedelta(hours=int(hours),
                                                minutes=int(minutes),
                                                seconds=int(seconds))
                    timedelta_list.append(timer_timedelta)
                return (sum(timedelta_list, timedelta()) / len(timedelta_list))
            except: return 0
        else: # for excercises
            daily_sums_list.append(daily_sum)
            daily_sums_list.pop(0)
            daily_sums_list.pop(0) # remove initilization line
            try:
                average = sum(daily_sums_list) / (number_of_new_days-1)
                return average
            except: return 0 # no data for any days

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
        self.__clock.after(1000, self.clock)

    def current_timer(self):
        if self.__timer.is_running():
            self.__current_timer_label.configure(text=self.__timer.get_running_time())
            # play ringer alarm after 25mins
            if self.__timer.get_running_time() > timedelta(minutes=25, seconds=0):
                if self.__timer.is_running() and not self.__alarm_playing:
                    if self.__play_alarm == True:
                        thread_for_sound = threading.Thread(target=self.play_sound)
                        thread_for_sound.start()
                        self.__alarm_playing = True
                # winsound.PlaySound("ringer_alarm.wav", winsound.SND_FILENAME)
        self.__current_timer_label.after(10, self.current_timer)

    def current_break_timer(self):
        if self.__break_timer.is_running():
            time_left = self.__break_timer.get_reverse_end_time() - datetime.now()
            overtime = False
            if time_left < timedelta(0):
                time_left = self.__break_timer.get_running_time()
                overtime = True
            # self.__break_timer_label.configure(text=self.__break_timer.get_running_time())
            self.__break_timer_label.configure(text=time_left, fg="green")
            if overtime == True:
                self.__break_timer_label.configure(fg="red")
            # play ringer alarm after 5mins
            if self.__break_timer.get_running_time() > timedelta(minutes=self.__break_variable.get()):
                if self.__break_timer.is_running() and not self.__alarm_playing:
                    if self.__play_alarm:
                        self.__sound_thread = threading.Thread(target=self.play_sound)
                        self.__sound_thread.start()
                        self.__alarm_playing = True
                # winsound.PlaySound("ringer_alarm.wav", winsound.SND_FILENAME)
        self.__break_timer_label.after(10, self.current_break_timer)

    def play_sound(self, filename="ringer_alarm.wav"):
        winsound.PlaySound(filename, winsound.SND_FILENAME)
        self.__alarm_playing = False
    
    def start_timer(self):
        self.__play_alarm = True
        start_time = datetime.now()
        time_to_display = start_time.strftime("%H:%M:%S")
        self.__work_timer_started_label.configure(text=time_to_display)
        self.__work_timer_button.configure(state=DISABLED)
        self.__timer = Timer(start_time)
        self.__work_timer_stop["state"] = NORMAL

    def stop_timer(self):
        self.__play_alarm = False
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
                self.__user_data.append([str(midnight_yesterday),
                                         "cumulative_timer",
                                         self.__cumulative_time])            
                self.write_data("cumulative_timer",
                                self.__cumulative_time,
                                midnight_yesterday)

                # record timer from midnight
                time_from_midnight = time_now - midnight
                self.__cumulative_time = time_from_midnight
                self.__user_data.append([str(time_now),
                                         "cumulative_timer",
                                         time_from_midnight])
                self.write_data("cumulative_timer", time_from_midnight)
                return

            # use this if midnight wasn't during the timer run
            self.__cumulative_time += time_difference
            self.__cumulative_time_label["text"] = self.__cumulative_time
            self.__user_data.append([str(time_now),
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
        self.__pushups_entry.delete(0, END)
        self.__excercise_added_label["text"] = f"Added {amount} pushups"
        
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
        self.__pullups_entry.delete(0, END)
        text = f"Added {amount} pullups"
        self.__excercise_added_label.configure(text=text)

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
        self.__squats_entry.delete(0, END)
        self.__excercise_added_label.configure(text=f"Added {amount} squats")

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

    def reverse_start(self, break_length):
        extra_time = timedelta(minutes=break_length)
        start_time = datetime.now()
        self.__reverse_end_time = start_time + extra_time
        self.start(start_time)

    def get_reverse_end_time(self):
        return self.__reverse_end_time
    
def select_user():
    user = Select_User.Select_user_GUI()
    return user.get_user()

def read_data(username):
    try:
        data = open(username + "_data.txt", mode="r")
    except: # if file doesnt exist create it and open again for reading
        data = open(username + "_data.txt", mode="w")
        data.write("0000-00-00 00:00:00.000000;cumulative_timer;0:00:00.000000")
        data.close()
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