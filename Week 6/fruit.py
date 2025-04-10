def reverse_list(fruit_list):
    """Reverse the order of the elements in a list.
    Parameter fruit_list: a list of strings
    Return: None
    """
    fruit_list.reverse()
    return fruit_list
def add_fruit(new_fruit):
    new_fruit.append("Orange")
    return new_fruit

def find_fruit(fruit_list):
    if "apple" in fruit_list:
        index = fruit_list.index("apple")#find the index of "apple"
        fruit_list.insert(index, "cherry")#add "cherry" before "apple"
    return fruit_list

def remove_fruit(fruit_list):
    if "Orange" in fruit_list:
        index = fruit_list.index("Orange")
        fruit_list.pop(index)
    return fruit_list

def remove_last_fruit(fruit_list):
    fruit_list.pop()
    return fruit_list

def remove_banana(fruit_list):
    fruit_list.remove("banana")
    return fruit_list

def main():
# Create and print a list named fruit.
    fruit_list = ["pear", "banana", "apple", "mango"]
    print(f"original: {fruit_list}")
    # Reverse the order of the elements in fruit_list.
    
    reverse_fruit = reverse_list(fruit_list)
    print(f"reverse_list: {reverse_fruit}")

    new_fruit = add_fruit(fruit_list)
    print(f"new_fruit: {new_fruit}")

    add_cherry = find_fruit(fruit_list)
    print(f"add_cherry: {add_cherry}")

    remove_orange = remove_fruit(fruit_list)
    print(f"remove_orange: {remove_orange}")

    remove_last = remove_last_fruit(fruit_list)
    print(f"remove_last: {remove_last}")

    remove_banan = remove_banana(fruit_list)
    print(f"remove_banana: {remove_banan}")
main()


