#first try with the first chapter of Promessi Sposi
file = open ("/home/giovanni/Documenti/Texts/promessiSposi.txt", "r")

#the dictionary "result" is the map with (key, value) as (word, numberOfOccurences)
result = {}
print(file.read())
tmpString  = ""
#exceptions in the text
def apostrophe(tmpString):
    tmpString = tmpString + char
    if(result.has_key(tmpString)):
        for k in result.keys():
            if(k == tmpString):
                result[k] = result.get(k) + 1
                tmpString = ""
    else:
        result[tmpString] = 1
        tmpString = ""

def comma():
    return
def column():
    return
def newLine():
    return
def minus():
    return
def question():
    return
def exclamation():
    return
def semiColumn():
    return
def point():
    return
def default(tmpString):
    tmpString = tmpString + char
def space(tmpString):
    if(result.has_key(tmpString)):
        for k in result.keys():
            if(k == tmpString):
                result[k] = result.get(k) + 1
                tmpString = ""
    else:
        result[tmpString] = 1
        tmpString = ""
    
def options(x, tmpString):
        if(x == ","):
            comma() 
        elif(x== "\n"):
            newLine()
        elif(x == "-"):
            minus()
        elif(x == "?"):
            question()
        elif(x == "!"):
            exclamation()
        elif(x== ";"):
            semiColumn()
        elif(x== "."):
            point()
        elif(x== "'"):
            apostrophe(tmpString)
        elif(x == " "):
            space(tmpString)
        else:
            default(tmpString)
        


char = file.read(1)


options(char, tmpString)

    
while char != "":
    char = file.read(1)
    options(char, tmpString)
    
for k in result.keys():
    print(k, result.get(k))

 
 
    
    

    
    
    
    

    
    
    



      

