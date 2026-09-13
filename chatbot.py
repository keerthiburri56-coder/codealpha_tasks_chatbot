def chatbot():
    print("Welcome to Chatbot")

    while True:
        user_input = input("You: ").lower()

        if user_input == "hello" or user_input == "hi":
            print("Bot: Hi! Nice to meet you.")

        elif user_input == "how are you":
            print("Bot: I'm doing great!, thank you for asking!")

        elif user_input == "bye" or user_input == "exit":
            print("Bot: Goodbye!")
            break

        else:
            print("Bot: Sorry, I don't understand.")


if __name__ == "__main__":
    chatbot()