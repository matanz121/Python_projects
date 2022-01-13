# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }
#
# #Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass
#
# import pandas
# student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    # pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}
import pandas
#TODO 1. Create a dictionary in this format:
nato_file = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row.letter:row.code for (index, row) in nato_file.iterrows()}
# print(nato_dict)
# {"A": "Alfa", "B": "Bravo"}


#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
def generate_phonetic():
    user_name = input("Enter your word: ").upper()
    try:
        user_phonetic_code = [nato_dict[char] for char in user_name]
    except KeyError:
        print("Sorry, only letters in alphabet please.")
        generate_phonetic()
    else:
        print(user_phonetic_code)


generate_phonetic()


