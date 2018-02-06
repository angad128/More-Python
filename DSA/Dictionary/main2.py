
def main():
	names = ["Jack","Bob","Rob","Marley","Anna","Oli","Mammata","Rehan","Gustavo","Sujan"]
	import random
	num_entries = 5000000
	f = open("data.txt","w")
	for i in range(num_entries):
		current = random.choice(names)
		f.write(current+"\n")
	f.close()

if __name__ == "__main__":
	main()