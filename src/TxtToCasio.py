char = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
statement = "if else for while"
forbiden = "str num" + statement
#+-ÀÁ^
math = "+-*/^="
cond = "|&<>="
blank = "\t\n\r"
includedChars = "\"'_"

var = []
strings = [[]]
ls = [[]]
mats = []
declarateur = ("Str ", "", "List ", "Mat ")

logic=["&&","||","!!","!|","==","!=","<=",">=","<",">","++","--"]
logic_casio=["And","Or","Not", "Xor","=","È","É","Ê","<",">","Isz ","Dsz "]

# PARS
# -c : transpile with comments
# -i : include blank variable declaration
#

pars = "" 
NAME="A"

def transpile(path, twc):
    transpileWithComments = cwc
    
    
def main():
    global code
    file = open("programme.txt")
    code = file.read()
    code = code.replace("\t", '')
    code = code.split("\n")
    cleanCode()
    write()
    print("Strings:",strings)
    print("Nums   :", var)
    print("Lists  :", ls)
    print("Mats   :", mats)

    
         
def cleanCode():
    i=0
    while i < len(code):
        if not "-c" in pars and '#' in code[i]:
            for j in range(0, len(code[i])-1):
                if code[i][j] == '#':
                    code[i]=code[i][0:j:]
                    break

        elif code[i] == "":
            code.remove("")
            i-=1
        i+=1

def write():
    global LINES
    LINES = ["Ù\n"]
    queue = []
    global r_line
    for r_line in range(0, len(code)):
        split = splitLine(code[r_line])


        ### INIT ###
        if split[0] in "Num Str List Mat":
            if(len(split)>1 and checkUnused(split[1])==(-1,-1)):
                getVarList(split[0]).append(split[1])
                u=checkUnused(split[1])
                txt=opToString(split[3:])
                if not txt=="//ERROR":
                    if "=" in code[r_line]:
                        if split[0]in ["Num","Mat"]:
                            txt= txt.replace('{','[').replace('}',']')  
                            LINES.append(txt+"ã"+declarateur[u[0]]+char[len(getVarList(split[0]))-1])
                        else:
                            LINES.append(txt+"ã"+declarateur[u[0]]+str(len(getVarList(split[0]))-1))
                    else:
                        if split[0]in ["Num","Mat"]:
                            LINES.append(txt+declarateur[u[0]]+char[len(getVarList(split[0]))-1])
                        elif "-i" in pars:
                            LINES.append(declarateur[u[0]]+str(len(getVarList(split[0]))))

       

        ### STATEMENT + QUEUE ###
        elif split[0] in statement:
            cap = split[0][0].capitalize()+split[0][1:]
            LINES+=cap
            LINES+=" "
            LINES+=conditionToString(split[1:])
            queue.append(getStatementEnd(cap))
            if split[0]=="if":
                LINES[-1]+="Ù\nThen "

        elif split[0]=='}':
            LINES+=queue.pop()

        ### OPERATIONS AND VAR FUNCTIONS
        elif checkUnused(split[0])[0] != -1 and len(splitLine)>2:
            u = checkUnused(split[0])

            ## OPERATIONS ##
            if splitLine[1]=='=':
                if u[0]==1:
                    if(split[1]in ["++","--"]):
                        LINES+=opToString(split)
                    else:
                        LINES+=opToString(split[2:])+"ã"+char[var.index(split[0])]
                elif u[0]==0:
                    LINES+=opToString(split[2:])+"ãStr "+str(strings.index(split[0]))
                elif u[0]==2:
                    LINES+=opToString(split[2:])+"ãList "+str(ls.index(split[0]))
                elif u[0]==3:
                    LINES+=opToString(split[2:])+"ãMat "+char[mats.index(split[0])]


            ## FUNCTIONS ##
            elif splitLine[1]=='.':
                
                           
        
        if(LINES[-1][-5:] != "Then "):
            LINES[-1]+="Ù\n"
        
    file = open("casio.txt",'w', encoding="utf8")
    file.writelines(LINES)
    file.close()
                                                         

