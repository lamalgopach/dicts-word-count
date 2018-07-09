def open_file(filename):

	file = open(filename)# put your code here.

	return file

def create_dict(file):
	poem_dictionary = {}
	
	for line in file:
		line = line.rstrip().split(" ")
		#line = line.split(" ")
		for word in line:
			word = word.lower().rstrip(",.!@#$?;:-")
			poem_dictionary[word] = poem_dictionary.get(word,0) + 1
	
	return poem_dictionary

def print_out_dict(poem_dictionary):
	for word, number in poem_dictionary.items():
		print("{} {}".format(word, number))

#open_file("test.txt")
file1 = open_file("test.txt")
word_dict = create_dict(file1)
print_out_dict(word_dict)

# file1 = open_file("test.txt")
# word_dict = create_dict(file1)
# print_out_dict(word_dict)



#print_out_dict(create_dict(open_file("test.txt")))
#print_out_dict(create_dict(open_file("twain.txt")))