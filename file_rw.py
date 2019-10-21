def write_on_file(path_to_ozone,key):
    f = open("{}",'w')
    f.write("{}".format(key))
    f.close()
    return True

def read_from_file(path_to_ozone):
    f = open("{}",'r')
    key = f.read()
    f.close()
    return key