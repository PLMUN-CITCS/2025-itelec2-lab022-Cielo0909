def greet_user():
    """Greets the user."""
    print("Hello! Welcome!")

def check_even_odd():
    """Checks if a number is even or odd."""
    try:
        number = int(input("Enter an integer: "))
        result = "Even" if number % 2 == 0 else "Odd"
        print(f"{number} is an {result} number.")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

def display_menu():
    """Displays the menu and returns the user's choice."""
    print("\nMenu:")
    print("1. Greet User")
    print("2. Check Even/Odd")
    print("3. Exit")
    return input("Enter your choice (1-3): ")
def main():
    """Main program flow with a menu system."""
    while True:
        choice = display_menu()

        if choice == '1':
            greet_user()
        elif choice == '2':
            check_even_odd()
        elif choice == '3':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 3.")

if __name__ == "__main__":
    main()