from .htmlbuilder import HtmlBuilder
class TableGen(HtmlBuilder):
    """ This Module allows to create tables
    """
    def __init__(self, ClassName):
        """ Loads constructor of superclass and constructs HtmlCode
        with a table skeleton
        """
        super().__init__(ClassName)
        # Construct the bones of a table 
        self.HtmlCode = ("<table>\n\t<tr>\n"+
                        "\t\t<!-- Header -->\n"+
                        "\t</tr>\n\t<tr>\n"+
                        "\t\t<!-- Row_0 -->\n"+
                        "\t</tr>\n </table>\n")
        # debug print(self.HtmlCode)
    def add_html(self,prop, name,row=0):
        """ Overweites superclass method
        Creates main functionallity to modify a table... When done make the
        put stuff in superclass together
        returns string on error
        """
        code = ""
        tag = ""
        # Table Header
        if prop == "header":
            # Configurate the tag
            tag = "<th>"
            # If more than 1 header is given, iterate over each and put the
            # code together
            if(len(name) > 1):
                #headerS = ""
                for i in name:
                    code = code + "\t\t<th>"+i+"</th>\n"
            else:
                code = "\t\t<th>"+name[0]+"</th>\n"
                
            pos = self.find_html_index("\t\t<!-- Header -->\n")
        elif prop == "row":
            try:
                # Fi
                pos = self.find_html_index("\t\t<!-- Row_{} -->\n".format(row))
                if(pos != False):
                    code = "\t\t<tr>"+name+"</tr>\n"
                else:
                    # Todo Create a New row!
                    pass
                #super().add(pos, "<tr>", "\t\t<tr>"+name+"</tr>\n")
                #self.HtmlCode = self.HtmlCode[:pos]+ "\t\t<tr>"+name+"</tr>\n"
                #+ self.HtmlCode[pos:]
            except IndexError:
                return "Row not found"
            
        result = super().add_html(pos, code, tag)
        return "Done."