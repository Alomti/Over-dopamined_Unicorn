import sys
no_of_tries = 5
word = "Angelika".lower()
users_tries = []
user_word = []
for _ in word:
    user_word.append("_")

def founding_indexes(word, letter):
    indexes = []
    for index, letter_in_word in enumerate(word):
        if letter_in_word == letter:
            indexes.append(index)
    return indexes

while True:
    print("-----------------------")
    print("Liczba twoich prób:", no_of_tries)
    print("Słowo:", "".join(user_word))
    print("Użyte litery:", ", ".join(users_tries))
    letter = input("Podaj literę: ")
    users_tries.append(letter)
    found_indexes = founding_indexes(word, letter)
    if len(found_indexes) == 0:
        print("Nie ma takiej litery")
        no_of_tries -= 1
        if no_of_tries == 0:
            print("Przegrałeś :(")
            sys.exit(0)
    else:
        for index in found_indexes:
            user_word[index] = letter
        if "".join(user_word) == word:
            print("wygrałeś :)")
            print("Słowo to:", word)
            sys.exit(0)