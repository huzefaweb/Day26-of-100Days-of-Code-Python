import pandas


# TODO 1. Create a dictionary in this format:
nato_csv = pandas.read_csv("nato_phonetic_alphabet.csv")
# nato_dict = nato_csv.set_index(nato_csv.columns[0]).to_dict()[nato_csv.columns[1]] # my way
phonetic_dict = {row.letter: row.code for (index, row) in nato_csv.iterrows()}
print(phonetic_dict)

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word = input("Enter a word: ").upper()
output = [phonetic_dict[letter] for letter in word]
print(output)

