"""
A simple program that return the number of vowels in a sentence, word or anything.
"""
if __name__ == '__main__':
    count = 0
    my_dic_vowels = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
    string_input = input("Enter the phrase, sentence or anything to start: ")
    for i in string_input.lower():
        if i == 'a':
            my_dic_vowels['a'] += 1
        elif i == 'e':
            my_dic_vowels['e'] += 1
        elif i == 'i':
            my_dic_vowels['i'] += 1
        elif i == 'o':
            my_dic_vowels['o'] += 1
        elif i == 'u':
            my_dic_vowels['u'] += 1
    print("The quantity of each vowels are: {}".format(my_dic_vowels))
    print("The total quantity is: {}".format(sum(my_dic_vowels.values())))
