import pandas

#TODO 1. Create a dictionary in this format:

#{"A": "Alfa", "B": "Bravo"}
df = pandas.read_csv("nato_phonetic_alphabet.csv")
NATO = {row.letter:row.code for (index, row) in df.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word = str(input("Enter word: ")).upper()
user_NATO = [NATO[letter] for letter in word if letter in NATO]

print(user_NATO)

