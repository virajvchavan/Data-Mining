#2014BIT026
def bins_by_freq(elements, bins_count):
	output = {}
	for j in range(bins_count):
		output[j] = []
	#for i in range(len(elements)):
	#	output[i%bins_count].append(elements[i])	
	width = int(len(elements)/bins_count)
	pos = 0	
	for i in range(bins_count):
		output[i].extend(elements[pos: pos+width])
		pos += width
		
	return output

def bins_by_width(elements, bins_count):	
	output = {}
	for j in range(bins_count):
		output[j] = []
	bin_size = int(max(elements)/bins_count)
	
	print("Width is: ", bin_size, "\n")
	
	#define data ranges
	bin_ranges = []
	for i in range(bins_count):		
		bin_ranges.append([i*bin_size+1, (i*bin_size)+bin_size+1])
		
	for element in elements:
		for k in range(bins_count):
			if(element < bin_ranges[k][1] and element >= bin_ranges[k][0]):
				output[k].append(element)
			
	return output
	

elements_count = int(input("Enter number of elements: "))
print("Enter ", elements_count, "elements: ")
elements = []
for i in range(elements_count):
	elements.append(int(input())) 

bins_count = int(input("Enter number of bins: "))

print("Bins by width: ", bins_by_width(elements, bins_count), "\n\n")

print("Bins by frequency: ", bins_by_freq(elements, bins_count), "\n\n")


