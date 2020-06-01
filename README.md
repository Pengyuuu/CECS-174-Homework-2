# CECS-174-Homework-2
A program to identify palindromes and crossword squares

print_menu(): prints a menu with three options: "Check a palindrome", "Check a crossword square", and "Quit"

get_menu_choice(): read the user's selected menu option, validate it, and return it

get_phrase(): ask the user to input an English phrase as a string; validate that at least one character is entered; return the validated phrase

is_palindrome(phrase): given a string named phrase, this function returns true if the string is a palindrome, and false otherwise

menu_check_palindrome(): implements Menu Option 1, "check a phrase to see if it is a palindrome"

get_crossword_square(): asks the user to input the words of a word square, one per line

check_crossword_square(square): given a concatenated string representing a potential crossword square, this function determines if the string actually is a crossword square

menu_check_crossword_square(): implements Menu Option 2, "check a crossword square"

main(): implements the "main" of this program
