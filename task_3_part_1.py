soglasnye = ('b', 'c', 'd', 'f', 'g', 'h', 'k', 'l', 'm', 'n', 'p', 'r', 's', 't', 'w', 'v', 'x', 'z')


def change_consonants_letters_to_vowel(s):
    for i in s:
        if i in soglasnye:
            s = s.replace(i, 'a')
    return s


print(change_consonants_letters_to_vowel("hellomystring"))
