from tester import request_api_key, process_data

# This is the code to the User Interface for testing the API

def main():

    filename = "example.txt"
    api_key = ""

    print("Welcome to the Tester Program of the FRA_UAS_AI_recognition_Project!")
    username = input("Please choose an username: ")
    try:
        api_key = request_api_key(username)
    except OSError:
        print("Could not connect to API. Once the server is running type 'key' to reload your session key.")
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
            print(" - file: Use example.txt for request")
            print(" - request: Send a request through commandline")
            print(" - key: Reload API key")
            print(" - user: Change username")
            print(" - quit: Quit the program")

        elif user_input == "file":

            try:
                file = open(filename, "r", encoding='utf-8')
                content = file.read()
                process_data(content, api_key)
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
