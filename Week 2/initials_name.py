def get_initial_name(name, force_uppercase):
    if force_uppercase:
        initial = name[0:1].upper()  # get the first letter of the name and convert it to uppercase the [0:1] means that we are getting the first letter of the name
    else:
        initial = name[0:1]
    return initial

first_name = get_initial_name(input("Enter your first name: "), True)
middle_name = get_initial_name(input("Enter your middle name: "), False)
last_name = get_initial_name(input("Enter your last name: "), True)
print("Your initials are: " + first_name + middle_name + last_name)