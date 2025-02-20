# Python Compound Interest Calculator

principle = 0
rate = 0
time = 0

while principle <= 0: # You can also write this as, while True if you want the user to be able to enter 0. 
    principle = float(input("Enter the principle amount: "))
    if principle <= 0:
        print("Principle can't be less than or equal to zero")
    # If you use the while True method then you will need to break the loop via the following: 
    # else:
    #     break
while rate <= 0: # You can also write this as, while True if you want the user to be able to enter 0. 
    rate = float(input("Enter the interest rate: "))
    if rate <= 0:
        print("Interest rate can't be less than or equal to zero")
    # If you use the while True method then you will need to break the loop via the following: 
    # else:
    #     break
while time <= 0: # You can also write this as, while True if you want the user to be able to enter 0. 
    time = int(input("Enter the time in years: "))
    if time <= 0:
        print("Time can't be less than or equal to zero")
    # If you use the while True method then you will need to break the loop via the following: 
    # else:
    #     break

total = principle * pow((1 + (rate/100)), time)

print(f"Balance after {time} year/s: ${total:.2f}")
# print(principle)
# print(rate)
# print(time)