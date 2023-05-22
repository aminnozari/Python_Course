def add_fractions(num1, den1, num2, den2):
    numerator = num1 * den2 + num2 * den1
    denominator = den1 * den2
    return simplify_fraction(numerator, denominator)

def multiply_fractions(num1, den1, num2, den2):
    numerator = num1 * num2
    denominator = den1 * den2
    return simplify_fraction(numerator, denominator)

def subtract_fractions(num1, den1, num2, den2):
    numerator = num1 * den2 - num2 * den1
    denominator = den1 * den2
    return simplify_fraction(numerator, denominator)

def divide_fractions(num1, den1, num2, den2):
    numerator = num1 * den2
    denominator = den1 * num2
    return simplify_fraction(numerator, denominator)

def simplify_fraction(num, den):
    gcd_val = gcd(num, den)
    return (num // gcd_val, den // gcd_val)

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

while True:
    print("1. Add two fractions")
    print("2. Multiply two fractions")
    print("3. Subtract two fractions")
    print("4. Divide two fractions")
    print("5. Quit")
    choice = int(input("Enter your choice: "))
    if choice == 5:
        break
    num1 = int(input("Enter the numerator of the first fraction: "))
    den1 = int(input("Enter the denominator of the first fraction: "))
    num2 = int(input("Enter the numerator of the second fraction: "))
    den2 = int(input("Enter the denominator of the second fraction: "))

    if choice == 1:
        result = add_fractions(num1, den1, num2, den2)
        print(f"The result is: {result[0]}/{result[1]}")
    elif choice == 2:
        result = multiply_fractions(num1, den1, num2, den2)
        print(f"The result is: {result[0]}/{result[1]}")
    elif choice == 3:
        result = subtract_fractions(num1, den1, num2, den2)
        print(f"The result is: {result[0]}/{result[1]}")
    elif choice == 4:
        result = divide_fractions(num1, den1, num2, den2)
        print(f"The result is: {result[0]}/{result[1]}")
    else:
        print("Invalid choice. Please try again.")