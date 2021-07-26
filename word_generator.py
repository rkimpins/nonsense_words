ALPHABET="abcdefghijklmnopqrstuvwxyz"

def import_word_list(filename):
	word_list = []
	with open(filename, 'r') as f:
		for line in f.read().splitlines():
			word_list.append([line.split('\t')[0], int(line.split('\t')[1])])
	#print(word_list[0:5])
	return word_list

def generate_next_letter_frequencies():
	next_letter_frequency = {}
	for letter in ALPHABET:
		next_letter_frequency[letter] = [0] * 26
	print(next_letter_frequency)
	return next_letter_frequency

def letter_to_index(letter):
	return ord(letter) - ord('a')

def populate_next_letter_frequencies(word_list, next_letter_frequency):
	for word, freq in word_list:
		for index in range(len(word)-1):
			current_letter = word[index]
			next_letter = letter_to_index(word[index+1])
			next_letter_frequency[current_letter][next_letter] += freq

	#Normalize letter distribution
	for letter in ALPHABET:
		next_letter_frequency[letter] = [x/sum(next_letter_frequency[letter]) for x in next_letter_frequency[letter]]

	print(next_letter_frequency)
	return next_letter_frequency


def main():
	word_list = import_word_list('word_count.txt')
	next_letter_frequency = generate_next_letter_frequencies()
	populate_next_letter_frequencies(word_list, next_letter_frequency)

	#print(letter_to_index('a'))
	#print(letter_to_index('z'))


if __name__ == "__main__":
	main()