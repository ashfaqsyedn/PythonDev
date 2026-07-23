import sys

print(sys.executable)
print(sys.platform)
print(sys.argv[0])
print(sys.version_info.major)
print(sys.getsizeof(1))
print(sys.getsizeof(42))
print(sys.getsizeof(1.0))

print(sys.getsizeof(""))
print(sys.getsizeof("a"))
print(sys.getsizeof("ab"))

def main():
    print("hello")
    print("world")

if __name__=="__main__":
    main()


sys.stdout.write("hello")
sys.stdout.write("world")


from __future__ import print_function
print("hello", end="")
print("world")

def main():
    print("We have a question")
    name = raw_input('Your name: ')
    print('Hello' + name + ', How are you')

main()

def main():
    print("We have a quesion")
    name = input('Your name')
    print('Hello' + name + 'how are you')

main()

def main():
    if sys.version_info.major < 3:
        name = raw_input('Your Name :')
    else:
        name = input('Your Name:')
    print('Hello' + name + 'how are you')

main()

def main():
    a = input('add first number:')
    b = input('add second number:')
    print(a + b)

main()

def main():
    a = input("fist number")
    b = input("second number")
    print(int(a) + int(b))

main()

val = input("Type the number")
print(val)
print(val.isdecimal())
print(val.isnumeric())

if val.isdecimal():
    num = int(val)
    print(num)

a = "23"
print(a)
print(type(a))

b = int(a)
print(b)
print(type(b))

a = "42 for life "
print(a)
print(type(a))

b = int(a)
print(b)
print(type(b)

a = 2.1
print(type(a))
print(a)

b = int(2.1)
print(type(b))
print(b)

a = "2.1"
print(a)
print(type(a))

b = int(a)
print(b)
print(type(b))

a = "2.1"
b = float(a)
c = int(b)
print(c)
print(type(a))
print(type(b))
print(type(c))

d = int(float(a))

print(d)
print(type(d))

print(int(float(2.1)))
print(int(float("2")))
print(int(float(2)))

def main():
    expected_answer = "42"
    inp = input('What is the answer')

    if inp == expected_answer:
        print("Welcome to the cabal")

main()

def main():
    expected_anwer = "52"
    inp = input("what is the number")
    if inp == expected_answer:
        print("Welcome to the cabal")
    else:
        print("Read the hitchhiker guide to the galaxy")

main()

def main():
    a = input('First number: ')
    b = input('second number: ')

    if a == b:
        print('They are equal')
    else:
        if int(a) < int(b):
            print(a + 'is smaller than' + b)
        else:
            print(a + 'is greated than' + b)

main()

def main():
    a = input("first number")
    b = input("second number")

    if a == b:
        print("They are equal")
    elif(int(a) < int(b)):
        print(a + 'is smaller than' + b)
    else:
        print(a + 'is bigger than '+ b)

main()

x = 3
answer = 'positive' if x > 0 else 'negative'
print(answer)


