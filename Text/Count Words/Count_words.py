"""
This program counts the number of words in a string. Also display the result for each word and the total.
"""
import string


def count_words(str_func):
    my_dic = {}
    # creating the dictionary:
    for letter in string.ascii_lowercase:
        my_dic[letter] = 0

    # Counting the words:
    for s in str_func:
        for letter in string.ascii_lowercase:
            if s.lower() == letter:
                my_dic[letter] += 1
    return my_dic


if __name__ == '__main__':
    str_input = input("Enter a word, phrase or sentence: ")
    words_dic = count_words(str_input)
    print("The number of words:")
    print(words_dic)
    print("The total numbers of words are: {}".format(sum(words_dic.values())))
