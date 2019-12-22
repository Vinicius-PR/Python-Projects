"""
Checks if the string entered by the user is a palindrome.
That is that it reads the same forwards as backwards like “racecar”
"""
if __name__ == '__main__':
    print("Lets see if what you enter is a palindrome. Don't need to worry about uppercase or lowercase.")
    string_input = input("Enter a word, phrase or a sentence: ")
    if string_input.lower() == string_input[::-1].lower():
        print("This is a palindrome! ")
    else:
        print("This is NOT a palindrome :(")
