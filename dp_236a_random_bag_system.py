import random
import dp_utils

TARGET_SIZE = 50
BAG = 'OISZLJT'


def main():
    dp_utils.print_title('236a', 'Random Bag System')
    out_str = ''
    while len(out_str) < TARGET_SIZE:
        size = min(TARGET_SIZE - len(out_str), len(BAG))
        out_str += ''.join(random.sample(BAG, size))
    print(out_str)

if __name__ == '__main__':
    main()
