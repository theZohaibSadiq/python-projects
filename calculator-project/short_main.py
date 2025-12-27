while True:
    op = input("Enter an Operations +, -, /, * and q for exit: ")

    if (op == "q"):
        break

    if (op not in "+-/*"):
        print("Invalid Operation...!")
        continue

    a = int(input("Enter Value: "))
    b = int(input("Enter Value: "))

    operations = {
        "+" : a + b,
        "-" : a - b,
        "*" : a * b,
        "/" : "Cannot divide by zero" if b == 0 else a / b,
    }

    print(f"Result: {operations[op]}")