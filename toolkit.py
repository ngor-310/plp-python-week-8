import random


# Tool 1: Simple Calculator
# Performs basic mathematical operations on two numbers entered by the user.
def simple_calculator():
    print("\n--- SIMPLE CALCULATOR ---")
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print("Select operation: +, -, *, /")
        operation = input("Operation: ").strip()

        if operation == "+":
            result = num1 + num2
            print(f"Result: {num1} + {num2} = {result}")
        elif operation == "-":
            result = num1 - num2
            print(f"Result: {num1} - {num2} = {result}")
        elif operation == "*":
            result = num1 * num2
            print(f"Result: {num1} * {num2} = {result}")
        elif operation == "/":
            if num2 == 0:
                print("Error: Cannot divide by zero!")
            else:
                result = num1 / num2
                print(f"Result: {num1} / {num2} = {result}")
        else:
            print(f"Invalid operation '{operation}'. Please choose +, -, *, or /.")
    except ValueError:
        print("Invalid input! Please enter numerical values.")


# Tool 2: To-Do List Manager
# Manages a dynamic list of tasks that changes as the program runs.
def todo_list_manager():
    tasks = []
    print("\n--- TO-DO LIST MANAGER ---")

    while True:
        print("\nTo-Do Menu:")
        print("1. View tasks")
        print("2. Add task")
        print("3. Clear all tasks")
        print("4. Return to main menu")

        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            if not tasks:
                print("Your to-do list is currently empty.")
            else:
                print("\nYour Current Tasks:")
                for index, task in enumerate(tasks, start=1):
                    print(f"{index}. {task}")
        elif choice == "2":
            new_task = input("Enter new task: ").strip()
            if new_task:
                tasks.append(new_task)
                print(f"Task '{new_task}' added successfully!")
            else:
                print("Task cannot be empty.")
        elif choice == "3":
            tasks.clear()
            print("All tasks have been cleared.")
        elif choice == "4":
            print("Returning to main menu...")
            break
        else:
            print("Invalid choice! Please enter a number from 1 to 4.")


# Tool 3: Number Guessing Game
# Uses a loop and conditionals to provide hints until the user guesses the secret number.
def number_guessing_game():
    print("\n--- NUMBER GUESSING GAME ---")
    secret_number = random.randint(1, 20)
    attempts = 0
    max_attempts = 5

    print("I have chosen a secret number between 1 and 20.")
    print(f"You have {max_attempts} attempts to guess it!")

    while attempts < max_attempts:
        try:
            guess = int(input(f"Attempt {attempts + 1}: Enter your guess: "))
            attempts += 1

            if guess < secret_number:
                print(f"Too low! {max_attempts - attempts} attempt(s) remaining.")
            elif guess > secret_number:
                print(f"Too high! {max_attempts - attempts} attempt(s) remaining.")
            else:
                print(
                    f"Congratulations! You guessed the number {secret_number} in {attempts} attempt(s)!"
                )
                return
        except ValueError:
            print("Invalid input! Please enter a valid whole number.")

    print(
        f"Game Over! You ran out of attempts. The secret number was {secret_number}."
    )


# Main Program Loop
def main():
    print("======================================")
    print("      WELCOME TO MULTI-TOOLKIT        ")
    print("======================================")

    while True:
        print("\nMAIN MENU:")
        print("1. Simple Calculator")
        print("2. To-Do List Manager")
        print("3. Number Guessing Game")
        print("4. Quit")

        choice = input("Please choose a tool (1-4): ").strip()

        if choice == "1":
            simple_calculator()
        elif choice == "2":
            todo_list_manager()
        elif choice == "3":
            number_guessing_game()
        elif choice == "4":
            print("\nThank you for using Multi-Toolkit. Goodbye!")
            break
        else:
            print(
                f"\nPolite Notice: '{choice}' is not a valid option. Please choose a number between 1 and 4."
            )


if __name__ == "__main__":
    main()
