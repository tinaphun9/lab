def add(x, y):
    answer = x + y
    print(x, "+", y, "=", answer)
def subtract(x, y):
    answer = x - y
    print(x, "-", y, "=", answer)
def multiply(x, y):
    answer = x * y
    print(x, "*", y, "=", answer)
def divide(x, y):
    if y == 0:
        print("Cannot divide by zero, try again")
    else:
        answer = x / y
        print(x, "/", y, "=", answer)
def main():

    while True:
        try:
            x = int(input("Give number "))
            y = int(input("what other number?"))
            break
        except:
            print("Please enter numbers only.")

    print("1-add | 2-subtract | 3-multipy | 4-divide")

    choice = input("Enter 1, 2, 3, or 4: ")

    if choice == "1":
        add(x, y)
    else:
        if choice == "2":
            subtract(x, y)
        else:
            if choice == "3":
                multiply(x, y)
            else:
                if choice == "4":
                    divide(x, y)
                else:
                    print("try again")

main()
