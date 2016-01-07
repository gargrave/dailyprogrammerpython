import random

import dp_utils


INPUT = './input/dp_247a_input.txt'
all_people = []


class Person:

    def __init__(self, fam_idx, name):
        self.fam_idx = fam_idx
        self.name = name
        self.has_giver = False
        self.giving_to = None

    def can_receive_from(self, other):
        return not self.has_giver \
               and self.fam_idx is not other.fam_idx \
               and self.giving_to is not other

    def __str__(self):
        return self.name


def main():
    dp_utils.print_title('247a', 'Secret Santa')

    # parse the input into people with family indeces
    with open(INPUT) as file:
        for idx, line in enumerate(file):
            people = line.split()
            for name in people:
                all_people.append(Person(idx, name))

    for giver in all_people:
        found = False
        while not found:
            receiver = random.choice(all_people)
            if receiver.can_receive_from(giver):
                giver.giving_to = receiver
                receiver.has_giver = True
                found = True

    for p in all_people:
        print('{} -> {}'.format(p, p.giving_to))

if __name__ == '__main__':
    main()
