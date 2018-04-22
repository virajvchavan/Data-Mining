from itertools import combinations
import csv, math
from ast import literal_eval

def read_dataset():
	with open('dataset.csv', 'rU') as f:
		return list(csv.reader(f, delimiter=','))

def print_dataset(somthing):
	for data in somthing:
		print(data)

def is_element_in_data(ele, data):
	# ele = [[1],[2]]
	# data = [4,2,5,1,6,2]
	for e in ele:
		if e.__class__.__name__ == 'list':
			if e[0] not in data:
				return False
		else:
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
				unique_elements.append(e)
	output = []
	for u in unique_elements:
		output.append([u])
	return output

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
print("Start: ", unique_elements)

unique_elements = get_supported_elements(dataset, unique_elements)
start_unique = unique_elements
print("\nUnique: ", start_unique)
level = 2
while(len(unique_elements) > 0):
	unique_elements = list(combinations(start_unique, level))
	unique_elements = list(map(list, unique_elements))
	unique_elements = get_supported_elements(dataset, unique_elements)
	print("\nUnique: ", unique_elements)
	level += 1

	