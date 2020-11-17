import argparse


def add(*args):
    print(args)
    result = 0
    for x in args:
        result += x
    return result


def multiply(*args):
    result = args[0]
    for x in args[1:]:
        result *= x
    return result


def main(opr, numbers):
    if opr == 'add':
        print(add(*numbers))
    elif opr == 'multiply':
        print(multiply(*numbers))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('operation', help="add or multiply")
    parser.add_argument('numbers', type=int, nargs='+', help="numbers to operate on")
    args = parser.parse_args()
    main(args.operation, args.numbers)
