
# CodeAlpha Basic Chatbot

# Function to generate chatbot responses
def chatbot_response(user_input):

    user_input = user_input.lower().strip()

    if user_input == "hello":
        return "Hi! How can I help you?"

    elif user_input == "how are you":
        return "I'm fine, thanks! How are you?"

    elif user_input == "bye":
        return "Goodbye! Have a nice day!"

    else:
        return "Sorry, I don't understand that message."


# Main chatbot program
print("================================")
print("       WELCOME TO CHATBOT")
print("================================")
print("Type 'hello', 'how are you' or 'bye' to chat.")

while True:

    user_message = input("\nYou: ")

    response = chatbot_response(user_message)

    print("Bot:", response)

    if user_message.lower().strip() == "bye":
        break

print("\nChat ended. Thank you!")
