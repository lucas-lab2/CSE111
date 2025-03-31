def read_compound_list(filename):
    """Read the contents of a text file into a list where
    each line is stored as a separate element in the list.
    Replace all occurrences of 'AB' with 'Alberta' and count occurrences.
    
    Parameter:
        filename (str): The name of the text file to read.
    
    Returns:
        tuple: A list containing each line from the file and the count of 'Alberta'.
    """
    compound_list = []  # Initialize an empty list
    alberta_count = 0  # Local variable to count occurrences

    with open(filename, "rt") as txt_file:
        for line in txt_file:
            line = line.strip()
            if line == "AB":
                line = "Alberta"
            if line == "Alberta":
                alberta_count += 1
            compound_list.append(line)  # Append modified line to list

    # Remove first and last element
    compound_list = compound_list[1:-1]

    return compound_list, alberta_count  # Return both the list and the count


def main():
    # Read the contents of the provinces.txt file into a list and get count
    provinces_list, alberta_count = read_compound_list("Week 5/provinces.txt")

    # Print the entire list
    print(provinces_list)
    print(f"Number of times 'Alberta' appears: {alberta_count}")


if __name__ == "__main__":
    main()
