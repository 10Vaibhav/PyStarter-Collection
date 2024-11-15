from Art import logo


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def division(a, b):
    return a / b


operations = {"+": add,
              "-": subtract,
              "*": multiply,
              "/": division,
              }


def calculation():
    print(logo)
    num1 = float(input("Enter the first number: "))
    shouldGo = True
    while shouldGo:

        for operator in operations:
            print(operator)
        choice1 = input("pick an operation : ")

        num2 = float(input("what's the next number?: "))

        answer = operations[choice1](num1, num2)
        print(f"{num1} {choice1} {num2} = {answer}")

        user = input(
            f"Type 'y' to continue calculating with {answer}, or type 'e' to exit, or type 'n' to start new "
            f"calculation. : ")
        if user == 'y':
            num1 = answer
        elif user == 'n':
            shouldGo = False
            calculation()
        else:
            shouldGo = False


calculation()
