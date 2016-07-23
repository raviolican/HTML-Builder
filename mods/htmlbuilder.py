# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.
class HtmlBuilder(object):
    """ Class implements fundamental functionallity
    which is inheritted by other modules
    """
    # className = ""
    def __init__(self, ClassName):
        """ Creating Class Instances
        Name  ClassName
        """
        self.Name = ClassName
        self._ClassName = ClassName
        self.HtmlCode = ""  
    def set_ClassName(self,name):
        """ Setter for the ClassName
        Use ClassName = X to set it (see below property function
        """
        self._ClassName = name
        return self._ClassName
    def get_ClassName(self):
        """ Getter for the ClassName
        User ClassName to get it
        """
        return self._ClassName
    # Returns index of the Html index
    def find_html_index(self,src):
        """ Finds the index of element src in HtmlCode
        returns integer position
        """
        if(self.HtmlCode.find(src)):
            return self.HtmlCode.index(src)
        else:
            return False
    def add_html(self,pos, html,tag=None):
        """ Adds a specific HTML into the given position
        returns string on error/success
        """
        # Todo: returns always None! So error catchin
        # does NOT work.
        try:
            self.HtmlCode = (self.HtmlCode[:pos]
                                    + html 
                                    + self.HtmlCode[pos:])
            #print(self.HtmlCode)
            return True
        except:
            return False
    def get_ids(self):
        """ Returns the ID of the objects
        returns integer with id/ string on error
        """
        return (self.Name,id(self))
    ClassName = property(get_ClassName,set_ClassName)