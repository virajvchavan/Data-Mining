import math
from itertools import combinations

def read_dataset(filename):
	lines = open(filename).readlines()
	items = lines[0].split(',')
	data = []
	for line in lines[1:]:
		data.append(list(map(int, line.split(','))))
	return { 'items': items, 'data': data }

def get_freq(data, items, combination):
	freq = 0
	for row in data:
		temp = 1
		for i in combination:
			temp *= row[items.index(i)]
		if temp >= 1:
			freq += 1
	return freq

def get_itemsets(data, items, level):
	sets = set(combinations(items, level))
	item_sets = []
	for s in sets:
		if(get_freq(data, items, s) >= min_freq):
			item_sets.append(s)
	return item_sets

dataset = read_dataset('market.csv')
min_support = 40
min_freq = math.ceil((min_support/100.0)*len(dataset['data']))

for l in range(2, len(dataset['items']) + 1):
	itemset = get_itemsets(dataset['data'], dataset['items'], l)
	if(len(itemset) == 0):
		break
	print("Level: " + str(l) + ": \n" + str(itemset) + "\n\n")