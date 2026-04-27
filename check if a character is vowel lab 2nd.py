# Program to check if a character is a vowel

char = input("Enter a character: ")

# Convert to lowercase to handle both cases
char = char.lower()

if char in ('a', 'e', 'i', 'o', 'u'):
    print("It is a vowel")
else:
    print("It is not a vowel")
