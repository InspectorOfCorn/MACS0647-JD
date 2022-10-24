import pandas as pd

# with open("./CSV Files/nato_phonetic_alphabet.csv") as nato_alphabet:
#     alphabet = nato_alphabet.readlines()
    
df1 = pd.read_csv("./CSV Files/nato_phonetic_alphabet.csv")

nato_alphabet = {}
for (index,row) in df1.iterrows():
    nato_alphabet[row.letter] = row.code

user_input = str(input("Enter a word: "))
user_input = user_input.upper()
new_list = [char for char in user_input]
#Loop through list and see if char is in dict.

result = {char:nato_alphabet[char] for char in new_list if char in nato_alphabet}

print(result)