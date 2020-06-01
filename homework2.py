import EnglishDictionary

def print_menu():
    #present option
    print('1. Check a palindrome \n2. Check a crossword square' \
          '\n3. Quit \nChoose a function:')

def get_menu_choice():
    #get menu choice and validate it
    menu_option = int(input())
    while menu_option < 1 or menu_option > 3:
        menu_option = int(input())

    return menu_option

def get_phrase():
    #get user's phrase and check if it's an actual word
    phrase = input('Please enter a phrase: ')

    while len(phrase) < 1:
        phrase = input('Please enter a phrase: ')

    return phrase

def is_palindrome(phrase):
    #check if it's a palindrome
    phrase = phrase.lower()
    i = 0
    j = len(phrase) - 1
    d = phrase
    while i < j:
        #if there's any spaces, if statements will skip it and check the next letter
        c = phrase[i].isalpha()
        d = phrase[j].isalpha()
        if c == False:
            i += 1

        elif d == False:
            j -= 1

        #check letters if they are equal to each other
        elif phrase[i] == phrase[j]:
            i += 1
            j-= 1

        else:
            return False

    return True

def menu_check_palindrome():
    #get phrase, check if it's a palindrome, print result
    phrase = get_phrase()
    phrase_result = is_palindrome(phrase)
    if phrase_result == True:
        print(phrase + ' is a palindrome!')
    else:
        print(phrase + ' is not a palindrome')

def get_crossword_square():
    #get words for crossword square and concatenate into one string
    first_line = input('Please enter the first word of the square: ')

    for i in range(len(first_line) - 1):
        next_line = input('Please enter the next word of the square: ')
        first_line += next_line

    return first_line

def check_crossword_square(square):
    start = 0
    end = 0
    string_length = int((len(square)) ** (1/2))

    #print out the crossword square
    for i in range(string_length):
        end += string_length
        first_line = square[start:end]
        print(first_line)
        start += string_length

    start = 0
    end = 0

    #see if words horizontally and vertically are actual words
    for i in range(string_length):
        end += string_length
        first_line = square[start:end]
        first_line = EnglishDictionary.is_word(first_line)
        if first_line == False:
            return False
        start += string_length

    start = 0
    end = 0
    for i in range(string_length):
        end += string_length
        first_line = square[start:len(square):string_length]
        first_line = EnglishDictionary.is_word(first_line)
        if first_line == False:
            return False
        start += 1

    return True

def menu_check_crossword_square():
    #get crossword square and check if it's a crossword square or not
    square = get_crossword_square()
    result = check_crossword_square(square)
    if result == True:
        print('is a crossword square!')
    else:
        print('is not a crossword square')

def main():
    #present the menu and choose whatever option user picks
    menu_option = 0
    while menu_option != 3:
        print_menu()
        menu_option = get_menu_choice()

        if menu_option == 1:
            menu_check_palindrome()

        if menu_option == 2:
            menu_check_crossword_square()
    print('Goodbye!')
main()
