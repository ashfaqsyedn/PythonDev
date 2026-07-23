


a = int(input('Enter the first number'))
b = int(input('Enter the second number'))
c = input('enter the operator')

def calculate(c):
    if c == '+':
        print(a + b)
    elif c == '-'):
        print(a-b)
    elif c == '*':
        print(a * b)
    elif c == '/':
        print(a/b)
    else:
        print("Type the correct operator")

calculate()

def main():
    a = input("Number" )
    b = input ("Number ")
    op = input("Operator ")
    command = a + op + b
    print(command)
    res = eval(command)
    print(res)

main()


