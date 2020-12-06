import tkinter as tk
from datetime import date
import datetime as dt
from time import strftime
root = tk.Tk()
root.title("TO-DO List")
root.geometry("300x500")
root.configure(bg="Black")
#Date on top
day = tk.Label(root, text=f"{dt.datetime.now():%a, %b %d %Y}", fg="white", bg="black", font=("Arial", 20))
day.pack()
def time(): 
    string = strftime('%H:%M:%S %p') 
    timeLabel.config(text = string) 
    timeLabel.after(1000, time) 
timeLabel = tk.Label(root,fg="White",bg="Black")
timeLabel.pack()
time()
#Plans
plans = tk.Label(text="Hello!\n What are the Plans for today?",bg = "Black", fg="White",font = 10)
plans.pack()
getplans = tk.Entry()
getplans.pack()
def getText():
    def Delete():
        result = ''
        for i in todo:
            result += i +'\u0336'
        printgoal.configure(text=result+"\u2713", fg="Green")
    
    todo = "•" + getplans.get() 
    printgoal = tk.Button(text=todo, font=("Arial",15), bg = "Black",fg="White", bd = 0,command=Delete,activebackground="Black")
    printgoal.pack(anchor="nw")
    getplans.delete(0,"end")
#ADD
buttonforplans = tk.Button(command=getText,text="ADD",bg="Grey",fg="white",bd=0,	
activebackground="Grey")
buttonforplans.pack( )
root.mainloop()
