# names = ['Susan', 'Christopher']
# print(len(names))
# names.insert(0, 'Bill')
# print(names)
# names.sort()
# print(names) 

# names =['Susan', 'Christopher', 'Bill', 'Justin']
# presenters = names[1:3]
# print(names)
# print(presenters)

# person = {'first': 'Christopher'}
# person ['last'] = 'Harrison'
# print(person)
# print(person['first'])

# for name in ['Christopher', 'Susan']:
#     print(name)

# for index in range(0, 2):
#     print(index)

# names = ['Christopher', 'Susan']
# index = 0
# while index < len(names):
#     print(names[index]) # print the name at the current index
#     index = index + 1

# names = ['Christopher', 'Susan']
# index = len(names)  # This line is unnecessary for the loop

# for i in range(0, index):  # range(0, len(names)) will iterate over 0 and 1
#     print(names[i])

# Example 1
def main():
    # Create a list that contains five strings.
    colors = ["yellow", "red", "green", "yellow", "blue"]
    # Call the built-in len function
    # and print the length of the list.
    length = len(colors)
    print(f"Number of elements: {length}")
    # Print the element that is stored
    # at index 2 in the colors list.
    print(colors[2])
    # Change the element that is stored at
    # index 3 from "yellow" to "purple".
    colors[3] = "purple"
    # Print the entire colors list.
    print(colors)
# Call main to start this program.
if __name__ == "__main__":
    main()