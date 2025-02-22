import time 

my_time = int(input("Enter the time in seconds: "))

for x in range(my_time, 0, -1): # You could also use the reversed function, i.e: for x in reversed(range(0, my_time))
    print(x)
    time.sleep(2)

print("Time's Up")