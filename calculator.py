def main() -> None:
    first_number : float = 0.0
    second_number : float = 0.0
    result : float = 0.0


    while True:
        try:
            first_number_str = input("Enter the first number of calculation: ")
            if first_number_str.startswith("-"):
                first_number = float(first_number_str[1:]) * -1.0
            else:
                first_number = float(first_number_str)


            second_number_str = input("Enter the second number of calculation: ")
            if second_number_str.startswith("-"):
                second_number = float(second_number_str[1:]) * -1.0
            else:
                second_number = float(second_number_str)

            print(sum_op(first_number, second_number), sub_op(first_number, second_number), mult_op(first_number, second_number), div_op(first_number, second_number))
        except:
            print('Invalid input')


def sum_op(first_number : float, second_number : float) -> float:
    return first_number + second_number

def sub_op(first_number : float, second_number : float) -> float:
    return first_number - second_number

def mult_op(first_number : float, second_number : float) -> float:
    return first_number * second_number

def div_op(first_number : float, second_number : float) -> float:
    return first_number / second_number

if __name__ == "__main__":
    main()