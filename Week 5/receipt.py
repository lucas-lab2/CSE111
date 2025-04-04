import csv
def read_dictionary(filename, key_column_index):
  """Read the contents of a CSV file into a compound
  dictionary and return the dictionary.
  Parameters
      filename: the name of the CSV file to read.
      key_column_index: the index of the column
          to use as the keys in the dictionary.
  Return: a compound dictionary that contains
      the contents of the CSV file.
  """
  dictionaty = {}
  with open(filename, mode="r", newline="") as csv_file:
    reader = csv.reader(csv_file) # Read the CSV file
    next(reader) # Skip the header line
    for row in reader:
       if len(row) == 0: # Skip empty rows
            continue
       key = row[key_column_index]
       dictionaty[key] = [row[0], row[1], float(row[2])]
    return dictionaty # Store the rest of the columns as a list

def main():


if __name__ == "__main__":
    main()