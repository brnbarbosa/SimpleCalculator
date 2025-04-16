# Simple Command-Line Calculator

## Description

This project is a basic command-line calculator written in Python. It currently provides the foundational structure for performing arithmetic operations.

## Current Features

*   Prompts the user to enter the first number for a calculation.
*   Handles basic numeric input (including negative numbers).
*   Includes defined functions for:
    *   Addition (`sum_op`)
    *   Subtraction (`sub_op`)
    *   Multiplication (`mult_op`)
    *   Division (`div_op`)
*   Basic error handling for invalid number input.

*(Note: The main execution loop currently only handles the input of the first number and doesn't yet incorporate selecting an operation or inputting a second number to use the defined `sum_op`, `sub_op`, or `mult_op` functions fully.)*

## How to Run

1.  Make sure you have Python 3 installed.
2.  Navigate to the project directory in your terminal:
    ```bash
    cd path/to/your/PythonProjects/Calculator
    ```
3.  Run the script:
    ```bash
    python calculator.py
    ```
4.  Follow the prompt to enter the first number. Press `Ctrl+C` to exit the loop.

## Future Improvements

*   Implement logic to ask the user for the desired operation (e.g., +, -, \*).
*   Prompt the user for the second number.
*   Call the appropriate operation function (`sum_op`, `sub_op`, `mult_op`) based on user input.
*   Display the final result of the calculation.
*   Add division operation (`div_op`) with handling for division by zero.
*   Refine the input loop and exit conditions.
*   Add more robust error handling.