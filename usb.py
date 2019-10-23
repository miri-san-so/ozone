import win32file
import glob
import os
from cipher import cipher

def locate_usb():
    drive_list = []

    # Get all the list of Drices
    drivebits = win32file.GetLogicalDrives()

    # Go through all the drives
    for d in range(1, 26):
        mask = 1 << d
        if drivebits & mask:
            # here if the drive is at least there
            drname = '%c:\\' % chr(ord('A') + d)
            t = win32file.GetDriveType(drname)
            if t == win32file.DRIVE_REMOVABLE:
                # Append all the removable drives
                drive_list.append(drname)
    return drive_list

def find_file(drive):
    # Checks for file in the drive list 
    #for i in drive_list:
    i = drive
    os.chdir(r'{}'.format(i))
    if glob.glob('access.'):
        return True
    else:
        return False

def new_usb_connected():
    if locate_usb() == []:
        return False
    else:
        return True


# locate_usb() 
#    <>returns the list of removable drives

# find_file()
#    <>takes list of usb drives
#    <>returns True if the ozone file exists
#    <>otherwise returns false