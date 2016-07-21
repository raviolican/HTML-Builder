# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

class htmlBuilder:
    def __init__(self):
        self.htmlCode = ""
    def generate_table(self, className, header, *vals):
        self.htmlCode += "<table class='"+className+"'>\n"
        # make headers
        self.htmlCode += "\t<tr>\n"
            
        for i in header:
            self.htmlCode += "\t\t<th>"+i+"</th>\n"
            
        self.htmlCode += "\t</tr>\n"
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

build = htmlBuilder()
form = build.generate_table("tester", ("Test","Nocheiner","Hello"), "1","Base","2", "Rain","3","schnaggaschnagga")
print(form)

