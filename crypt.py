
from cryptography.fernet import Fernet

def give_data():
    key = Fernet.generate_key()
    k = key.decode("utf-8")
    return(k)
    
def give_ciphered_counter(current_counter):
    main_list = ["-hcum","-tantropmi","-yranoityulover","-saedi","-eht","-yaw","-ot","-egnahc","-ruo","-dlrow"]

    updated_counter=list(str(current_counter))
    c = "\.//"
    cypher = ""
    for i in updated_counter:
        if i == "0":
            cypher+=main_list[0]
        if i == "1":
            cypher+=main_list[1]
        if i == "2":
            cypher+=main_list[2]
        if i == "3":
            cypher+=main_list[3]
        if i == "4":
            cypher+=main_list[4]
        if i == "5":
            cypher+=main_list[5]
        if i == "6":
            cypher+=main_list[6]
        if i == "7":
            cypher+=main_list[7]
        if i == "8":
            cypher+=main_list[8]
        if i == "9":
            cypher+=main_list[9]
    c += cypher
    return c

def give_new_key(current_counter):
    key_data = give_data()
    key_counter = give_counter(current_counter)
    key = key_data + key_counter
    return key

def decipher(key):
    flag = 0
    #extracting counter elements from the key
    key = key.split("\.//")
    if len(key) == 2:
        deciphered_data = key[0]
        counter_list = key[1]
        counter_elements = counter_list.split("-")

        #deciphering the counter
        j=1
        main_list = ["-hcum","-tantropmi","-yranoityulover","-saedi","-eht","-yaw","-ot","-egnahc","-ruo","-dlrow"]
        decipher = ""
        for j in counter_elements:
            k = "-"
            k +=j 
            if k == main_list[0]:
                decipher+="0"
                flag = 1
            if k == main_list[1]:
                decipher+="1"
                flag = 1
            if k == main_list[2]:
                decipher+="2"
                flag = 1
            if k == main_list[3]:
                decipher+="3"
                flag = 1
            if k == main_list[4]:
                decipher+="4"
                flag = 1
            if k == main_list[5]:
                decipher+="5"
                flag = 1
            if k == main_list[6]:
                decipher+="6"
                flag = 1
            if k == main_list[7]:
                decipher+="7"
                flag = 1
            if k == main_list[8]:
                decipher+="8"
                flag = 1
            if k == main_list[9]:
                decipher+="9"
                flag = 1

        if flag == 1:
            return deciphered_data, decipher
        else:
            print("cannot decipher since the counter elements are not valid")
            return False
    else:
        print("key has been modified")
        return False

# give_data()
#    <> returns a data part for the key


# give_ciphered_counter()
#    <> takes current counter count as argument
#    <> returns couter part of the key
#print(give_ciphered_counter(123))


# give_new_key()
#    <> Takes the current counter as argument
#    <> returns a key with the data and counter part together


# decipher()
#    <> takes the ciphered counter 
#    <> returns the counter as tuple of string 
#print(decipher("gayboi69\.//-tantropmi-yranoityulover-saedi"))
