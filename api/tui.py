def main():
    print("Welcome to the Text Interface Program!")
    print("Type 'help' to see available commands or 'exit' to quit.")
    
    filename = "example.txt"

    while True:
        # Wait for user input
        user_input = input("> ").strip().lower()

        # Process the input
        if user_input == "help":
            print("Available commands:")
            print(" - help: Show this help message")
            print(" - read: Input a textfile")
            print(" - greet: Get a friendly greeting")
            print(" - exit: Quit the program")

        elif user_input == "greet":
            print("Hello! Hope you're having a great day!")

        elif user_input == "read":

            try:
                file = open(filename, "r")
                content = file.read()
                print(content)
                file.close()

            except OSError:
                print("Could not open/read file:"), filename

        elif user_input == "exit":
            print("Goodbye!")
            break

        else:
            print(f"Unknown command: '{user_input}'. Type 'help' to see available commands.")

if __name__ == "__main__":
    main()