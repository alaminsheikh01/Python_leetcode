# How to find average of N numbers in python

num = int(input("How many numbers ?"))
total_sum = 0;

for n in range(num):
    numbers = float(input("Please enter numbers ? "))
    total_sum += numbers

avg = total_sum/num

print("The average is", avg)