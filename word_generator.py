import random


ALPHABET="abcdefghijklmnopqrstuvwxyz"

def import_word_list(filename):
	word_list = []
	with open(filename, 'r') as f:
		for line in f.read().splitlines():
			word_list.append([line.split('\t')[0], int(line.split('\t')[1])])
	#print(word_list[0:5])
	return word_list

def generate_next_letter_frequencies(include_spaces=False):
	next_letter_frequency = {}
	if include_spaces:
		for letter in ALPHABET + " ":
			next_letter_frequency[letter] = [0] * 27
	else:
		for letter in ALPHABET:
			next_letter_frequency[letter] = [0] * 26
	#print(next_letter_frequency)
	return next_letter_frequency

def letter_to_index(letter):
	assert(letter in ALPHABET or letter == ' ')
	if letter == ' ':
		return 26
	return ord(letter) - ord('a')

def populate_next_letter_frequencies(word_list, next_letter_frequency, include_spaces=False):
	for word, freq in word_list:
		if include_spaces:
			word = word + " "
		for index in range(len(word)-1):
			current_letter = word[index]
			next_letter = letter_to_index(word[index+1])
			next_letter_frequency[current_letter][next_letter] += freq

	#Normalize letter distribution
	for letter in ALPHABET:
		next_letter_frequency[letter] = [x/sum(next_letter_frequency[letter]) for x in next_letter_frequency[letter]]

	#print(next_letter_frequency)
	return next_letter_frequency

def generate_word(starting_letter, len_word, next_letter_frequency):
	word = starting_letter
	for i in range(len_word):
		next_letter = random.choices(ALPHABET, weights=next_letter_frequency[word[-1]])[0]
		word += next_letter
	#print(word)
	return word

def generate_words_by_distribution(num_words, next_letter_frequency):
	word_length_distribution = [0.2, 0.2, 0.2, 0.15, 0.1, 0.05, 0.05, 0.05, 0.025]
	words = ""
	for i in range(num_words):
		starting_letter = random.choices(ALPHABET)[0]
		words += generate_word(starting_letter, random.choices(range(9), weights=word_length_distribution)[0], next_letter_frequency) + " "
	print(words)
	return words


def main():
	word_list = import_word_list('word_count.txt')
	next_letter_frequency = generate_next_letter_frequencies()
	populate_next_letter_frequencies(word_list, next_letter_frequency)
	#generate_word('t', 10, next_letter_frequency)
	generate_words_by_distribution(10, next_letter_frequency)

	#print(letter_to_index('a'))
	#print(letter_to_index('z'))


if __name__ == "__main__":
	main()