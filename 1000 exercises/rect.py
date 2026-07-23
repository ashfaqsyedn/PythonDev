print("enter the value of side a")
a = int(input(a))
print("enter the value of side b")
b = int(input(b))
def main():
    if len(sys.argv) != 3:
        exit("Needs 2 arguments: width length")

    width = int(sys.argv[1])
    length = int(sys.argv[2])

    if length <= 0:
        exit("length is not positive")
    if width <= 0:
        exit("width is not positive")

    area = a * b
    print("the area is: ", area)

main()


