import random
import re

import dp_utils


def main():
    dp_utils.print_title('240a', 'Typoglycemia')

    with open('dp_240a_typoglycemia_input.txt', 'r') as file:
        text = file.read()
    words = text.split()

    scrambled = []
    for word in words:
        # check for ending puncuation, and update the end-offset if found
        end_punc = re.search(r'[,.;]$', word)
        end_len = -2 if end_punc else -1
        # the length of the randomizeable letters
        rand_len = len(word) + end_len - 1
        # the length of the actual word, ignoring ending puncation
        adj_len = len(word) + end_len + 1

        # words of three or less have no letter to scramble
        # for longer words, loop to make sure we don't get the original word back
        new_word = word
        if adj_len > 3:
            while new_word == word:
                # 4-letter words -> reverse 2nd and 3rd chars
                if adj_len == 4:
                    new_word = '{}{}{}{}'.format(word[0], word[2], word[1], word[3])
                # 4+-letter words -> scramble them up!
                else:
                    new_word = '{}{}{}'.format(
                        word[0],
                        ''.join(random.sample(word[1:end_len], rand_len)),
                        word[end_len:]
                    )
        scrambled.append(new_word)

    print('Original:\n{}'.format(text))
    print('Scrambled:\n{}'.format(' '.join(scrambled)))

if __name__ == '__main__':
    main()
