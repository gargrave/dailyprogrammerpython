import dp_utils

MAX_ATTEMPTS = 5000000
path_stack = []


def first_path(val):
    """
    Sets the initial path(s) for the number. Since the main processing loop
    runs until the stack is empty, we need to make sure we have at least
    one path in there before we begin. This path will either be [0], or a
    set of paths with opposite numbers (e.g. [[1], [-2]].

    :param val: The value to add for the first path(s). Should either be 0
        or a tuple containing opposite numbers.
    """
    if val == 0:
        path_stack.append([0])
    else:
        path_stack.append([val[0]])
        path_stack.append([val[1]])


def new_path(path, val):
    """
    Adds a new path to the stack for later testing. This path
    consists of the original path + one extra value added to the end
    as specified by 'val'.

    :param path: The original path up to its current points
    :param val: The value to append to the end of the path
    """
    path_stack.append(path + [val])


def get_offset(num):
    """
    Returns the division offset for the supplied number. If the number is
    divisible by three, this will simply be zero. Otherwise, it will be a
    tuple of both values that can be added to it to make it divisible by three.

    :param num: The number to test
    :return: 0 if the number is divisible by 3; otherwise a tuple consiting of
        one positive and one negative number.
    """
    if num % 3 == 0:
        return 0
    else:
        return (1, -2) if (num + 1) % 3 == 0 else (-1, 2)


def show_solution(paths, num):
    """
    Prints the solution(s) for the number. For numbers with no solution, it will
    simply show "Impossible." For other numbers, it will print out all solutions
    found.

    :param paths: The set of paths that resolve the number to zero (do need necessarily
        need to be zero-sum at this point).
    :param num: The original number we were testing for.
    """
    solution_found = False
    for p in paths:
        test_num = num
        if sum(p) == 0:
            solution_found = True
            # print each step, then the final number
            for i in p:
                print('{} {}'.format(test_num, i))
                test_num = (test_num + i) // 3
            print('{}\n'.format(test_num))

            # then print the sum string of all steps
            sum_str = ' + '.join(str(val) for val in p)
            print('[{}] = {}'.format(sum_str, sum(p)))
            print('='*40)
            print()

    if not solution_found:
        print('Impossible')


def process(num):
    """
    Processes the number by dividing it down by its nearest factors of three until it
    reaches one. This method is not concerned with finding the zero-sum paths--just ANY
    path that resolves to 1.

    :param num: The number we are working with
    """
    print('Testing number: {}\n'.format(num))
    # just find a single solution for huge numbers
    find_all_solutions = num < 500000000
    # all paths that have been successfully resolved to 1
    finished_paths = []
    # add the first step of the initial path
    first_path(get_offset(num))
    attempts = 0

    searching = True
    while searching and len(path_stack) > 0:
        test_num = num
        # get the next path and divide through all of its existing steps
        path = path_stack.pop()
        for i in path:
            test_num = (test_num + i) // 3

        while test_num > 1:
            offset = get_offset(test_num)
            # if we get a tuple back for the offset, add a new path with
            # the second value for later checking, and check the first value now
            if offset != 0:
                new_path(path, offset[1])
                offset = offset[0]

            path.append(offset)
            test_num = (test_num + offset) // 3

            # check if we have reached the end of the path
            # if we do, add it to the list of solutions
            # if we are only looking for one solution, go ahead
            # and check if it is zero-sum; if so, end the loop now
            if test_num == 1:
                finished_paths.append(path)
                if not find_all_solutions and sum(path) == 0:
                    searching = False
            # otherwise, check progress towards max attempts
            else:
                attempts += 1
                if attempts > MAX_ATTEMPTS:
                    searching = False
                elif attempts % 100000 == 0:
                    print('{} solutions tested so far...'.format(attempts))

    show_solution(finished_paths, num)


def main():
    dp_utils.print_title('239b', 'A Game of Threes: Zero Sum Edition')
    process(929)
    process(18446744073709551615)
    # process(18446744073709551614)

if __name__ == '__main__':
    main()
