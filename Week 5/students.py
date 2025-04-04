def read_dictionary(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters:
        filename: the name of the CSV file to read.
        key_column_index: the index of the column to use as the key.

    Return: a dictionary that maps keys to lists of remaining columns.
    """
    students = {}
    with open(filename, "r") as file:
        next(file)  # Skip the header line
        for line in file:
            parts = line.strip().split(",")
            key = parts[key_column_index]
            value = parts[:key_column_index] + parts[key_column_index + 1:] # Exclude the key column
            students[key] = value[0] if value else ""
    return students # Store the rest of the columns as a list

def clean_i_number(i_number):
    """ Remove dashes and return cleaned I-Number"""
    return i_number.replace("-", "").strip()

def validate_student_number(i_number):
    """Validate the I-Number and return a message or None if valid."""
    if not all(c.isdigit() or c == "-" for c in i_number):
        return "Invalid I-Number"
    cleaned = clean_i_number(i_number)
    if len(cleaned) < 9:
        return "Invalid I-Number: too few digits"
    elif len(cleaned) > 9:
        return "Invalid I-Number: too many digits"
    return None

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