def open_file(file):

	filename = open(file)# put your code here.

	return filename

def create_dict(filename):
	poem_dictionary = {}
	
	for line in filename:
		line = line.rstrip()
		line = line.split(" ")
		for word in line:
			poem_dictionary[word] = poem_dictionary.get(word,0) + 1
	
	return poem_dictionary

def print_out_dict(poem_dictionary):
	for word, number in poem_dictionary.items():
		print("{} {}".format(word, number))

#open_file("test.txt")
print_out_dict(create_dict(open_file("test.txt")))
print_out_dict(create_dict(open_file("twain.txt")))