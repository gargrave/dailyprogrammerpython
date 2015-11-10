import itertools
import dp_utils


def print_results(results):
    print('Found {} vampire numbers!\n'.format(len(results)))
    results.sort()
    for r in results:
        print(r)


def process(digits, num_fangs):
    print('Working...')
    results = []
    # use itertools to create all possible combinations of these digits
    for i in itertools.combinations_with_replacement(range(10, 100), num_fangs):
        prod = 1
        digit_str = ''
        # multiply each value together, and build a string out of them
        for x in i:
            prod *= x
            digit_str += '*' if len(digit_str) > 0 else ''
            digit_str += str(x)

        # sort the string of digits and compare them
        # if they match, we have a vampire number!
        if sorted(str(prod)) == sorted(digit_str.replace('*', '')):
            results.append('{}={}'.format(prod, digit_str))

    print_results(results)


def main():
    dp_utils.print_title('234a', 'Vampire Numbers')
    process(6, 3)

if __name__ == '__main__':
    main()
