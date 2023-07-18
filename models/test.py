def default( line):
    """Handle the <class name>.all() command"""
    class_name, _, command = line.partition(".")
    if command.startswith("update"):
        # User.update("4726cdcc-50e2-48b0-aebc-9fd403a36d8e", "first_name", "John")
        # update User 4726cdcc-50e2-48b0-aebc-9fd403a36d8e first_name "Emma"
        func, _, others = command.partition("(")
        args = others.split(", ")
        id = args[0].strip("\"")
        name = args[1]
        value = args[2].strip(")")
        stripped_command = f"{class_name} {id} {name} {value}"
        print(stripped_command)


default("User.update(\"4e4bb38e-90de-4af8-b962-3d02d431f3cd\", \"age\", 89")
