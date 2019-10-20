def cipher(x):
    #defining extended characters and alpabets as elements of list
    ext_chars = list("‚ƒŽ—œ«®±ØÝç▓│┤└┴τΦ╜╛√╫■≈⌡∟")
    alphabets = list("abcdefghijklmnopqrstuvwxyz")

    #for loop to go through all the alphabets nad replace with the respective ext_chars
    for i in x:
        if i == ' ':
            x = x.replace(' ','☺')
        if i == alphabets[0]:
            x = x.replace(alphabets[0],ext_chars[0])
        if i == alphabets[1]:
            x = x.replace(alphabets[1],ext_chars[1])
        if i == alphabets[2]:
            x = x.replace(alphabets[2],ext_chars[2])
        if i == alphabets[3]:
            x = x.replace(alphabets[3],ext_chars[3])
        if i == alphabets[4]:
            x = x.replace(alphabets[4],ext_chars[4])
        if i == alphabets[5]:
            x = x.replace(alphabets[5],ext_chars[5])
        if i == alphabets[6]:
            x = x.replace(alphabets[6],ext_chars[6])
        if i == alphabets[7]:
            x = x.replace(alphabets[7],ext_chars[7])
        if i == alphabets[8]:
            x = x.replace(alphabets[8],ext_chars[8])
        if i == alphabets[9]:
            x = x.replace(alphabets[9],ext_chars[9])
        if i == alphabets[10]:
            x = x.replace(alphabets[10],ext_chars[10])
        if i == alphabets[11]:
            x = x.replace(alphabets[11],ext_chars[11])
        if i == alphabets[12]:
            x = x.replace(alphabets[12],ext_chars[12])
        if i == alphabets[13]:
            x = x.replace(alphabets[13],ext_chars[13])
        if i == alphabets[14]:
            x = x.replace(alphabets[14],ext_chars[14])
        if i == alphabets[15]:
            x = x.replace(alphabets[15],ext_chars[15])
        if i == alphabets[16]:
            x = x.replace(alphabets[16],ext_chars[16])
        if i == alphabets[17]:
            x = x.replace(alphabets[17],ext_chars[17])
        if i == alphabets[18]:
            x = x.replace(alphabets[18],ext_chars[18])
        if i == alphabets[19]:
            x = x.replace(alphabets[19],ext_chars[19])
        if i == alphabets[20]:
            x = x.replace(alphabets[20],ext_chars[20])
        if i == alphabets[21]:
            x = x.replace(alphabets[21],ext_chars[21])
        if i == alphabets[22]:
            x = x.replace(alphabets[22],ext_chars[22])
        if i == alphabets[23]:
            x = x.replace(alphabets[23],ext_chars[23])
        if i == alphabets[24]:
            x = x.replace(alphabets[24],ext_chars[24])
        if i == alphabets[25]:
            x = x.replace(alphabets[25],ext_chars[25])
    return x

def decipher(x):

    #defining extended characters and alpabets as elements of list
    ext_chars = list("‚ƒŽ—œ«®±ØÝç▓│┤└┴τΦ╜╛√╫■≈⌡∟")
    alphabets = list("abcdefghijklmnopqrstuvwxyz")

    #for loop to go through all the alphabets nad replace with the respective ext_chars
    for i in x:
        if i == '☺':
            x = x.replace('☺',' ')
        if i == ext_chars[0]:
            x = x.replace(ext_chars[0],alphabets[0])
        if i == ext_chars[1]:
            x = x.replace(ext_chars[1],alphabets[1])
        if i == ext_chars[2]:
            x = x.replace(ext_chars[2],alphabets[2])
        if i == ext_chars[3]:
            x = x.replace(ext_chars[3],alphabets[3])
        if i == ext_chars[4]:
            x = x.replace(ext_chars[4],alphabets[4])
        if i == ext_chars[5]:
            x = x.replace(ext_chars[5],alphabets[5])
        if i == ext_chars[6]:
            x = x.replace(ext_chars[6],alphabets[6])
        if i == ext_chars[7]:
            x = x.replace(ext_chars[7],alphabets[7])
        if i == ext_chars[8]:
            x = x.replace(ext_chars[8],alphabets[8])
        if i == ext_chars[9]:
            x = x.replace(ext_chars[9],alphabets[9])
        if i == ext_chars[10]:
            x = x.replace(ext_chars[10],alphabets[10])
        if i == ext_chars[11]:
            x = x.replace(ext_chars[11],alphabets[11])
        if i == ext_chars[12]:
            x = x.replace(ext_chars[12],alphabets[12])
        if i == ext_chars[13]:
            x = x.replace(ext_chars[13],alphabets[13])
        if i == ext_chars[14]:
            x = x.replace(ext_chars[14],alphabets[14])
        if i == ext_chars[15]:
            x = x.replace(ext_chars[15],alphabets[15])
        if i == ext_chars[16]:
            x = x.replace(ext_chars[16],alphabets[16])
        if i == ext_chars[17]:
            x = x.replace(ext_chars[17],alphabets[17])
        if i == ext_chars[18]:
            x = x.replace(ext_chars[18],alphabets[18])
        if i == ext_chars[19]:
            x = x.replace(ext_chars[19],alphabets[19])
        if i == ext_chars[20]:
            x = x.replace(ext_chars[20],alphabets[20])
        if i == ext_chars[21]:
            x = x.replace(ext_chars[21],alphabets[21])
        if i == ext_chars[22]:
            x = x.replace(ext_chars[22],alphabets[22])
        if i == ext_chars[23]:
            x = x.replace(ext_chars[23],alphabets[23])
        if i == ext_chars[24]:
            x = x.replace(ext_chars[24],alphabets[24])
        if i == ext_chars[25]:
            x = x.replace(ext_chars[25],alphabets[25])
    return x
