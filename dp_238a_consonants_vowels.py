import random

import dp_utils


vowels = 'aeuoi'
cons = 'bcdfghjklmnpqrstvwxyz'


def get_vowel():
    return random.choice(vowels)


def get_cons():
    return random.choice(cons)


def convert(in_word):
    new_word = ''
    for char in in_word:
        if char == 'C':
            new_word += get_cons().capitalize()
        elif char == 'V':
            new_word += get_vowel().capitalize()
        elif char == 'c':
            new_word += get_cons()
        elif char == 'v':
            new_word += get_vowel()
        else:
            new_word = 'ERROR: Invalid input in word: "{}"'.format(in_word)
    return new_word


def main():
    dp_utils.print_title('238a', 'Consonants & Vowels')
    print(convert('cvcvcc'))
    print(convert('CcvV'))
    print(convert('cvcvcvcvcvcvcvcvcvcv'))
    print(convert('notjustcsandvs'))

if __name__ == '__main__':
    main()
