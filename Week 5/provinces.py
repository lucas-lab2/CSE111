def read_compound_list(filename):
    """Read the contents of a text file into a list where
    each line is stored as a separate element in the list.
    Replace all occurrences of 'AB' with 'Alberta'.
    
    Parameter:
        filename (str): The name of the text file to read.
    
    Returns:
        list: A list containing each line from the file as a separate element.
    """
    compound_list = []  # Initialize an empty list

    with open(filename, "rt") as txt_file:
        # Read each line one by one
        for line in txt_file:
            # Strip whitespace/newlines and check if it is "AB"
            line = line.strip()
            if line == "AB":
                line = "Alberta"
            compound_list.append(line)  # Append modified line to list
    compound_list = compound_list[1:-1]
    return compound_list


def main():
    # Read the contents of the provinces.txt file into a list
    provinces_list = read_compound_list("Week 5/provinces.txt")

    # Print the entire list
    print(provinces_list)


if __name__ == "__main__":
    main()
