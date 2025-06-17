def calculator():
    print("Welcome to the CLI Calculator. Type 'q' to quit.\n")

    while True:
        first = input("Enter first number: ")
        if first.lower() == 'q':
            break
        second = input("Enter second number: ")
        if second.lower() == 'q':
            break
        operator = input("Choose an operation (+, -, *, /): ")

        try:
            a = float(first)
            b = float(second)
        except ValueError:
            print("⚠️ Please enter valid numbers.\n")
            continue

        if operator == '+':
            result = a + b
        elif operator == '-':
            result = a - b
        elif operator == '*':
            result = a * b
        elif operator == '/':
            if b == 0:
                print("⚠️ Can't divide by zero.\n")
                continue
            result = a / b
        else:
            print("⚠️ Invalid operator.\n")
            continue

        print(f"✅ Result: {result}\n")

calculator()
