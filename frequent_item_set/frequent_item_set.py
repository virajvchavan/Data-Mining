from itertools import combinations
import csv, math
from ast import literal_eval

def read_dataset():
	with open('dataset.csv', 'rU') as f:
		return list(csv.reader(f, delimiter=','))

def print_dataset():
	for data in dataset:
		print(data)

def is_element_in_data(ele, data):
	# ele = [1,2]
	# data = [4,2,5,1,6,2]
	for e in ele:
		if e not in data:
			return False
	return True

dataset = read_dataset()
min_support = int(math.ceil(len(dataset)*float(60/100.0)))

def get_unique_elements(dataset):
	unique_elements = []
	for ele in dataset:
		for e in ele:
			if e not in unique_elements:
				unique_elements.append([e])
	return unique_elements

def get_supported_elements(dataset, elements):
	count_hash = {}
	for ele in elements:
		count_hash[repr(ele)] = 0
		for data in dataset:
			if is_element_in_data(ele, data):
				count_hash[repr(ele)] += 1
	valid_elements = []
	for e, count in count_hash.items():
		if(count >= min_support):
			valid_elements.append(literal_eval(e))
	return valid_elements

unique_elements = get_unique_elements(dataset)

print_dataset()
print
print("Unique: ", unique_elements)
print(get_supported_elements(dataset, unique_elements))