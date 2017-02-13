char = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
forbiden = "init str num i for else while and or"
math = "+-*/^=."
blank = "\t\n\r"
#[name,char,Re,Im]
var = []
#[name,value]
strings = [[]]

transpileWithComments = False

def transpile(path, twc):
    transpileWithComments = cwc
    
    
def main():
    global file
    global code
    file = open("programme.txt")
    code = file.read()
    code = code.replace("\t", '')
    code = code.split("\n")
    cleanCode()
    write()
    print(strings)
    print(var)


    
         
def cleanCode():
    print(len(code))
    i=0
    while i < len(code):
        print(i)
        if not transpileWithComments and '#' in code[i]:
            for j in range(0, len(code[i])-1):
                if code[i][j] == '#':
                    code[i]=code[i][0:j:]
                    break

        elif code[i] == "":
            code.remove("")
            i-=1
        i+=1

def write():
    LINES = []
    for line in code:
        split = splitLine(line)
        if split[0] == "Str":
            readNewString(split)
            LINES.append('"'+strings[-1][1]+'"'+"ãStr "+str(len(strings)))

def readNewString(split):
    new = []
    new.append(split[1])
    new.append('')
    if len(split)>2 and split[2]=='=':
        for i in range(3, len(split),2):
            new[1]+=split[i]

    strings.append(new)
            
    
def getNumIndex(name):
    for i in range (0, len(var)):
        if var[i][0]==name:
            return i
    return -1
            
def getStrIndex(name):
    for i in range (0, len(strings)):
        if strings[i][0]==name:
            return i
    return -1

def checkUnused(name):

    for i in range(0, len(strings)):
        if name == strings[i][0]:
            return (0,i)
    for i in range(0, len(var)):
        if name == var[i][0]:
            return (1,i)
    if name in forbiden:
        return (2,-1)
    #(tab, index)
    return (-1,-1)



def splitLine(string):
    result=[]
    i=0
    while(i<len(string)):
        if(string[i].isalpha()):
            if(i+1<=len(string) or string[i+1].isalpha()):
                temp = ''
                while(i<len(string) and string[i].isalnum()):
                    temp += string[i]
                    i+=1
                result.append(temp)
            else:
                result.append('i')
                i+=1

        elif(string[i].isdigit()):
            temp=''
            while(i<len(string) and string[i].isdigit()):
                temp += string[i]
                i+=1
            result.append(temp)

        elif(string[i] in math or(string[i] in "{}")):
            result.append(string[i])
            i+=1
        elif(string[i] in blank):
            i+=1
        else:
            # Erreur, caractère inattendu
            i+=1
    return result


