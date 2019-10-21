
from cryptography.fernet import Fernet

# genrate new Key whenever it is called 
def give_new_key():
    key = Fernet.generate_key()
    k = key.decode("utf-8")
    return(k)

# The key generated will be stored on the USB 
# THen the key will be saved on a key_file in local directory of program or a tuple
# Tuple needs to be appened whenever this function is called



