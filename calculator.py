def calculator() -> None:
    first_operand : float = get_float_input("Enter the first operand of calculation: ")
    second_operand : float = get_float_input("Enter the second operand of calculation: ")
    operator : str = get_operator("Insert a valid operator (+, -, *, /): ")

    calculation_result = result(first_operand, second_operand, operator)

    if calculation_result != None:
        print("Result: " + str(calculation_result))
    
def get_float_input(prompt : str) -> float:
    while True:
        try:
            operand_str = input(prompt)
            operand = float(operand_str)

            return operand
        except ValueError:
            print('Invalid Input')

def get_operator(prompt : str) -> str:
    while True:
        try:
            operator = input(prompt)
            valid_operators = ['+', '-', '*', '/']
            for item in valid_operators:
                if operator == item:
                    return operator
        except ValueError:
            print("Invalid input.")

def result(first_operand : float, second_operand : float, operator : str) -> float:
    calculation_result = None

    match operator:
        case '+':
            calculation_result = sum_op(first_operand, second_operand)
        case '-':
           calculation_result = sub_op(first_operand, second_operand)
        case '*':
            calculation_result = mult_op(first_operand, second_operand)
        case '/':
            calculation_result = div_op(first_operand, second_operand)
        case _:
            print("Error: Unknown operator")

    return calculation_result

def sum_op(first_operand : float, second_operand : float) -> float:
    return first_operand + second_operand

def sub_op(first_operand : float, second_operand : float) -> float:
    return first_operand - second_operand

def mult_op(first_operand : float, second_operand : float) -> float:
    return first_operand * second_operand

def div_op(first_operand : float, second_operand : float) -> float:
    try:
        result = first_operand / second_operand
        return result
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
        return None

if __name__ == "__main__":
    calculator()