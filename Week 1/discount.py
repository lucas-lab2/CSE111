total = 0
disccount = 0
subtotal = 0

while True:




    while True:
        cont = int(input("Do you want to continue? 1 - Yes 0 - No: "))
        if cont == 1 or cont == 0:
            break  # leave loop
        print("Invalid input. Please enter 1 or 0.")
        
    if cont == 0:
        break
    
 