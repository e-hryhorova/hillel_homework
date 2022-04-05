import random
soglasnye = ('b', 'c', 'd', 'f', 'g', 'h', 'k', 'l', 'm', 'n', 'p', 'r', 's', 't', 'w', 'v', 'x', 'z')
vowels = ('a', 'e', 'o', 'i', 'u')

def change_consonants_letters_to_vowel(s):
    for i in s:
        if i in soglasnye:
            s = s.replace(i, random.choice(vowels))
    return s


print(change_consonants_letters_to_vowel("hellomystring"))
