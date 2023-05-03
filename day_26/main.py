# List Comprehention -> creating new list from previous list
list = [1, 2, 3]

new_list = [item for item in list]
print(new_list)

range_list  = [num * 2 for num in range(1,5)]
print(range_list)

names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']
short_names = [name.upper() for name in names if len(name) <= 6]
print(short_names)

# Exercise -> Squaring Numbers
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
new_numbers = [num**2 for num in numbers]
print(new_numbers)
even_numbers = [num for num in numbers if num % 2 == 0]
print(even_numbers)

# Dictionary Comprehention -> Creating new dict from previous dict
dict = {"a": 1, "b": 2, "c": 3, "d": 4}

new_dict = {key: value for (key, value) in dict.items() if True}
print(new_dict)




# NATO Alphabet Project
import pandas

student_data_frame = pandas.read_csv('nato_phonetic_alphabet.csv')

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
phonetic_dict = {row.letter: row.code for (_, row) in student_data_frame.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word = input("Enter a word: ").upper()

output_list = [phonetic_dict[letter] for letter in word]

print(output_list)
