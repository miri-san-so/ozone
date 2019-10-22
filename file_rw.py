def write_on_file(path_to_ozone,key):
    import ctypes
    FILE_ATTRIBUTE_HIDDEN = 0x02
    f = open("{}access.ozone".format(path_to_ozone),'w')
    f.write("{}".format(key))
    f.close()
    ctypes.windll.kernel32.SetFileAttributesW('{}access.ozone'.format(path_to_ozone),FILE_ATTRIBUTE_HIDDEN)
    return True

def read_from_file(path_to_ozone):
    f = open("{}access.ozone".format(path_to_ozone),'r')
    key = f.read()
    f.close()
    return key

# write_on_file()
#     <> takes path to the access.ozone file
#     <> returns true if file has been written successfully

# read_from_file()
#     <> takes path to the access.ozone file
#     <> returns the data from the file
