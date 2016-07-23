# Import Classes
from mods import *
import re
myObjects = {}

while True:
    # Split the command
    cmd = input("> ").split(" ")
    # Initiate table object and store it in the list
    if(cmd[0] == "table"):
        name = cmd.pop(1)
        try:
            myObjects[name] = TableGen(name)
        except IndexError:
            myObjects[name] = TableGen(name)
        continue   
    # Get ID's of current objects    
    elif(cmd.pop(0) == "idinfo"):
        try:
            inptObjects = cmd[0].split(",")
            print(inptObjects)
            if not all(inptObjects):
                raise IndexError   
        except IndexError:
            # Trying to fix False instances in list
            length = len(inptObjects)
            newitems = []
            for v in range(length):
                if inptObjects[v]:
                    newitems.append(inptObjects[v])
                # String is false
                else:
                    continue
            else:
                # List empty now? Stop this process
                if len(inptObjects) == 0:
                    raise AttributeError
                inptObjects = newitems
        except AttributeError:
            print("Please provide one or more name(s) seperated by comma of "
                + "your table or use tables() to get all tables.")
            continue
        finally:
            for i in inptObjects:
                if i not in myObjects:
                    print ("Cannot find table \""+i +"\"")
                else:
                    idinfo = list(myObjects[i].get_ids())
                    print("Id for table \""+idinfo[0]+"\"",format(idinfo[1]))
        
    # Executes commands
    elif cmd[0] in myObjects:
        if cmd[1] == "getclass":
            print(myObjects[cmd[0]]._ClassName)   
        elif cmd[1] == "setclass":
            if(cmd[2] in cmd):
                myObjects[cmd[0]]._ClassName = cmd[2]
            else:
                print("Expecting 3rd paramenter")
        # Add a new Tag to the table
        elif cmd[1] == "add":
            if cmd[2] == "header":
                result = myObjects[cmd[0]].add_html("header",cmd[3:])
                print(result)
            elif cmd[2] == "row":
                try:
                    result = myObjects[cmd[0]].add_html("row",cmd[3],cmd[4])    
                except:
                    result = myObjects[cmd[0]].add_html("row",cmd[3])
                print(result)
        else:
            print("Command not found")
            continue  
    else:
        print("Command not found")
        continue
