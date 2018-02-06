names = ["Jack","Bob","Rob","Marley","Anna","Oli","Mammata","Rehan","Gustavo","Sujan"]

def create_dataset():
	import random
	num_entries = 5000000
	f = open("data.txt","w")
	for i in range(num_entries):
		current = random.choice(names)
		f.write(current+"\n")
	f.close()


def read_dataset_list():
	class_counts = []
	for c in names:
		class_counts.append(0)
	with open("data.txt","r") as f:
		for line in f:
			line = line.strip()
			if line != "":
				class_counts[names.index(line)]+=1
	print(class_counts)

def read_dataset_dict():
	class_counts = {}
	for c in names:
		class_counts[c] = 0
	with open("data.txt") as f:
		for line in f:
			line = line.strip()
			if line != "":
				class_counts[line] +=1
	print(class_counts)


import time

t0 = time.time()
read_dataset_list()
t1 = time.time()
print("List took %0.1f seconds\n" %(t1-t0) )

t0 = time.time()
read_dataset_dict()
t1 = time.time()
print("Dict took %0.1f seconds\n" %(t1-t0) )