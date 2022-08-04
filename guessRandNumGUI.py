# -*- coding: utf-8 -*-
"""
Created on Sun Jul 31 15:25:47 2022

@author: faith
"""
from tkinter import Tk, Label, Entry, Button, END
from random import randint

#create window
root = Tk()

#set title screen size and color
root.title("Number Guess")
root.geometry("750x350")
root.configure(bg="#999999")

#display text label
num_label = Label(root, text="Guess a number 1-10", font=("Arial", 32, "bold"), bg="#999999")
num_label.pack(padx=10, pady=10)

#user guesses what the random generated number is
def guess():

    if guess_entry.get().isdigit():
        num_label.config(text="Guess a number 1-10")
        int(guess_entry.get())
        if int(guess_entry.get()) == num:
            num_label.config(text="Correct")
        elif int(guess_entry.get()) < num:
            num_label.config(text="Too low")
        elif int(guess_entry.get()) > num:
            num_label.config(text="Too high")
        else:
            num_label.config(text="Try again!")
               
    else:
        guess_entry.delete(0, END)
        num_label.config(text="Your guess has to be a number 1-10!", font=("Arial", 24, "bold"))
#gets random integer 
def random_int():
    global num
    num = randint(1, 10)
    #clear guess box
    guess_entry.delete(0, END)
    num_label.config(text="Guess a number 1-10", bg="#999999")

#user input
guess_entry = Entry(root, font=("Arial", 60), width=2)
guess_entry.pack(padx=10, pady=10)

#user submits input
submit_button = Button(root, text="Submit", font=("Arial", 26), command=guess)
submit_button.pack(padx=10, pady=10)

#start a new game
restart_button = Button(root, text="New Game", command=random_int)
restart_button.pack(padx=10, pady=10)

#call to get random number at start of game
random_int()
root.mainloop()


 