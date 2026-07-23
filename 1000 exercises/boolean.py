x = 3

if x == 3:
    print("It is 3")
else: 
    print(" It is not 3")


x = 2

v = x == 2
print(v)

if v:
    print(v, "Is true- who would thought?")

v = x == 3
print(v)

if v:
    print(v)
else:
    print(v, "is false - who would thought")


x = 32
if x:
    print(" x is true")

y = 9
if y:
    print(" y is true")
else:
    print(" y is false")


values = [None, 0, "", False, [], {}, "0", True]

for v in values:
    if v:
        print("True value: ", v)
    else:
        print("False value: ", v)

