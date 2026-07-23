import sys

def main():
    print(sys.argv)
    print(sys.argv[0])
    print(sys.argv[1])
    print(sys.argv[2])

main()

def main():
    print(sys.argv)
    print(len(sys.argv))

main()

def main():
    if len(sys.argv) != 2:
        exit("Usage: " + sys.argv[0] + "value")
    print("Hello" + sys.argv[1])

main()


