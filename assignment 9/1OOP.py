class Kasr:
    def __init__(self, s, m):
        self.sorat = s  # Numerator
        self.makhraj = m  # Denominator

    def sum(self, mehman):
        Result = Kasr(None, None)  # Create a new instance to hold the result
        Result.sorat = (self.sorat * mehman.makhraj) + (self.makhraj * mehman.sorat)
        Result.makhraj = self.makhraj * mehman.makhraj
        return Result

    def show(self):
        print(self.sorat, '/', self.makhraj)

    def mul(self, mehman):
        res = Kasr(None, None)  # Create a new instance to hold the result
        res.sorat = self.sorat * mehman.sorat
        res.makhraj = self.makhraj * mehman.makhraj
        return res

    def div(self, mehman):
        reS = Kasr(None, None)  # Create a new instance to hold the result
        reS.sorat = self.sorat * mehman.makhraj
        reS.makhraj = self.makhraj * mehman.sorat
        return reS

    def sub(self, mehman):
        Res = Kasr(None, None)  # Create a new instance to hold the result
        Res.sorat = self.sorat * mehman.makhraj - self.makhraj * mehman.sorat
        Res.makhraj = self.makhraj * mehman.makhraj
        return Res


# Main program loop
while True:
    print("1. Add two fractions")
    print("2. Multiply two fractions")
    print("3. Subtract two fractions")
    print("4. Divide two fractions")
    print("5. Quit")

    # Get user's choice
    choice = int(input("Enter your choice: "))

    if choice == 5:
        break

    # Get inputs for fractions
    num1 = int(input("Enter the numerator of the first fraction: "))
    den1 = int(input("Enter the denominator of the first fraction: "))
    num2 = int(input("Enter the numerator of the second fraction: "))
    den2 = int(input("Enter the denominator of the second fraction: "))

    # Create instances of the Kasr class using user inputs
    a = Kasr(num1, den1)
    b = Kasr(num2, den2)

    # Perform the chosen operation and display the result
    if choice == 1:
        result = a.sum(b)
        result.show()
    elif choice == 2:
        result = a.mul(b)
        result.show()
    elif choice == 3:
        result = a.sub(b)
        result.show()
    elif choice == 4:
        result = a.div(b)
        result.show()
    else:
        print("Invalid choice. Please try again.")
