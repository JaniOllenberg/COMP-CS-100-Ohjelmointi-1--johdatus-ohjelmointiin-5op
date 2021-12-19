"""
COMP.CS.100 Programming 1
Testing tkinter.
Jani Ollenberg
H288244
"""
# import tkinter
# def main():
#     mainWindow = tkinter.Tk()
#     mainWindow = tkinter.mainloop()
# if __name__ == "__main__":
#     main()

# from tkinter import *

# class Käyttöliittymä:
#   def __init__(self):
#     self.__pääikkuna = Tk()

#     # self.__tekstikenttä = Label(self.__pääikkuna, text="Hello World!")
#     self.__text2 = Label(self.__pääikkuna, text="Hei hei mitä kuuluu?")
#     self.__text2.pack(side=TOP)
#     self.__tekstikenttä = Label(self.__pääikkuna, text="Hello World!",
#                             background="green", foreground="red",
#                             padx=30, pady=10,
#                             relief=RAISED, borderwidth=5)
#     self.__tekstikenttä.pack(expand=True, fill=BOTH)
#     self.__tekstikenttä.configure(text="Yep!",
#                               background="blue",
#                               foreground="yellow",
#                               padx=80,
#                               pady=5,
#                               relief=FLAT,
#                               borderwidth=1)
#     self.__tekstikenttä.pack()

#     self.__pääikkuna.mainloop()

# def main():
#   käli = Käyttöliittymä()

# if __name__ == "__main__":
    # main()

# from tkinter import *

# class Käyttöliittymä:
#   def __init__(self):
#     self.__pääikkuna = Tk()

#     self.__tekstikenttä = Label(self.__pääikkuna, text="Hello World!")
#     self.__tekstikenttä.pack()

#     self.__lopetusnappi = Button(self.__pääikkuna, text="lopeta mut",
#                                   command=self.lopeta)
#     self.__lopetusnappi.pack()

#     self.__pääikkuna.mainloop()

#   def lopeta(self):
#     self.__pääikkuna.destroy()

# def main():
#   käli = Käyttöliittymä()

# if __name__ == "__main__":
#   main()


from tkinter import *

class GUI:
  def __init__(self):
    self.__main_window = Tk()

    self.__labelA = Label(self.__main_window, text="A", borderwidth=2, relief=GROOVE)
    self.__labelA.grid(row=1, column=1)

    self.__labelB = Label(self.__main_window, text="B", borderwidth=2, relief=GROOVE)
    self.__labelB.grid(row=1, column=2, sticky=E)

    self.__high_label = Label(self.__main_window, text="high", borderwidth=2, relief=GROOVE)
    self.__high_label.grid(row=0, column=0, rowspan=3, sticky=N+S)

    self.__wide_label = Label(self.__main_window, text="wide", borderwidth=2, relief=GROOVE)
    self.__wide_label.grid(row=0, column=1, columnspan=2, sticky=E+W)

    self.__quit_button = Button(self.__main_window, text="Quit", command=self.quit)
    self.__quit_button.grid(row=2, column=2)

    self.__main_window.mainloop()

  def quit(self):
    self.__main_window.destroy()

def main():
  gui = GUI()

if __name__ == "__main__":
    main()