soglasnye = ['b', 'c', 'd', 'f', 'g', 'h', 'k', 'l', 'm', 'n', 'p', 'r', 's', 't', 'w', 'v', 'x', 'z']


def change_consonants_letters_to_vowel(s):
    stroka2 = ""
    for i in s:
        if i in soglasnye:
            letter = 'a'
            stroka2 = stroka2 + letter
        else:
            stroka2 = stroka2 + i
    return stroka2


print(change_consonants_letters_to_vowel("hellomysuperpuperstring"))
