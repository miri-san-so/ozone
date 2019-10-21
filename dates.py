
# The function requires a path to .ozone file

import os.path, time

def give_date(path_to_ozone):
    date_modified = time.ctime(os.path.getmtime(path_to_ozone))
    date_created = time.ctime(os.path.getctime(path_to_ozone))
    return date_created, date_modified

#returns date created & date modified