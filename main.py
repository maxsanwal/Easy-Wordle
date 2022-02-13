word = "carry"
number_of_trys = 6


def index_check(word, input_word):
    correct_indexes = []
    for i in range(len(word)):
        if word[i] == input_word[i]:
            correct_indexes.append(i)
    return correct_indexes


def letter_existence(word, input_word):
    existence_index = []
    non_existence_index = []
    for i in range(len(input_word)):
        if input_word[i] in word:
            existence_index.append(i)
        else:
#             print('Non:', i, word[i])
            non_existence_index.append(i)
    return existence_index, non_existence_index


for i in range(number_of_trys):
    non_existing_words = []
    while True:
        input_word = input(f'Try number {i+1}:')
        if len(input_word) == 5:
            break
        else:
            print("Please input 5 letter word")
    correct_indexes = index_check(word, input_word)
    if len(correct_indexes) == len(word):
        print("You are a genius")
        break
#     elif len(correct_indexes) == 0:
#         print("All the letters are wrong")
    else:
        existing_indexes, non_existence_index = letter_existence(word, input_word)
        for i in non_existence_index:
            non_existing_words.append(input_word[i])
        if len(correct_indexes) !=0:
            print(f'Letters {list(word[i] for i in correct_indexes)} at position {[i+1 for i in correct_indexes]} are correct')
        if correct_indexes != existing_indexes:
            exisitence_list = list(set(existing_indexes) - set(correct_indexes))
            print(f'Letters {list(input_word[i] for i in exisitence_list)} are correct but at wrong positions {[i+1 for i in exisitence_list]}')
        if len(non_existing_words) != 0:
            print(f'Letters {set(non_existing_words)} does not exist')