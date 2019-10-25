def write_on_file(path_to_ozone,key):
    f = open("{}access".format(path_to_ozone),'w')
    f.write("{}".format(key))
    f.close()
    return True

def read_from_file(path_to_ozone):
    f = open("{}access".format(path_to_ozone),'r')
    key = f.read()
    f.close()
    return key

# write_on_file()
#     <> takes path to the access.ozone file
#     <> returns true if file has been written successfully

# read_from_file()
#     <> takes path to the access.ozone file
#     <> returns the data from the file

#print(write_on_file('I://',''))