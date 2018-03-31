import copy, math, pdb, csv, random

k = input("Enter k:")

def read_data_set():
	with open('file.csv', 'rU') as f:
		return [list(map(int, rec)) for rec in csv.reader(f, delimiter=',')]

def find_initial_means(data_set, k):
	means = []
	i = 0
	while i < k:
		rand_mean = data_set[random.randint(0, len(data_set) - 1)]
		if(rand_mean not in means):
			means.append(rand_mean)
			i += 1
		else:
			i -= 1
	return means

def recalculate_means(clusters):
	means = []
	for cluster in clusters:
		total_x = 0
		total_y = 0
		for point in cluster:
			total_x += point[0]
			total_y += point[1]
		mean = [round((float(total_x)/len(cluster)),2), round(float(total_y)/len(cluster), 2)]
		means.append(mean)
	return means

def calculate_distance(point1, point2):
	return math.sqrt(((point1[0] - point2[0])**2) + ((point1[1] - point2[1])**2))

def assign_clusters(data_set, means, k):
	clusters = [[] for _ in range(k)]
	for point in data_set:
		min_distance = calculate_distance(means[0], point)
		min_distance_index = 0
		for i in range(1, len(means)):
			if(calculate_distance(means[i], point) < min_distance):
				min_distance_index = i
				min_distance = calculate_distance(means[i], point)
		clusters[min_distance_index].append(point)
	return clusters

data_set = read_data_set()
means = find_initial_means(data_set, k)
old_means = copy.deepcopy(means)
clusters = []
while True:
	print("Means: " + str(means))
	clusters = assign_clusters(data_set, means, k)
	means = recalculate_means(clusters)
	if(means == old_means):
		break
	else:
		old_means = copy.deepcopy(means)

print("Final Means: " + str(means))
print("Clusters: \n............................................." )
for cluster in clusters:
	print(cluster)




