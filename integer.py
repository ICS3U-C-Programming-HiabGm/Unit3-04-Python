# Created by: Hiab G
# Date: Wed, Feb. 28th
# This program checks if the number is positive, negative, or just zero


def main():
    # get number of students
    integer = int(input("Enter an integer: "))

    # check if number if there are too many students

    if integer > 0:
        print(f"{integer} is a positive number!")

    # check if number if there are correct number of students
    elif integer < 0:
        print(f"{integer} is a negative number!")

    elif integer == 0:
        print(f"{integer} is just zero")


if __name__ == "__main__":
    main()
