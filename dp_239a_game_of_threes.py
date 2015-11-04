import dp_utils


def increment(num):
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


def run(num):
    """
    Generator to process the number through the "game of threes." Continually
    divides the number's closest multiple of 3 until it reaches 1.
    :param num: The original number to process.
    :return: Yields a string detailing the number and increment at each step.
    """
    while num > 1:
        new_num, offset = increment(num)
        yield '{} => {}'.format(num, offset)
        num = new_num
    print('{}\n'.format(num))


def process(num):
    for i in run(num):
        print(i)


def main():
    dp_utils.print_title('239a', 'The Game of Threes')
    process(1)
    process(2)
    process(100)
    process(31337357)

if __name__ == '__main__':
    main()
