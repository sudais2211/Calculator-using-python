class ScientificCalculator:
    def __init__(self):#taking a constructor  which call once when program execute
        self.menu()#this is the static variable 

    def menu(self):
        print("\nSelect operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Remainder")
        print("6. Exponentiation")
        print("7. Sine (in degrees)")
        print("8. Cosine (in degrees)")
        print("9. Tangent (in degrees)")
        print("10. Square Root")
        print("11. Exit")
        self.choose_operation()

    def choose_operation(self):
        try:
            choice = int(input("Enter choice(1-11): "))#variable name choice
            if choice in [1, 2, 3, 4, 5]:#if choice in range [range in from 1 to 5]
                num1 = float(input("Enter first number: "))#taking a number from user
                num2 = float(input("Enter second number: "))#taking a nother number from user
                self.perform_operation(choice, num1, num2)
            elif choice in [6, 7, 8, 9, 10]:
                num = float(input("Enter the number: "))
                if choice == 6:
                    exponent = float(input("Enter the exponent: "))
                    self.perform_operation(choice, num, exponent)
                else:
                    self.perform_operation(choice, num)
            elif choice == 11:
                print("Exiting the calculator.")
                exit()
            else:
                print("Invalid input! Please select a valid option.")
                self.menu()
        except ValueError:
            print("Invalid input! Please enter a valid number.")
            self.menu()

    def perform_operation(self, choice, *args):#arg to take a different input and handle it easily
        if choice == 1:
            print(f"Result: {args[0]} + {args[1]} = {args[0] + args[1]}")#we write it is as {num1}+{num2} = {num1 - num2}
        elif choice == 2:
            print(f"Result: {args[0]} - {args[1]} = {args[0] - args[1]}")
        elif choice == 3:
            print(f"Result: {args[0]} * {args[1]} = {args[0] * args[1]}")
        elif choice == 4:
            if args[1] == 0:
                print("Error: Division by zero!")
            else:
                print(f"Result: {args[0]} / {args[1]} = {args[0] / args[1]}")
        elif choice == 5:
            print(f"Result: {args[0]} % {args[1]} = {args[0] % args[1]}")
        elif choice == 6:
            print(f"Result: {args[0]} ^ {args[1]} = {args[0] ** args[1]}")
        elif choice == 7:
            print(f"Result: sin({args[0]}) = {self.sine(args[0])}")
        elif choice == 8:
            print(f"Result: cos({args[0]}) = {self.cosine(args[0])}")
        elif choice == 9:
            print(f"Result: tan({args[0]}) = {self.tangent(args[0])}")
        elif choice == 10:
            if args[0] < 0:
                print("Error: Cannot take square root of a negative number!")
            else:
                print(f"Result: sqrt({args[0]}) = {args[0] ** 0.5}")
        else:
            print("Invalid operation!")
        
        # Offer to continue or terminate after the operation
        self.after_operation_menu()

    def after_operation_menu(self):
        print("\nWhat would you like to do next?")
        print("1. Perform another operation")
        print("2. Exit")
        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                self.menu()  # Show the main menu again
            elif choice == 2:
                print("Exiting the calculator.")
                exit()
            else:
                print("Invalid input! Please select a valid option.")
                self.after_operation_menu()
        except ValueError:
            print("Invalid input! Please enter a valid number.")
            self.after_operation_menu()

    # Trigonometric functions using degrees
    def sine(self, x):
        radians = x * (3.14159 / 180)  # Convert degrees to radians
        return self.approx_sin(radians)

    def cosine(self, x):
        radians = x * (3.14159 / 180)  # Convert degrees to radians
        return self.approx_cos(radians)

    def tangent(self, x):
        radians = x * (3.14159 / 180)  # Convert degrees to radians
        return self.approx_sin(radians) / self.approx_cos(radians)

    # Approximation of sine using Taylor series
    def approx_sin(self, x):
        # Using the first 5 terms of the Taylor series expansion for sine
        return x - (x**3 / 6) + (x**5 / 120) - (x**7 / 5040)

    # Approximation of cosine using Taylor series
    def approx_cos(self, x):
        # Using the first 5 terms of the Taylor series expansion for cosine
        return 1 - (x**2 / 2) + (x**4 / 24) - (x**6 / 720)


# Create an instance of the calculator
calculator = ScientificCalculator()
