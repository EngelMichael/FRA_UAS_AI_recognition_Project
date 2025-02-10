from tester import request_api_key, process_data

# This is the code to the User Interface for testing the API

def main():

    filename = "example.txt"
    api_key = ""

    print("Welcome to the Text Interface Program!")
    username = input("Please choose an username: ")
    try:
        api_key = request_api_key(username)
    except OSError:
        print("Could not connect to API.")
    print("\nType 'help' to see available commands or 'exit' to quit.")

    while True:
        # Wait for user input
        print(f"\nCurrent user: {username}")
        print(f"Session Key: {str(api_key)}")
        user_input = input("> ").strip().lower()

        # Process the input
        if user_input == "help":
            print("\nAvailable commands:")
            print(" - help: Show commands")
            print(" - read: Input a textfile")
            print(" - request: Send a request")
            print(" - key: Load API key")
            print(" - user: Change username")
            print(" - quit: Quit the program")

        elif user_input == "read":

            try:
                file = open(filename, "r")
                content = file.read()
                print(f"\n{content}")
                file.close()

            except OSError:
                print("Could not open/read file:"), filename

        elif user_input == "request":
            try:
                input_text = input("Please enter a text to be: ")
                process_data(input_text, api_key)

            except OSError:
                print("Could not connect to API.")

        elif user_input == "key":
            try:
                api_key = request_api_key(username)
            except OSError:
                print("Could not connect to API.")

        elif user_input == "user":
            while True:
                username = input("Please choose a new username: ")
                api_key = request_api_key(username)
                if username != "":
                    break

        elif user_input == "quit":
            break

        else:
            print(f"Unknown command: '{user_input}'. Type 'help' to see available commands.")

if __name__ == "__main__":
    main()
