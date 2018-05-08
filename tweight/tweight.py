#2014BIT026
#Calculates t-weight and d-weight for m products sold in n countries

m = int(input("Enter number of Products:"))
n = int(input("Enter number of Countries:"))
data = [[None] * m for i in range(n)]

print("Enter data:")
for i in range(n):
	for j in range(m):
		data[i][j] = int(input("Sales of Product " + str(j) + " in Country " + str(i) + ": "))

rows_sum = [0]*n
cols_sum = [0]*m

for i in range(n):
	for j in range(m):
		rows_sum[i] += data[i][j]

for i in range(m):
	for j in range(n):
		cols_sum[i] += data[j][i]

print("Row sum: " + str(rows_sum))
print("Cols sum: " + str(cols_sum))

print("....................................................")
for i in range(m):
	print("For Product " + str(i) + ": ")
	
	for j in range(n):
		print("\tIn Country " + str(j) + ": ")
		print("\t\tt-weight: " + str(data[i][j]/rows_sum[i]))
		print("\t\td-weight: " + str(data[i][j]/cols_sum[j]))
		print("\n")
print("....................................................")



