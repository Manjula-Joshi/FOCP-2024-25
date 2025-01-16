import random
import json

def read_json_file():
    try:
        with open("responses.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print("Error: responses.json not found")
        return {}

def memory(log_file, sender, message):
    with open(log_file, "a") as log:
        log.write(f"{sender}: {message}\n")

def random_disconnect(interaction_count, max_interactions, user_name, agent_name):
    if interaction_count == max_interactions:
        disconnect_messages = [
            f"{agent_name}: Oops, {user_name}! It looks like there's a connection problem. Try again later!",
            f"{agent_name}: Uh-oh! My circuits need a break, {user_name}. I'll be back shortly!",
            f"{agent_name}: Looks like we hit a hiccup in the system, {user_name}. Let's reconnect soon!"
        ]
        print(random.choice(disconnect_messages))
        return True
    return False

def find_response(user_input, responses):
    for category, keywords in responses.items():
        for keyword, response in keywords.items():
            if keyword in user_input:
                return response
    return None

def get_random_response():
    random_responses = [
        "Could you please provide more details?",
        "I'm afraid I don't understand what you mean by that.",
        "That's interesting. Do you have anything specific in mind?",
        "Hmm, I'm not sure about that. Can you elaborate more?",
        "Apologies, that's out of my scope. Let me know if there's something else I can assist with.",
        "I'm unable to assist with that at the moment. Can you clarify?",
        "Please feel free to ask about university-related topics.",
        "I'm here to assist you as much as I can. Ask away!",
        "Oops! I didn't quite get that. Ask me about the campus or events!",
        "Our campus has a lot to offer! What aspect are you curious about?",
        "Good question! I'll do my best to help you find the correct information.",
        "I'm here to assist you with your knowledge quest.",
        "That sounds like an exciting topic. Let me know what you're curious about.",
        "I'm here to help. Please ask me anything about the University of Poppleton.",
        "Our campus has a lot to provide. What are you curious about?",
        "I recommend checking our website for more information.",
        "Let me know if you need information about our academic services.",
        "What can I assist you with today?"
    ]
    return random.choice(random_responses)

def start_chatbot():
    responses = read_json_file()

    username = input("May I know your name, please? ")

    log_file = f"{username}_chat_log.txt"  

    agent_names = ["Lia", "Alex", "Jake", "Sally", "Jay"]
    agent_name = random.choice(agent_names)

    print(f"Hey {username}, I am {agent_name}, your virtual assistant here at the University of Poppleton.")

    with open(log_file, "a") as log:
        log.write(f"Virtual chat session with {agent_name} and {username}:\n")

    interaction_count = 0
    max_interactions = random.randint(5, 10)

    while True:
        user_input = input(f"{username}: ").lower()

        memory(log_file, username, user_input)

        if user_input in ['bye', 'quit', 'exit']:
            print(f"{agent_name}: Goodbye, {username}! Have a great day!")
            memory(log_file, agent_name, "Goodbye message sent.")
            break

        interaction_count += 1
        if random_disconnect(interaction_count, max_interactions, username, agent_name):
            memory(log_file, agent_name, "Random disconnection occurred.")
            break

        response = find_response(user_input, responses)
        if response:
            print(f"{agent_name}: {response}")
            memory(log_file, agent_name, response)
        else:
            random_response = get_random_response()
            print(f"{agent_name}: {random_response}")
            memory(log_file, agent_name, random_response)

start_chatbot()
