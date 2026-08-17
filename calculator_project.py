OPERATOR = input("Enter an operator (+, -, *, /): ")
num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")
 
try: 

    num1 = float(num1)
           
    num2 = float(num2)
         
    if OPERATOR == '+':
        result = num1 + num2
        print(f"The result of {num1} + {num2} is: {result}")
    elif OPERATOR == '-':
        result = num1 - num2
        print(f"The result of {num1} - {num2} is: {result}")
    elif OPERATOR == '*':
        result = num1 * num2
        print(f"The result of {num1} * {num2} is: {result}")
    elif OPERATOR == '/':
        if num2 != 0:
            result = num1 / num2
            print(f"The result of {num1} / {num2} is: {result}")
        else:
            print("Error: Division by zero is not allowed.")
    else:
        print("Error: Invalid operator. Please use +, -, *, or /.")

    #print("Error: Please enter valid numbers.")  

except ValueError:
    print("Error: Invalid input. Please enter numeric values for the numbers.")    

    def calculator():
        OPERATOR = input("Enter an operator (+, -, *, /): ")
        num1 = input("Enter the first number: ")
        num2 = input("Enter the second number: ")
        
        try:
            num1 = float(num1)
            num2 = float(num2)
            
            if OPERATOR == '+':
                result = num1 + num2
                print(f"The result of {num1} + {num2} is: {result}")
            elif OPERATOR == '-':
                result = num1 - num2
                print(f"The result of {num1} - {num2} is: {result}")
            elif OPERATOR == '*':
                result = num1 * num2
                print(f"The result of {num1} * {num2} is: {result}")
            elif OPERATOR == '/':
                if num2 != 0:
                    result = num1 / num2
                    print(f"The result of {num1} / {num2} is: {result}")
                else:
                    print("Error: Division by zero is not allowed.")
            else:
                print("Error: Invalid operator. Please use +, -, *, or /.")
        
        except ValueError:
            print("Error: Invalid input. Please enter numeric values for the numbers.") 

           