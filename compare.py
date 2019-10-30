from usb import locate_usb
from ozone_aes import decrypt_file,encrypt_file
from crypt import decipher
import json
import os

def get_curwd_values():
    
    # key for decryption (not needed provided already in ozone_aes.py)
    #key = b'[MX\xc8\xd5\xbfI{\xa2$\x05(\xd5\x18\xbf\xc0\x85)\x10nc\x94\x02)n\xdf\xcb\xc4\x94\x9d(\x9e'

    print(os.getcwd())    

    # Decrypt the file 
    decrypt_file("curwd.ozone")

    # Read the Values of the file 
    with open("curwd", "r") as f:
        x = f.readlines()

    # Again ecncrypt the File
    encrypt_file("curwd")

    # Initialize a Empty String to store the values
    file_content = ""
    
    # Convert List to String 
    for elements in x:
        file_content += elements

    # import json values for 
    # ├ Counter 
    # ├ key
    # ├ password
    data = json.loads(file_content)

    return(data['pwd'], data['counter'], data['new_key'])
    #print(data['pwd'], data['counter'], data['new_key'])

def get_access_values():
    drives = locate_usb()
    for drive in drives:
        decrypt_file("{}access.ozone".format(drive))
        with open("{}access".format(drive), "r") as f:
            key = f.read()
        x = decipher(key)
        encrypt_file("{}/access".format(drive))                                                                  
    return x