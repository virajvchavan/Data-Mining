import math
from itertools import combinations

def read_dataset(filename):
	lines = open(filename).readlines()
	items = lines[0].split(',')
	data = []
	for line in lines[1:]:
		data.append(list(map(int, line.split(','))))
	return { 'items': items, 'data': data }

def get_freq(data, items, s):
	freq = 0
	for d in data:
		temp = 1
		for i in s:
			temp *= d[items.index(i)]
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

dataset = read_dataset('dataset.csv')
min_support = 40
min_freq = math.ceil((min_support/100.0)*len(dataset['data']))
print get_itemsets(dataset['data'], dataset['items'], 2)