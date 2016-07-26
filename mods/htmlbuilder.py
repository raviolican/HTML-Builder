# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.
class HtmlBuilder(object):
    """ Class implements fundamental functionallity
    which is inherit to other modules
    """
    # className = ""
    def __init__(self, ClassName):
        """ Creating Class Instances
        Name  ClassName
        """
        self._Name = ClassName
        self._ClassName = ClassName
        self._HtmlCode = ""  
    @property
    def ClassName(self):
        """ Getter for the ClassName
        User ClassName to get it
        """
        return self._ClassName
    @ClassName.setter
    def ClassName(self,name):
        """ Setter for the ClassName
        Use ClassName = X to set it (see below property function
        """
        self._ClassName = name
        return self._ClassName
    # Returns index of the Html index
    def find_html_index(self,src):
        """ Finds the index of element src in HtmlCode
        returns integer position
        """
        if(self._HtmlCode.find(src)):
            return self._HtmlCode.index(src)
        else:
            return False
    def add_html(self,pos, html,tag=None):
        """ Adds a specific HTML into the given position
        returns string on error/success
        """
        # Todo: returns always None! So error catchin
        # does NOT work.
        try:
            self._HtmlCode = (self._HtmlCode[:pos]
                                    + html 
                                    + self._HtmlCode[pos:])
            #print(self.HtmlCode)
            return True
        except:
            return False
    def get_ids(self):
        """ Returns the ID of the objects
        returns integer with id/ string on error
        """
        return (self._Name,id(self))
    @property
    def HtmlCode(self):
        """ Returns the ID of the objects
        returns integer with id/ string on error
        """
        return (self._HtmlCode,id(self))
    @HtmlCode.setter
    def HtmlCode(self, value):
        self._HtmlCode = value