def checkUnused(name):

    for i in range(1, len(strings)):
        if name == strings[i]:
            return (0,i)
    for i in range(0, len(var)):
        if name == var[i]:
            return (1,i)
    for i in range(1, len(ls)):
        if name == ls[i]:
            return (2,i)
    for i in range(0, len(mats)):
        if name == mats[i]:
            return (3,i)
    
    if name in forbiden:
        return (2,-1)
    #(tab, index)
    return (-1,-1)



def splitLine(string):
    result=[]
    i=0
    while(i<len(string)):
        if(string[i].isalpha() or (string[i] in includedChars)):
            if(i+1<=len(string) or (string[i] in includedChars)):
                temp = ''
                while(i<len(string) and (string[i].isalnum() or (string[i] in includedChars))):
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

        elif(string[i] in math+cond):
            temp=''
            while i<len(string) and string[i] in math+cond:
                temp += string[i]
                i+=1
            result.append(temp)
        
        elif(string[i] in "{}()."):
            result.append(string[i])
            i+=1
        
        elif(string[i] in blank):
            i+=1
        elif(string[i] in '['):
            temp = '['
            i+=1
            while i<len(string) and  string[i] not in '][':
                temp+=string[i]
                i+=1
            if i<len(string) and string[i]==']':
                temp+=']'
                i+=1
            result.append(temp)
        elif(string[i]==']'):
            result.append(']')
            i+=1
            
            
        else:
            # Error, unexpected character
            i+=1
    return result

def opToString(split, *rec):
    final=''
    par="+-ÀÁ^="
    if len(split)==2 and checkUnused(split[0])[0]==1 and split[1] in ["++","--"]:
        final = dictionary(split[1])+char[var.index(split[0])]
    else:
        for i in range(0, len(split)):
            u=checkUnused(split[i]) 
            if u[0]==0:
                final+="Str "+str(u[1])
            elif(u[0]==1):
                final+=char[u[1]]
            elif(split[i] in math):
                final+= par[math.index(split[i])]
            elif(split[i][0]=='[' and split[i][-1]==']'):
                final+="{"
                final+=opToString(splitLine(split[i][1:-1]), ',')
                final+='}'
            elif split[i]in['[',']']:
                final+="{}"[['[',']'].index(split[i])]
            else:
                final+=split[i].replace('i','½')
            if rec != () and i!=len(split)-1:
                 final+=rec[0]
    
    return final
            

def conditionToString(split):
    final = ""
    
    for i in range(0,len(split)):
        
        if split[i][0]==split[i][-1]=='"' or checkUnused(split[i])[0]==0:
            c_split=[]
            while i<len(split) and split[i] not in logic and split[i] not in "!==":
                c_split.append(split[i])
                i+=1
            final  += concatToSring(split[c_split])

        elif split[i] in "()":
            final += split[i]

        elif split[i] in logic:
            final+=dictionary(split[i])
            
        elif split[i].isdigit() or checkUnused(split[i])[0]==1 or split[i]in "i.":
            c_split=[]
            while i<len(split) and split[i] not in logic and split[i] not in "({})":
                c_split.append(split[i])
                i+=1
            final  += opToString(c_split)

    return final

def getStatementEnd(string):
    if string in "IfWhile":
        return string+"End"
    elif string == "For":
        return "Next"
    else:
        return ""
    
def dictionary(string):
    for i in range(0, len(logic)):
        if string == logic[i]:
            return logic_casio[i]
    return ""
            
def getVarList(name):
    u=checkUnused(name)
    if u[0]==0 or name=="Str":
        return strings
    elif u[0]==1 or name=="Num":
        return var
    elif u[0]==2 or name=="List":
        return ls
    elif u[0]==3 or name=="Mat":
        return mats
    else:
        return None
