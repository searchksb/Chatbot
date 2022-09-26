from tkinter import *
from tkinter import messagebox

window = Tk() #create a window
window.title("welcome to solent chatterbox")
window.geometry("400x150")#to fix the window size
main_menu = Menu(window)


frame1 = Frame(window)
frame1.pack()
scrollbar = Scrollbar(frame1)
scrollbar.pack(side=RIGHT, fill=Y)
text = Text(frame1, width=40, height=10, wrap=WORD, yscrollcommand=scrollbar.set)

lbl = Label(window, text= "Hello World", font=("Arial Bold", 12))
#lbl.grid(column=0, row=0)

lbl2 = Label(window, text="Please enter your name")
#lbl2.grid(column=0, row=1)

txt= Entry(window)
#txt.grid(column=1, row=1)
text.pack()
scrollbar.config(command=text.yview)
def Greetuser():
    userName= txt.get()
    messagebox.showinfo("", "Hello, " + userName)


btn = Button(window, text="Click Me", bg="yellow", fg="red",command= Greetuser)
#btn.grid(column=2, row=1)

window.mainloop()

#every line in here would be blocked
#until the window is closed

from chat import get_response, bot_name
BG_GRAY =
BG_COLOR =
TEXT_COLOR =
FONT = "Helvetica 14"
FONT_BOLD = "Helvetica 13 bold"

class chatapplication:

    def _init_(self):
        self.window = Tk()
        self._setup_main_window()

    def run(self):
        self.window.mainloop()

    def _setup_main_window(self):
        self.window.title("chat")
        self.window.resizable(width=False, height=False)
        self.window.configure(width= 470, height=550, bg=BG_COLOR)

        #head label
        head_label = label(self.window, bg= BG_COLOR, fg=TEXT_COLOR,text="Welcome", font=FONT_BOLD, pady=10)
        head_label.place(relwidth=1)


        #tiny divider
        line = Label(self.window, width=450, bg=BG_GRAY)
        line.place(relwidth=1, rely=0.07, relheight=0.012)

    if _name_ == "_main_":
        app = chatapplication()
        app.run()
