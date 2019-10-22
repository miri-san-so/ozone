
import os.path, time

def give_date(path_to_ozone):
    try:
        path = path_to_ozone
        path += "access.ozone"
        date_modified = time.ctime(os.path.getmtime(path))
        date_created = time.ctime(os.path.getctime(path))
        return date_created, date_modified
    except FileNotFoundError:
        return "file deleted or renamed", False


# give_data()
#    <> Takes path to .ozone file
#    <> returns date created & date modified
#    <> returns ('file deleted or renamed', false)
#          |- returns a tuple 

#print(give_date("I://"))