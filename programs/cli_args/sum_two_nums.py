import ast
import sys

try:
    num1, num2 = sys.argv[1:]
    total = ast.literal_eval(num1) + ast.literal_eval(num2)
except ValueError:
    sys.exit('Error: Please provide exactly two numbers as arguments')
else:
    print(f'{num1} + {num2} = {total}')

