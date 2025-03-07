age =  int(input ("Please enter your age: "))
max_heart_rate = 220 - age
target_heart_rate = 0.65 * max_heart_rate
target_heart_rate2 = 0.85 * max_heart_rate
print (f"When you exercise to strengthen your heart, you should keep your heart rate between {target_heart_rate: .1f} and {target_heart_rate2: .1f} beats per minute.")