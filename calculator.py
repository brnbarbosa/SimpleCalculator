def main() -> None:
    first_number : float = 0.0
    second_number : float = 0.0
    result : float = 0.0


    while True:
        try:
            first_number_str = input("Enter the first number of calculation: ")
            if first_number_str.startswith("-"):
                first_number = float(first_number_str[1:]) * -1.0
                print(sum_op(first_number))
            else:
                first_number = float(first_number_str)

            print(first_number)
        except:
            print('Invalid input')


def sum_op(first_number : float, second_number : float = 2.0) -> float:
    return first_number + second_number

def sub_op(first_number : float, second_number : float) -> float:
    return first_number - second_number

def mult_op(first_number : float, second_number : float) -> float:
    return first_number * second_number

if __name__ == "__main__":
    main()