import sys


def main():
    meal = sys.argv[1]
    while True:
        try:
            meal = int(meal)
            break
            meal = raw_input("Please enter a number as an input parameter for the meal")
        except ValueError:
            meal=raw_input("Please enter a number as an input parameter for the meal")
            


if __name__ == '__main__':
    main()