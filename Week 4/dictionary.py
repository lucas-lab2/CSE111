# bad_guys = {
#     'daredevil': 'kingpin',
#     'batman': 'bane',
#     'x-men': 'magneto',
#     'avengers': 'loki',
# }
# print(bad_guys['daredevil'])

def main():

    students_dict = {
        "42-039-4736": "Clint Huish",
        "61-315-0160": "Amelia Davis",
        "10-450-1203": "Ana Soares",
        "75-421-2310": "Abdul Ali",
        "07-103-5621": "Amelia Davis"
    }
    students_dict["81-298-9238"] = "Soma Patel"
    students_dict.pop("61-315-0160")
    length = len(students_dict)

    print(students_dict)
    print()
    # Get a student ID from the user.
    id = input("Enter a student ID: ")
    # Check if the student ID is in the dictionary.
    if id in students_dict:
        # Find the student ID in the dictionary and
        # retrieve the corresponding student name.
        name = students_dict[id]
        # Print the student's name.
        print(name)
    else:
        print("No such student")
# Call main to start this program.

    print(f"The dictionary has {length} students.")
if __name__ == "__main__":
    main()