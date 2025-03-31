def read_compound_list(filename):
    """Read the contents of a text file into a list where
    each line is stored as a separate element in the list.
    Replace all occurrences of 'AB' with 'Alberta'.
    
    Parameter:
        filename (str): The name of the text file to read.
    
    Returns:
        list: A list containing each line from the file as a separate element.
    """
    # Open the file and read lines
    with open(filename, "rt") as txt_file:
        lines = txt_file.readlines()  # Read all lines into a list

    # Strip newline characters and replace 'AB' with 'Alberta'
    cleaned_lines = [line.strip().replace("AB", "Alberta") for line in lines]

    return cleaned_lines


def main():
    # Read the contents of the provinces.txt file into a list
    provinces_list = read_compound_list("Week 5/provinces.txt")

    # Print the entire list
    print(provinces_list)


if __name__ == "__main__":
    main()
