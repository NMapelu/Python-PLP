while True:
    try:
        # Get user input
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        operation = input("Enter the operation (+, -, *, /) or 'q' to quit: ")

        # Check for quit command
        if operation.lower() == 'q':
            print("Calculator exiting... Goodbye!")
            break

        # Perform the operation
        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 == 0:
                print("Error: Division by zero is not allowed.")
                continue
            result = num1 / num2
        else:
            print("Invalid operation. Please enter +, -, *, or /. Try again.")
            continue
        
        # Display the result
        print(f"Result: {num1} {operation} {num2} = {result}")
    except ValueError:
        print("Invalid input. Please enter numerical values only.")

    
    