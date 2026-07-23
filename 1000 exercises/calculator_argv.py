import sys

def main():
    if len(sys.argv) < 4:
        exit("Usage " + sys.argv[0] + "Operand operator Operand")
    a = float(sys.argv[1])
    b = float(sys.argv[3])
    op = sys.argv[2])

    if op == '+':
        res = a + b
    elif op == '-':
        res = a-b
    elif op == '*':
        res = a * b
    elif op == '/':
        res = a / b
    else:
        print(" invalid Operator:  '{}/".format(op))
        exit()

    print(res)

main()



