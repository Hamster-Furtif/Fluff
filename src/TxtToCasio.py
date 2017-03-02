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
logic=["&&","||","!!","!|","==","!=","<=",">=","<",">"]
logic_casio=["And","Or","Not", "Xor","=","È","É","Ê","<",">"]
transpileWithComments = False

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
    print(strings)
    print(var)


    
         
def cleanCode():
    i=0
    while i < len(code):
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
    global LINES
    LINES = []
    queue = []
    for i in range(0, len(code)):
        split = splitLine(code[i])

        ### STR ###
        if split[0] == "Str":
            if(len(split)>1 and checkUnused(split[1])==(-1,-1)):
                strings.append(split[1])
                txt=concatToString(split[3:])
                if not txt=="//ERROR":
                    if "=" in code[i]:
                        LINES.append(txt+"ãStr "+str(len(strings)))
                    else:
                        LINES.append(txt+"Str "+str(len(strings)))

                else:
                   print("Error at line ", i, ": Num variables can't be used in concatenations")


            elif(len(split)==1):
                print("Error at line ", i, ": name expected after 'Str' declaration")

            else:
                print("Error at line ", i, ": a variable with the name ", split[1], " is already registered")

        ### NUM ###
        if split[0] == "Num":
            if(len(split)>1 and checkUnused(split[1])==(-1,-1)):
                var.append(split[1])
                txt=opToString(split[3:])
                if not txt=="//ERROR":
                    if "=" in code[i]:
                        LINES.append(txt+"ã"+char[len(var)])
                    else:
                        LINES.append(txt+char[len(var)])

                else:
                   print("Error at line ", i, ": Str variables can't be used in operations")

            elif(len(split)==1):
                print("Error at line ", i, ": name expected after 'Str' declaration")

            else:
                print("Error at line ", i, ": a variable with the name ", split[1], " is already registered")

        ### STATEMENT + QUEUE###
        if split[0] in statement:
            cap = split[0][0].capitalize()+split[0][1:]
            LINES+=cap
            LINES+=" "
            LINES+=conditionToString(split[1:])
            queue.append(getStatementEnd(cap))

        if split[0]=='}':
            LINES+=queue.pop()
        

        LINES[-1]+="Ù\n"
        
    file = open("casio.txt",'w', encoding="utf8")
    file.writelines(LINES)
    file.close()
    
    

        
    
def getNumIndex(name):
    for i in range (0, len(var)):
        if var[i][0]==name:
            return i
    return -1
            
def getStrIndex(name):
    if len(strings)>0:
        for i in range (1, len(strings)):
            if strings[i][0]==name:
                return i
    return -1

def checkUnused(name):

    for i in range(1, len(strings)):
        if name == strings[i]:
            return (0,i)
    for i in range(0, len(var)):
        if name == var[i]:
            return (1,i)
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
            while i<len(string) and string[i] in math+cond+"(){}.":
                temp += string[i]
                i+=1
            result.append(temp)

        elif(string[i] in "(){}."):
            result.append(string[i])
            i+=1
        
        elif(string[i] in blank):
            i+=1
        else:
            # Error, unexpected character
            i+=1
    return result

def opToString(split):
    final=''
    par="+-ÀÁ^="
    for i in range(0, len(split)):
        u=checkUnused(split[i]) 
        if u[0]==0:
            final="//ERROR"
            break
        elif(u[0]==1):
            final+=char[u[1]]
        elif(split[i] in math):
            final+= par[math.index(split[i])]
        else:
            final+=split[i].replace('i','½')
    
    return final
            

def concatToString(split):
    par=0
    final=""
    if len(split)==1:
        if split[0][0]=='"' and split[0][-1]=='"':
            return split[0]
        elif checkUnused(split[0])[0]==0:
            return "Str "+str(checkUnused(split[0])[1])
    elif split[1]=='+' and len(split)>=3:
        for i in range(0, len(split),2):
            if i+2<len(split) and split[i+1]=="+":
                if split[i][0]=='"' and split[i][-1]=='"':
                    final+="StrJoin("+split[i]+","
                    par+=1
                elif checkUnused(split[i])[0]==0:
                    final+="StrJoin(Str "+str(checkUnused(split[i])[1])+","
                    par+=1
                else:
                    return "//ERROR_A"
            elif i==len(split)-1:
                if split[i][0]=='"' and split[i][-1]=='"':
                    final+=split[i]
                elif checkUnused(split[i])[0]==0:
                    final+="Str "+str(checkUnused(split[i])[1])
                else:
                    return "//ERROR_B"
                
            else:

                return "//ERROR_C"
        final+=")"*par

        return final

def conditionToString(split):
    final = ""
    
    for i in range(0,len(split)):
        print(split[i])
        
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
            
