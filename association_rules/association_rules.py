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

def print_rules(rules):
	#[start, end, confidence]
	for rule in rules:
		print(str(rule[0]) + "\t\t-------->\t\t" + str(rule[1]) + "\t\t" + str(rule[2]))

dataset = read_dataset('market.csv')
min_freq_perc = 40
min_freq = math.ceil((min_freq_perc/100.0)*len(dataset['data']))
min_support_perc = 50

rules = []
for l in range(2, len(dataset['items']) + 1):
	itemset = get_itemsets(dataset['data'], dataset['items'], l)
	if(len(itemset) == 0):
		break
	# print("Level: " + str(l) + ": \n" + str(itemset) + "\n\n")
	for s in itemset:
		freq_s = get_freq(dataset['data'], dataset['items'], s)
		for i in range(0, len(s) - 1):
			x = s[0:i+1]
			y = s[i+1:]
			freq_x = get_freq(dataset['data'], dataset['items'], x)
			c = float(freq_s)/float(freq_x)
			if c*100 >= min_support_perc:
				rules.append([x, y, c])

print("\nGenerated Rules: \nGenerated")
print_rules(rules)

