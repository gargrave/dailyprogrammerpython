import dp_utils


def get_prime_factors(num):
    factors = set()
    i = 2
    while num >= i:
        if num % i == 0:
            factors.add(i)
            num //= i
        i += 1
    return factors


def test_pair(pair):
    valid = sum(get_prime_factors(pair[0])) == sum(get_prime_factors(pair[1]))
    print('{} {}'.format(pair, 'VALID' if valid else 'NOT VALID'))


def main():
    dp_utils.print_title('235a', 'Ruth-Aaron Pairs')
    pairs = []
    with open('dp_235a_ruthaaron_pairs.txt', 'r') as file:
        # read the first line to get the number of pairs to test
        lines = int(file.readline())
        for _ in range(lines):
            # build a pair from each line in the file
            num_a, num_b = eval(file.readline())
            pairs.append((num_a, num_b))

    for pair in pairs:
        test_pair(pair)

if __name__ == '__main__':
    main()
