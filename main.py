from file_rw import *
from crypt import give_new_key
from tkinter import Frame, Entry, Label, Tk, Button
from usb import new_usb_connected, locate_usb, find_file
from compare import get_access_values, get_curwd_values
from ozone_aes import decrypt_file, encrypt_file
from cipher import decipher
import os, glob, json

def give_correct_drive(drive):
    # Checks for file in the drive list 
    #for i in drive_list:
    os.chdir(drive)     
    if glob.glob("*.ozone") != "":
        return drive
    else:
        return False

workin_dir = os.getcwd()

def get_value(pwd):
    
    drives = locate_usb()
    
    # Gets the password 
    recieved_password = pwd
    print("recieved password : ",recieved_password)
    
    # Gets the passwotd, counter and the key from curwd
    curwd_file_password, curwd_file_counter, curwd_file_key = get_curwd_values()
    print("curwd password : ",curwd_file_password)
    
    # compares password
    if recieved_password == curwd_file_password:
        
        print("password same")        
        
        # seprates the key
        curwd_file_key = curwd_file_key.split("[$].//")
        curwd_file_key = curwd_file_key[0]    
        print("curwd counter : ",curwd_file_counter," type = ",type(curwd_file_counter))    
        print("curwd old key : ",curwd_file_key)    
        curwd_file_counter = int(curwd_file_counter)
 
        access_file_key, access_file_counter = get_access_values()
        print("access file key : ",access_file_key)
        print("access file counter : ",access_file_counter)
        access_file_counter = int(access_file_counter)
        
        if access_file_counter == curwd_file_counter and access_file_key == curwd_file_key:
            
            for i in drives:
                drive_found = give_correct_drive(i)
                if drive_found == False:
                    print("File not found")
                else:
                    new_counter = curwd_file_counter + 1
                    ###[ W R I T I N G   F O R    A C C E S S  F I L E  ]###
                    print("\n-------------\nfor access file")
                    
                    # Making new Key    [Passing curwd counter] 
                    print("created new key...")
                    new_key = give_new_key(new_counter)
                    print("new_key for access file : ",new_key)
                    # Decrypting file 
                    print("decrypting file...")
                    decrypt_file("{}access.ozone".format(drive_found))
                    
                    # Writing the key on file
                    print("writing on file...")
                    write_on_file(drive_found, new_key)
                    print("new key in access file : ", new_key)
                    
                    # Encrypting the file again
                    print("encrypting...")
                    encrypt_file("{}access".format(drive_found))   
                    
                    
                    ###[ W R I T I N G    F O R    C U R W D   F I L E  ]###
                    print("\n-----------\nfor curwd file...")         
                               
                    # Decrypting the Curwd file
                    print("Decrypting curwd...")
                    decrypt_file("{}\curwd.ozone".format(workin_dir))

                    # Read the Values of the file 
                    with open("{}\curwd".format(workin_dir), "r") as f:
                        x = f.readlines()

                    # Initialize a Empty String to store the values
                    file_content = ""
                    
                    # Convert List to String 
                    for elements in x:
                        file_content += elements
                        
                    print("making json...")
                    data = json.loads(file_content)
                    data['new_key'] = new_key
                    data['counter'] = new_counter
                    print("curwd new key : ",new_key)
                    
                    with open("{}\\curwd".format(workin_dir), "w") as f:
                        print("writing on curwd...")
                        data_for_curwd = json.dumps(data)
                        print(data_for_curwd)
                        f.write(data_for_curwd)
                    
                    print("encrypting the curwd...")
                    encrypt_file("{}/curwd".format(workin_dir))
                    
            print("verified")
            new = Tk()
            new.geometry('900x500')
            new.config(bg='#1a1a1a')
            label1 = Label(new,text="access has been granted", font=("Helvetica", 12), fg="cyan", bg="#1a1a1a")
            label1.pack()
            new.mainloop()
        else:
            print("key and counter are not same")
    else:
        print("password not same")

if locate_usb() == []:
    t = Tk()
    t.geometry('900x500')
    t.config(bg='#1a1a1a')
    error = Label(
            t, text="p l e a s e   e n t e r   y o u r   o z o n e   k e y   a n d   r e s t a r t   *", font=("Helvetica", 12), fg="cyan", bg="#1a1a1a")
    error.place(x=220,y=240)

    t.mainloop()
    
else:
    def create_window():
        t = Tk()
        t.geometry('900x500')
        t.config(bg='#1a1a1a')
        ozone = Label(t, text="o z o n e .", font=("Helvetica", 12,
                                                "italic", "bold"), fg="#8fdcdf", bg="#1a1a1a")
        ozone.place(x=400, y=140)

        pwd = Label(t, text="e n t e r   p a s s w o r d", font=(
            "Helvetica", 12), fg="#8fdcdf", bg="#1a1a1a")
        pwd.place(x=315, y=180)

        frame = Frame(t, height=20, width=30, bg="#8fdcdf",
                    bd=2, highlightbackground="#8fdcdf")
        pwd = Entry(frame, bg="#1a1a1a", width=40, fg="#8fdcdf",
                    show="*", insertbackground="cyan")
        pwd.grid(column=2)
        frame.place(x=315, y=215)

        submit = Button(t, text="e\t n\t t\t e\t r", font=("Helvetica", 8), fg="cyan", bg="#1a1a1a", activebackground="#1a1a1a",
                                activeforeground="#8fdcdf", padx=3, pady=3, borderwidth=2, command=lambda: get_value(pwd.get()))
        submit.config(highlightbackground="#8fdcdf",
                    highlightcolor="#8fdcdf", highlightthickness=10, relief="solid")
        submit.place(x=320, y=390)

        t.mainloop()
    create_window()


"""devices = locate_usb()
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

"""
