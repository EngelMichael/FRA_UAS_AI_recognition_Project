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
            print(" - help: Show commands")
            print(" - read: Input a textfile")
            print(" - exit: Quit the program")

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
