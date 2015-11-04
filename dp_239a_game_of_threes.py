import dp_utils


def step(num):
    """
    Finds the closest multiple of 3 to the given number and
    returns that number divded by 3.
    :param num: The number to test.
    :return: The original number moved to its closest multiple of 3,
        then divided by 3.
    """
    offset = 0
    if (num + 1) % 3 == 0:
        offset = 1
    elif (num - 1) % 3 == 0:
        offset = -1
    return int((num + offset) / 3), offset


def process(num):
    """
    Continuously divides the provided number by three until it reaches one.
    :param num: The number to divide down.
    :return: A string containing the full list of operations for this number.
    """
    out = ''
    while num > 1:
        new_num, offset = step(num)
        out += '{} => {}\n'.format(num, offset)
        num = new_num
    out += '{}\n'.format(num)
    return out


def main():
    dp_utils.print_title('239a', 'The Game of Threes')
    print(process(1))
    print(process(2))
    print(process(100))
    print(process(31337357))

if __name__ == '__main__':
    main()
