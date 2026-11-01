
import re

rules = [
    (r'.*\b(hi|hello|hey)\b.*', ["Hello! How can I help you today?", "Hi there!"]),
    (r'.*\bhow are you\b.*', ["I'm just a program, but I'm doing well!"]),
    (r'.*\bmy name is (.*)', ["Nice to meet you, {0}!"]),
    (r'.*\b(bye|goodbye)\b.*', ["Goodbye! Have a great day!"]),
    (r'.*\bwhat is your name\b.*', ["I am a simple rule-based chatbot."]),
    (r'.*\bhelp\b.*', ["I can chat about simple things. Try greeting me!"]),
    (r'.*', ["Sorry, I didn't understand that. Can you rephrase?"]),  # default rule
]

def chatbot_response(user_input):
    user_input = user_input.lower().strip()

    for pattern, responses in rules:
        match = re.match(pattern, user_input)

        if match:
            response = responses[0]

            if match.groups():
                response = response.format(*match.groups())

            return response

    return "I don't understand."


print("Chatbot: Hello! Type 'bye' to exit.")

while True:
    user_input = input("You: ")

    if re.match(r'.*\b(bye|goodbye)\b.*', user_input.lower()):
        print("Chatbot:", chatbot_response(user_input))
        break

    print("Chatbot:", chatbot_response(user_input))
