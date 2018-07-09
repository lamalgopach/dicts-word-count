filename = open("test.txt")# put your code here.

poem_dictionary = {}
for line in filename:
	line = line.rstrip()
	line = line.split(" ")

	for word in line:
		poem_dictionary[word] = poem_dictionary.get(word,0) + 1
#print(poem_dictionary)	

for word, number in poem_dictionary.items():
	print("{} {}".format(word, number))