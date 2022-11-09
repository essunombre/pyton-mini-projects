def format_name(first_name, last_name):
    """take a first and last name and format it,
    to return the title case version of the inputs"""
    formated_f_name = first_name.title()
    formated_l_name = last_name.title()
    return f"{formated_f_name} {formated_l_name}"

#si uso return necesito guardar la funcion en un avariable
#el return le dice que ahi se acaba la funcion
test = format_name("JOSE", "DAVid")
print(test)