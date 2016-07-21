# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

# Prints the ID of any instance
def getIds(objects):
    for i in objects:
        print(i,id(i))
