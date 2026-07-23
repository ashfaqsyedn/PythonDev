import random
hidden = random.randrange(1, 21)

print("The hidden value is", hidden)

user_input = input("Enter your guess")

print(user_input)

guess = int(user_input)

if guess == hidden:
    print("Success")
elif guess < hidden:
    print("guess is low")
else:
    print("guess is too high")


