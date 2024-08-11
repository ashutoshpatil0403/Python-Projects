import tkinter as tk
#import time
from time import strftime

root=tk.Tk()
root.title("Digital Clock")

def Current_time():
    string=strftime("%H:%M:%S %p \n %D")
    label.config(text=string)
    label.after(1000,Current_time)

label=tk.Label(root,font=('calibri',50,'bold'),background='blue',foreground='black')
label.pack(anchor="center")    

Current_time()
root.mainloop()