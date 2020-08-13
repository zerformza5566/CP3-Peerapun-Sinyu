number = int(input("Please enter your number : "))

for x in range(number):
    text = (" " * (number - x))+"*"
    for y in range(x):
        text = text+"**"
    print(text)