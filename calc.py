def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y
    
num1 = float(input('Input your first number.'))
opr = str(input('Input your operator.(+,-,*,/)'))
num2 = float(input("input your second number."))

print("The answer is: ")

if opr == "+":
   print(f"{num1} + {num2} = {add(num1, num2)}")
elif opr == "-":
    print(subtract(num1,num2))
elif opr == "*":
    print(multiply(num1,num2))
elif opr == "/":
    print(divide(num1,num2))
else:
    print("Incorrect input.")