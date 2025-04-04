def main():
    """
    This program reads a CSV file containing student numbers and names,
    validates the student number input by the user, and retrieves the
    corresponding student name if the number is valid.
    It uses a dictionary to store the student numbers and names for
    efficient lookup.
    The program also includes a function to validate the student number
    format and a function to clean the input by removing any leading
    or trailing whitespace.
    """
    filename = "students.csv"
    key_column_index = 0
    students_dict = read_dictionary(filename, key_column_index)

    i_number = input("Enter the student number: ")
    error_message = validate_student_number(i_number)

    if error_message:
        print(error_message)
    else:
        cleaned_i_number = clean_i_number(i_number)
        student_name = students_dict.get(cleaned_i_number)
        if student_name:
            print(f"Student name: {student_name}")
        else:
            print("Student not found.")

if __name__ == "__main__":
    main()