import math

items = int(input("Please enter the number of items: "))
boxes = int(input("Please enter the number of items per box: "))
full_boxes = math.ceil(items / boxes)
print(f"For {items} items, packing {boxes} items in each box, you will need {full_boxes} boxes.")
