"""
COMP.CS.100 Programming 1
GUI for user selection.
Jani Ollenberg
H288244
"""

import tkinter
from tkinter.constants import END

class Select_user_GUI():
    def __init__(self):
        self.__select_user_window = tkinter.Tk()
        self.__select_user_window.title("Life Manager - Select User")
        self.__select_user_window.option_add("*Font", "Verdana 30")

        self.__users_list = read_users_list()

        self.__select_user_label = tkinter.Label(text="Select user:")
        self.__select_user_label.grid()

        self.__variable = tkinter.StringVar(self.__select_user_window)
        self.__variable.set(self.__users_list[0]) # default value
        self.__dropdown = tkinter.OptionMenu(self.__select_user_window, self.__variable,
                               *self.__users_list, command=self.display_selected)
        self.__dropdown.grid()

        self.__continue = tkinter.Button(text="Continue", command=self.stop)
        self.__continue.grid(row=1, column=1)
        
        self.__new_user_button = tkinter.Button(text="Add new user",
                                                command=self.new_user)
        self.__new_user_button.grid()

        self.__new_user_entry = tkinter.Entry(text="New username here")
        self.__new_user_entry.grid(row=2, column=1)

        self.__select_user_window.mainloop()

    def display_selected(self, choice):
        choice = self.__variable.get()
        print(choice)
    
    def new_user(self):
        name = self.__new_user_entry.get()
        self.__users_list.append(name)
        print(self.__users_list)
        users_file = open("Life Manager_users.txt", mode="a")
        users_file.write(f"{name}\n")
        users_file.close()
        # update dropdown menu
        menu = self.__dropdown["menu"]
        menu.delete(0, END)
        for user in self.__users_list:
            menu.add_command(label=user,
                             command= lambda value=user:
                             self.__variable.set(user))

    def stop(self):
        self.__select_user_window.destroy()

    def get_user(self):
        return self.__variable.get()

def read_users_list():
    # try to open user list
    try:
        users_file = open("Life Manager_users.txt", mode="r")
        print("file exists")
    except: # create the users list
        users_file = open("Life Manager_users.txt", mode="w")
        users_file.write("Test User\n")
        users_file.close()
        print("create new file")
        return read_users_list()
    
    users_list = []
    all_lines = users_file.readlines()
    print(all_lines)

    for line in all_lines:
        line = line.rstrip()
        users_list.append(line)
    print(users_list)
    users_file.close()
    return users_list