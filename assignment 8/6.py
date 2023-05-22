class ComplexNumber:
    def __init__(self, real=0, imag=0):
        self.real, self.imag = real, imag
    def __str__(self):
        return f"{self.real}+{self.imag}i"

def add_complex_numbers(c1, c2):
    return ComplexNumber(c1.real + c2.real, c1.imag + c2.imag)

def multiply_complex_numbers(c1, c2):
    return ComplexNumber(c1.real * c2.real - c1.imag * c2.imag, c1.real * c2.imag + c1.imag * c2.real)

def subtract_complex_numbers(c1, c2):
    return ComplexNumber(c1.real - c2.real, c1.imag - c2.imag)

while True:
    print("\nMenu:\n1. Add\n2. Multiply\n3. Subtract\n4. Exit\n")
    choice = input("Enter your choice: ")
    if choice == '1' or choice == '2' or choice == '3':
        real1, imag1 = map(float, input("Enter the first complex number (real imag): ").split())
        real2, imag2 = map(float, input("Enter the second complex number (real imag): ").split())
        c1, c2 = ComplexNumber(real1, imag1), ComplexNumber(real2, imag2)
    if choice == '1':
        print(f"\nThe sum of {c1} and {c2} is {add_complex_numbers(c1, c2)}.")
    elif choice == '2':
        print(f"\nThe product of {c1} and {c2} is {multiply_complex_numbers(c1, c2)}.")
    elif choice == '3':
        print(f"\nThe difference between {c1} and {c2} is {subtract_complex_numbers(c1, c2)}.")
    elif choice == '4':
        break
    else:
        print("Invalid choice. Please try again.")