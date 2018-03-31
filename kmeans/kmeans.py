import copy, math, pdb

k = input("Enter k:")

def read_data_set():
	return [[2,3],[8,4],[4,15],[1,13],[8,3],[9,5],[6,4]]

def find_initial_means(data_set, k):
	return [[2, 3],[8,3],[6,4]]

def recalculate_means(clusters):
	means = []
	for cluster in clusters:
		if(len(cluster) > 0):
			total_x = 0
			total_y = 0
			for point in cluster:
				total_x += point[0]
				total_y += point[1]
			# pdb.set_trace()
			mean = [total_x/len(cluster), total_y/len(cluster)]
			means.append(mean)
	return means

def calculate_distance(point1, point2):
	return math.sqrt(((point1[0] - point2[0])**2) + ((point1[1] - point2[1])**2))

def assign_clusters(data_set, means, k):
	clusters = [[] for _ in range(k)]
	for point in data_set:
		min_distance = calculate_distance(means[0], point)
		min_distance_index = 0
		for index, mean in enumerate(means[1:]):
			if(calculate_distance(mean, point) < min_distance):
				min_distance_index = index
		clusters[min_distance_index].append(point)
		# pdb.set_trace()
	return clusters

data_set = read_data_set()
means = find_initial_means(data_set, k)
old_means = copy.deepcopy(means)
while True:
	print("Means: " + str(means))
	clusters = assign_clusters(data_set, means, k)
	means = recalculate_means(clusters)
	if(means == old_means):
		break
	else:
		old_means = copy.deepcopy(means)

print("Final Means: " + str(means))




