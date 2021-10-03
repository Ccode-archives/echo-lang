variables = {}

while True:
    # debug
    #print(variables)
    try:
        inp = input(">>").lstrip()
        variable_assigned = False

        # replace variable names with values
        for var_name, var_value in variables.items():
            inp = inp.replace(f"{var_name}$", var_value)

        # variable handler
        if ":=" in inp:
            var_name, *var_value = inp.split(":=")
            var_name, var_value = var_name.strip(), ':='.join(var_value)
            if ' ' not in var_name and var_value:
                variables[var_name] = var_value
                variable_assigned = True

        inp = inp or "No content"

        # commands
        if inp == "exit":
            print("Exiting.")
            break
        elif inp.startswith("print "):
            print(inp[6:])
        elif not variable_assigned:
            print(f"syntax error - ({inp})")
    except:
        print("\nExiting.")
        break
