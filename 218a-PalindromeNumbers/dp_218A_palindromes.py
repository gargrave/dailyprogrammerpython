def step(orig):
    return orig + int(str(orig)[::-1])


def is_palindrome(num):
    return str(num) == str(num)[::-1]


def calc(num):
    value = num
    steps = 0
    found = False
    while not found:
        value = step(value)
        steps += 1
        if is_palindrome(value):
            found = True
        elif steps >= 10000:
            break
    return found, value, steps


def main():
    # #########################################################################
    # Test the challenge input
    # #########################################################################
    for i in 123, 286, 196196871:
        print('\n')
        print('Testing: {}'.format(i))
        found, value, steps = calc(i)
        if found:
            print('Final value: {}'.format(value))
            print('Steps: {}'.format(steps))

    # #########################################################################
    # Bonus: see which input numbers, through 1000, yield identical palindromes.
    # Bonus 2: See which numbers don't get palindromic in under 10000 steps.
    # Numbers that never converge are called Lychrel numbers.
    # #########################################################################
    print('\nRunning bonus tests. Please be patient...')
    pairs = {}
    for i in range(1000):
        found, value, steps = calc(i)
        if not found:
            print('{} did not converge!'.format(i))
        else:
            if value not in pairs:
                pairs[value] = []
            pairs[value].append(i)

    for k, v in pairs.items():
        if v.__len__() > 1:
            print('\n{} was created by the following inputs:\n{}'.format(k, v))


if __name__ == '__main__':
    main()
