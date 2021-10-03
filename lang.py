variables = {}

while True:
    inp = input(">>").lstrip()
    variable_assigned = False

    # variable handler
    if ":=" in inp:
        var_name, var_value, *_ = inp.split(":=")
        var_name = var_name.strip()
        if ' ' not in var_name and var_value:
            variables[var_name] = var_value
            variable_assigned = True

    # replace variable names with values
    for var_name, var_value in variables.items():
        inp = inp.replace(f"{var_name}$", var_value)

    inp = inp or "No content"

    # commands
    if inp == "exit":
        break
    elif inp.startswith("print "):
        print(inp[6:])
    elif not variable_assigned:
        print(f"syntax error - ({inp})")
