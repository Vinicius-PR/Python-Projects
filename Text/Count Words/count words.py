"""
This program counts the number of words in a string. Also display the result for each word and the total.
"""
import string as str


def count_words(str_func):
    my_dic = {}
    # creating the dictionary:
    for letter in str_func.split():
        my_dic[letter] = 0

    # Counting the words:
    for word in str_func.split():
        my_dic[word] += 1
    return my_dic


if __name__ == '__main__':
    str_input = input("Enter a word, phrase or sentence: ")
    words_dic = count_words(str_input)
    print("The number of words:")
    print(words_dic)
    print("The total number of words is: {}".format(sum(words_dic.values())))
