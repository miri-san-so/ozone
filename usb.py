import win32file
import glob
import os
from cipher import cipher

def locate_usb():
    drive_list = []
    drivebits = win32file.GetLogicalDrives()
    for d in range(1, 26):
        mask = 1 << d
        if drivebits & mask:
            # here if the drive is at least there
            drname = '%c:\\' % chr(ord('A') + d)
            t = win32file.GetDriveType(drname)
            if t == win32file.DRIVE_REMOVABLE:
                drive_list.append(drname)
    return drive_list

drives = locate_usb()

os.chdir(r'{}'.format(drives[0]))
ozone_files = glob.glob('*.ozone')

pwd = "hello my friend, its pasha my friend"
pwd_cip = (cipher(pwd), "utf-8")

f = open("test.ozone","w")
f.write("{}".format(pwd_cip))
f.close()

for drive in drives:
    pass
