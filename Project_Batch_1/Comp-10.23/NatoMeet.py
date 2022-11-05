import pandas as pd

# with open("./CSV Files/nato_phonetic_alphabet.csv") as nato_alphabet:
#     alphabet = nato_alphabet.readlines()

path = r"C:\Users\Owner\Downloads\Portofolio\Project_Batch_1\Comp-10.23\CSV Files\nato_phonetic_alphabet.csv"
df1 = pd.read_csv(path)

phonetic_dict = {row.letter: row.code for (index, row) in df1.iterrows()}
print(phonetic_dict)
def generate_phonetic():
    word = input("Enter a word: ").upper()
    try:
        output_list = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print("Sorry only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(output_list)