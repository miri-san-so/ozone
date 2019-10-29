from file_rw import *
from crypt import give_new_key
from tkinter import Frame, Entry, Label, Tk
from usb import new_usb_connected, locate_usb, find_file


while new_usb_connected() == False:
    continue

def create_window():
    t=Tk()
    t.geometry('900x500')
    t.config(bg='#1a1a1a')
    ozone = Label(t, text="ozone.", font=("Helvetica", 21),fg="#8fdcdf",bg="#1a1a1a")

    ozone.place(x=395,y=180)

    frame=Frame(t,height=20,width=30,bg="#8fdcdf",bd=2,highlightbackground="#8fdcdf")
    Entry(frame,bg="#1a1a1a",width=40,fg="#8fdcdf").grid(column=2)
    frame.place(x=315,y=215)

    t.mainloop()

devices = locate_usb()
counter = 0
last_key_generated = ""
access_flag = 0
for device in devices:
    print(device)
    if(find_file(device)==True):
        key = read_from_file(device)
        if key == last_key_generated:
            counter += 1
            new_key = give_new_key(counter)
            last_key_generated = new_key
            write_on_file(device,new_key)
            create_window()
            access_flag = 1
        else:
            access_flag = 0
            print("key did not match")
    else:
        print("ozone file not found")
        
