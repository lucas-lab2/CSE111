def get_inital_name (name):
    inital = name[0:1]
    return inital

first_name = get_inital_name(input("Enter your first name: "))
last_name = get_inital_name(input("Enter your last name: "))
print("Your initials are: " + first_name + last_name)