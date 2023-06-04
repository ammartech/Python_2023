import sympy as sp
import statistics
import matplotlib.pyplot as plt
import numpy as np

# Dictionary of math operations
math_operations = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
    '/': lambda x, y: x / y,
    'and': lambda x, y: x and y,
    'or': lambda x, y: x or y,
    'not': lambda x: not x,
    'factorial': lambda x: sp.factorial(x),
    'sin': lambda x: sp.sin(x),
    'cos': lambda x: sp.cos(x),
    'tan': lambda x: sp.tan(x),
    'log': lambda x, y: sp.log(x, y),
}

def calculate_math_expression(expression):
    try:
        if 'diff' in expression:
            # Differentiation
            expr = sp.sympify(expression[expression.find("(")+1:expression.find(")")])
            var = sp.symbols('x')
            result = sp.diff(expr, var)
            return f"The result of differentiation is {result}"
        
        elif 'int' in expression:
            # Integration
            expr = sp.sympify(expression[expression.find("(")+1:expression.find(")")])
            var = sp.symbols('x')
            result = sp.integrate(expr, var)
            return f"The result of integration is {result}"
        
        elif 'mean' in expression:
            # Mean calculation
            numbers = expression.split()[1:]
            numbers = [float(num) for num in numbers]
            result = statistics.mean(numbers)
            return f"The mean of the numbers is {result}"
        
        elif 'median' in expression:
            # Median calculation
            numbers = expression.split()[1:]
            numbers = [float(num) for num in numbers]
            result = statistics.median(numbers)
            return f"The median of the numbers is {result}"
        
        elif 'mode' in expression:
            # Mode calculation
            numbers = expression.split()[1:]
            numbers = [float(num) for num in numbers]
            result = statistics.mode(numbers)
            return f"The mode of the numbers is {result}"
        
        elif 'graph' in expression:
            # Graphing
            expr = sp.sympify(expression[expression.find("(")+1:expression.find(")")])
            var = sp.symbols('x')
            x_vals = np.linspace(-10, 10, 400)
            y_vals = [sp.lambdify(var, expr)(x) for x in x_vals]
            
            plt.plot(x_vals, y_vals)
            plt.xlabel('x')
            plt.ylabel('y')
            plt.title('Graph of the Function')
            plt.show()
            
            return "Graph displayed."
        
        elif 'sin' in expression:
            # Sin function
            angle = float(expression[expression.find("(") + 1:expression.find(")")])
            result = math_operations['sin'](angle)
            return f"The result of sin({angle}) is {result}"
    
        elif 'cos' in expression:
            # Cos function
            angle = float(expression[expression.find("(") + 1:expression.find(")")])
            result = math_operations['cos'](angle)
            return f"The result of cos({angle}) is {result}"
    
        elif 'tan' in expression:
            # Tan function
            angle = float(expression[expression.find("(") + 1:expression.find(")")])
            result = math_operations['tan'](angle)
            return f"The result of tan({angle}) is {result}"
    
        elif 'log' in expression:
            # Log function
            base = float(expression.split()[1])
            number = float(expression.split()[2])
            result = math_operations['log'](number, base)
            return f"The result of log base {base} of {number} is {result}"

        else:
            # Regular math expression calculation
            operand1, operator, operand2 = expression.split()
            operand1 = float(operand1)
            operand2 = float(operand2)
            result = math_operations[operator](operand1, operand2)
            return f"The result of {expression} is {result}"
    
    except (ValueError, KeyError, sp.SympifyError, statistics.StatisticsError, np.linalg.LinAlgError) as e:
        return f"Sorry, I couldn't perform the calculation. Please enter a valid math expression."

# AI Assistant loop
while True:
    # Get user input
    user_input = input("Enter a math expression (e.g., 2 + 3, diff(x^2), int(x^2), mean 1 2 3, median 1 2 3, graph(x^2)): ")

    if user_input.lower() == 'exit':
        break

    # Perform the math calculation
    math_result = calculate_math_expression(user_input)

    # Display the result
    print(math_result)
