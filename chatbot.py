import re
patterns_and_responses = {
    r"(hi|hello|hey|good morning|good afternoon)": ["Hello! How can I help you today?"],
    r"what is your name?": ["I'm a chatbot!"],
    r"how are you?": ["I'm just a computer program, so I don't have feelings, but thanks for asking! How can I assist you today?"],
    r"what can i call you?": ["I'm just a bot, Call me ChatGPT."],
    r"can i give you a petname?": ["Ofcourse! I'd love a petname. what do you have in mind?"],
    r"I would like to call you Balu.": ["sure, Balu sounds like a cute petname! From now on, you can call me Balu too."],
}
def get_response(user_input):
    for pattern, responses in patterns_and_responses.items():
        if re.search(pattern, user_input, re.IGNORECASE):
            return responses

    return ["I don't understand. Can you rephrase that?"]


print("Hello! I'm your chatbot. You can type 'quit' to exit.")
while True:
    user_input = input("You: ")
    if user_input.lower() == 'quit':
        print("Chatbot: Take care, my lovable friend! See you later!")
        break
    response = get_response(user_input)
    print("Chatbot:", response[0])
