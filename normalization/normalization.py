#2014BIT026
import math

def calc_min_max(i, mini, maxi, new_max, new_min):
	return new_min + (new_max - new_min)*((i - mini)/(maxi-mini))

def min_max_norm(elements):
	output = []
	new_min = int(input("Input new Min: "))
	new_max = int(input("Input new Max: "))

	for i in elements:
		output.append(calc_min_max(i, min(elements), max(elements), new_max, new_min))

	return output

def calc_std_deviation(elements, mean):
	summation = 0
	for i in elements:
		summation += ((i-mean)*(i-mean))
	
	return math.sqrt(summation/(len(elements)-1))

def z_score_norm(elements):
	output = []
	mean = sum(elements)/len(elements)
	for i in elements:
		output.append((i-mean)/calc_std_deviation(elements, mean))

	return output

elements_count = int(input("Enter number of elements: "))
print("Enter ", elements_count, "elements: ")
elements = []
for i in range(elements_count):
	elements.append(int(input())) 

print("Min Max normalization: " + str(min_max_norm(elements)))
print("Z-score normalization: " + str(z_score_norm(elements)))
