import math
from itertools import combinations
data = [[1,0,1,1,0,0],
				[0,0,0,1,1,0],
				[0,1,1,1,0,0],
				[1,1,0,1,1,1],
				[1,0,1,0,0,1]]
items = ['a', 'b', 'c', 'd', 'e', 'f']

min_support = 40
min_freq = math.ceil((min_support/100.0)*len(data))

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

print get_itemsets(data, items, 2)