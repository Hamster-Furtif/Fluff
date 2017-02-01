num = [0,1,2,3,4,5,6,7,8,9]
char = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#[name,char,Re,Im]
var = []
#[name,value]
strings = []

def main():
    global file
    global code
    file = open("programme.txt")
    code = file.read()
    code = code.replace(" ", "")
    code = code.split("\n")
    initVar()

def initVar():
    if(code[0] == "init{"):
        i=0
        while (code[i] != "}"):
            if(code[i][:6:] == "String"):
                readStringVar(code[i])
            else:
                readNumVar(code[i])
            i+=1
       

def readStringVar(line):
    string = ["",""]
    j=6
    while(line[j] != "=" and j<len(line)-1):
        string[0] += line[j]
        j+=1
        
    if( line[j] == "="):
        if(line[j+1] == '"' and line[-1]=='"'): 
            string[1] = line[j+2:-1]
            
        else:
            if (getStrIndex(line[j+1:])!=-1):
                string[1] = strings[getStrIndex(line[j+2:])][1]

    strings.append(string)

def readNumVar(line):
    num=["","",0,0]
    num[1]=char[len(var)-1]
    j=0
    while(line[j] != "=" and j<len(line)-1):
        num[0] += line[j]
        j+=1
    var.append(var)

def getVarIndex(name):
    for i in range (0, len(var)):
        if var[i][0]==name:
            return i
    return -1
            
def getStrIndex(name):
    for i in range (0, len(strings)):
        if strings[i][0]==name:
            return i
    return -1
