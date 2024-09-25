import pandas


nato_phonetic_alphabet = pandas.read_csv("nato_phonetic_alphabet.csv")
# new_dict = {}
# for (index, row) in nato_phonetic_alphabet.iterrows():
#     new_dict[row.letter] = row.code

# Another form:
phonetic_dict = {row.letter: row.code for (index, row) in nato_phonetic_alphabet.iterrows()}
print(phonetic_dict)


def generate_phonetic():
    user_word = [letter for letter in input("type anything").upper()]
    try:
        user_list = [phonetic_dict[letter] for letter in user_word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(user_list)


generate_phonetic()
