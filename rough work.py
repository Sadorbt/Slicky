from tkinter import *

# Canceling an item

# clicking an item



# Destroy a window
def window2(window):
    window.destroy()

# Go back to the starter window
def go_back(window):
    window2(window)
    start_game()

# Starter window 
def start_game():
    splash_window = Tk()
    splash_window.geometry("360x360")
    splash_window.configure(bg="#17161b")
    splash_window.title("Guessing Game")
    splash_window.resizable(0, 0)

    intro = Label(splash_window, text="Welcome to the Guessing World", font=('Helvetica', 17, 'bold'))
    intro.pack(ipady=25)

    exit_button = Button(splash_window,text="Exit Game",font=("Arial",14), fg="White", bg="#b82741", command=exit)
    exit_button.place(x=120, y=280)

    play_button = Button(splash_window, text="Play Game", font=("Arial", 14, "bold"), fg = "Black", bg="#29c70a", command=lambda:play_game(splash_window))
    play_button.place(x=140, y=220)




# This is to start the actual game
def play_game(window):
   window2(window) 
   new = Tk()
   new.geometry("360x360")
   new.title("Guessing Game")
   new.configure(bg="#17161b")
   new.resizable(0, 0)

   input_text = StringVar()
   
   instruction = Label(new, text="Input your lowest range", width=360, font=('Helvetica', 17, 'bold'))
   instruction.pack(ipady=10)
   
   input_frame = Frame(new, width=360, height=50, bd=1, highlightbackground="black", highlightcolor="black", highlightthickness=2)
   input_frame.pack(side=TOP)
   
   input_field = Entry(input_frame, font=('arial', 18, 'bold'), fg='black', textvariable=input_text, width=50, bg="#eee", bd=0, justify=RIGHT)
   input_field.grid(row=0, column=0)
   input_field.pack(ipady=10)
   #    print('VALUE: ', input_text.get())
   # Button container  
    
   btns_frame = Frame(new, width=360, height=310.5, bg="tomato")
   btns_frame.pack()
   # Button row 1
   one = Button(btns_frame, text = "1", fg = "white", width = 6, height = 2, bd = 1, bg = "#2a2d36", cursor = "hand2", padx = 10, pady = 8, command=lambda:btn_click(1))
   one.place(x=1, y=1)
   
   two = Button(btns_frame, text = "2", fg = "white", width = 6, height = 2, bd = 1, bg = "#2a2d36", cursor = "hand2",  padx = 10, pady = 8, command=lambda:btn_click(2))
   two.place(x=95, y=1)
   
   three = Button(btns_frame, text = "3", fg = "white", width = 6, height = 2, bd = 1, bg = "#2a2d36", cursor = "hand2", padx = 10, pady = 8, command=lambda:btn_click(3))
   three.place(x=190, y=1)
   
   four = Button(btns_frame, text = "4", fg = "white", width = 6, height = 2, bd = 1, bg = "#2a2d36", cursor = "hand2", padx = 10, pady = 8, command=lambda:btn_click(4))
   four.place(x=290, y=1)
   
   # Button row 2
   five = Button(btns_frame, text = "5", fg = "white", width = 6, height = 2, bd = 1, bg = "#2a2d36", cursor = "hand2", padx = 10, pady = 8, command=lambda:btn_click(5))
   five.place(x=1, y=60)
   
   six = Button(btns_frame, text = "6", fg = "white", width = 6, height = 2, bd = 1, bg = "#2a2d36", cursor = "hand2", padx = 10, pady = 8, command=lambda:btn_click(6))
   six.place(x=95, y=60)
   
   seven = Button(btns_frame, text = "7", fg = "white", width = 6, height = 2, bd = 1, bg = "#2a2d36", cursor = "hand2", padx = 10, pady = 8, command=lambda:btn_click(7))
   seven.place(x=190, y=60)
   
   eight = Button(btns_frame, text = "8", fg = "white", width = 6, height = 2, bd = 1, bg = "#2a2d36", cursor = "hand2", padx = 10, pady = 8, command=lambda:btn_click(8))
   eight.place(x=290, y=60)
   
   # Button row 3
   back = Button(btns_frame, text = "Back", font=("Arial",14), fg="White", bg="#b82741",  width = 7,  height = 2,  padx = 1, pady = 1, command=lambda:go_back(new))
   back.place(x=1, y=120)
   
   nine = Button(btns_frame, text = "9", fg = "white", width = 6, height = 2, bd = 1, bg = "#2a2d36", cursor = "hand2", padx = 10, pady = 8, command=lambda:btn_click(9))
   nine.place(x=95, y=120)
   
   
   zero = Button(btns_frame, text = "0", fg = "white", width = 6, height = 2, bd = 1, bg = "#2a2d36", cursor = "hand2", padx = 10, pady = 8, command=lambda:btn_click(0))
   zero.place(x=190,y=120)
   
   clear = Button(btns_frame, text = "Clear",font=("Arial",14), fg="White", bg="#b82741" , width = 7, height = 2, padx = 1, pady = 1)
   clear.place(x=270, y=120)
   
   # Button row 4
   continue_btn = Button(btns_frame, text = "Continue",font=("Arial",16), fg = "white", width = 12, height = 1, bd = 1, bg ="#29c70a", cursor = "hand2", padx = 10, pady = 5, command = lambda: btn_clear)
   continue_btn.place(x=97, y=200)                                                                                                                                                                                                                                                                                                                                                                                                                                          #    play_button.place(x=140, y=220)



 

expression = "" 

def btn_click(number):
   global expression
   expression = expression + str(number)
   input_text.set(expression)
    #print('VAL: ', input_text.get())


def btn_clear():
    global expression
    expression = "" 
    input_text.set("")






start_game()
mainloop()