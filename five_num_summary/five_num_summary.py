#2014BIT026

# Q1: Minimum of all
# Q2: Lower Quartile
# Q3: Median
# Q4: Upper Quartile
# Q5: Maximum of all

import numpy as np
def findMedian(v):
    return np.median(v)
    
def fivenum(v):    
    v.sort()
    Q1 = min(v)
    Q5 = max(v)
    Q3 = findMedian(v)
    #print(len(v))
    if(len(v)%2 == 0):
        Q2 = findMedian(v[:int(len(v)/2)])
        Q4 = findMedian(v[int(len(v)/2):])
    else:
        Q2 = findMedian(v[:int((len(v)-1)/2)])
        Q4 = findMedian(v[int(1+(len(v)-1)/2):])
    
    return Q1, Q2, Q3, Q4, Q5,

print("\n\n****************FIVE NUMBER SUMMARY**************************\n\n")
n = int(input("How many numbers?"))
numbers = []
print("Enter " + str(n) + " numbers: ")
for i in range(n):
    numbers.append(int(input())) 

answer = fivenum(numbers)
print("\nHere is the five number summary: ")       
print("Min: " + str(answer[0]))
print("Lower Quartile: " + str(answer[1]))
print("Median: " + str(answer[2]))
print("Upper Quartile: " + str(answer[3]))
print("Max: " + str(answer[4]) + "\n\n")