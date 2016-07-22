from mods import *

myObjects = {}
while True:
    # Split the command
    cmd = input("> ").split(" ")
    # Initiate table object and store it in the list
    if(cmd[0] == "table"):
        try:
            myObjects[cmd[1]] = TableGen(cmd[1])
        except IndexError:
            myObjects[cmd[1]] = TableGen("Class")
        continue   
    # Get ID's of current objects    
    elif(cmd[0] == "idinfo"):
        try:
            inptObjects = cmd[1].split(",")
            for i in inptObjects:
                if i not in myObjects:
                    print (i+" Not created yet")
                else:
                    myObjects[i].get_ids()
        except IndexError:
            print("Expecting 2nd parameter")
        
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
