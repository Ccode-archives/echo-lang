var = []
varnames = []
varvalues = []

while True:
    # variable setup
    varnames = []
    varvalues = []
    for string in var:
        varnames.append(string.split(":=")[0])
        varvalues.append(string.split(":=")[1])
    # debug
    #print("varnames:", end = " ")
    #print(varnames)
    #print("varvalues:", end = " ")
    #print(varvalues)
    #print("var:", end = " ")
    #print(var)
    inp = input(">>")
    
    # variable handler
    if ":=" in inp:
        counter = 0
        varnum = 0
        out = False
        for string in var:
            varname = inp.split(":=")[0]
            varin = string.split(":=")[0]
            if varname == varin:
                out = True
                varnum = counter
            counter += 1
        if not out:
            var.append(inp)
        else:
            var[varnum] = inp
    # replace varnames with values
    varcounter = 0
    for string in varnames:
        inp = inp.replace(string, varvalues[varcounter])
        varcounter += 1
    
    # debug
    #print("inp: " + inp)
    
    # commands
    if inp == "exit":
        break
    elif inp.startswith("print "):
        com = inp.replace("print ", "")
        print(com)
    else:
        if not ":=" in inp:
            print("syntax error")
