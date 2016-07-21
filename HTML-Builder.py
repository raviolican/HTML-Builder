# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.
import htmlInfos
class HtmlBuilder:
    #className = ""
    def __init__(self):
        print("hi world")
        self.Name = ""
        self.ClassName = "name"
        self.HtmlCode = ""  
    def setClass(self,name):
        self.className = name
        return self.ClassName
    def getClass(self):
        return self.ClassName
    def findHtmlIndex(self,src):
        if(self.HtmlCode.find(src)):
            return self.HtmlCode.index(src)
        else:
            return False
        
class TableGen(HtmlBuilder):
    def __init__(self):
        super().__init__()
        self.HtmlCode = ("<table>\n\t<tr>\n"+
                        "\t\t<!-- Header -->\n"+
                        "\t</tr>\n\t<tr>\n"+
                        "\t\t<!-- Row_0 -->\n"+
                        "\t</tr>\n </table>\n")
        # debug print(self.HtmlCode)
    
    def addHeader(self, name):  
        #print(name)
        headerS = ""
        if(len(name) > 1):
            headerS = ""
            for i in name:
                headerS = headerS + "\t\t<th>"+i+"</th>\n"
        else:
            headerS = "\t\t<th>"+name[0]+"</th>\n"
            
        print(headerS)
                
        pos = self.findHtmlIndex("\t\t<!-- Header -->\n")
        self.HtmlCode = self.HtmlCode[:pos]+ headerS + self.HtmlCode[pos:]
        print(self.HtmlCode)
    def addRow(self,row,name):
        print("\t\t<!-- Row_{} -->\n".format(row))
        pos = self.findHtmlIndex("\t\t<!-- Row_{} -->\n".format(row))
        if pos:
            self.HtmlCode = self.HtmlCode[:pos]+ "\t\t<tr>"+name+"</tr>\n" + self.HtmlCode[pos:]
        else:
            print("row doesn't exist!")
    
    def generate_table(self, className, header, *vals):
        HtmlBuilder.htmlCode += "<table class='"+className+"'>\n"
        # make headers
        HtmlBuilder.htmlCode += "\t<tr>\n"
        # Creating columnt headers    
        for i in header:
            HtmlBuilder.htmlCode += "\t\t<th>"+i+"</th>\n"    
        HtmlBuilder.htmlCode += "\t</tr>\n"
        n = 0
        length = len(vals)/len(header)
        self.htmlCode += "\t<tr>\n"
        # loop throught the values
        for i in vals:
            if n == len(header): 
                self.htmlCode += "\t</tr>\n"
                self.htmlCode += "\t<tr>\n"
                n = 0
            self.htmlCode += "\t\t<td>"+i+"</td>\n"
            n += 1
        self.htmlCode += "\t</tr>\n</table>"
        
        return self.htmlCode


myObjects = {}
while True:
    # Split the command
    cmd = input("> ").split(" ")
    # Initiate table object and store it in the list
    if(cmd[0] == "table"):
        myObjects[cmd[1]] = TableGen()
        continue   
    # Get ID's of current objects    
    elif(cmd[0] == "idinfo"):
        inptObjects = cmd[1].split(",")
        htmlInfos.getIds(inptObjects)
        
    # Executes commands
    elif cmd[0] in myObjects:
        if cmd[1] == "getclass":
            print(myObjects[cmd[0]].getClass())   
        elif cmd[1] == "setclass":
            if(cmd[2] in cmd ):
                myObjects[cmd[0]].setClass(cmd[2])
            else:
                print("Expecting 3rd paramenter")
        # Add a new Tag to the table
        elif cmd[1] == "add":
            if cmd[2] == "header":
                myObjects[cmd[0]].addHeader(cmd[3:])
            if cmd[2] == "row":
                myObjects[cmd[0]].addRow(cmd[3],cmd[3:])
                
                
        else:
            print("Command not found")
            continue  
    else:
        print("Command not found")
        continue

#        cmd[1] = TableGen()
#        print("Let's generate a table!")
#        while True:
#            work = input().split("=")
#            if work[0] =="setClass":
#                cmd[1].setClass(work[1].strip())
#                #print("Classname:"+table.setClass(cmd[1]))
#            elif work[0] == "getClass":
#                print(cmd[1].getClass())
#            elif work[0] == "q":
#                break
           
           






#build = htmlBuilder()
#form = build.generate_table("tester", ("Col1","Col2","Col3"), "Col1.val1","Col2.val1","Col3.val1", "Col1.val2","Col2.val2","Col3.val2")
#print(form)

