import re

patterns_responses = {
    r'\b(hi|hello|hey|hola|greetings)\b': [
        "Hello! How can I help you today?",
        "Hey there! Nice to meet you!",
        "Hi! What can I do for you?"
    ],
    r'\b(how are you|how r you|how do you do)\b': [
        "I'm doing great, thank you for asking!",
        "I'm fine! How about you?",
        "All good here! What about you?"
    ],
    r'\b(what is your name|who are you|your name)\b': [
        "I'm a simple chatbot created to assist you!",
        "You can call me ChatBot!",
        "I'm your friendly assistant bot!"
    ],
    r'\b(bye|goodbye|see you|exit|quit)\b': [
        "Goodbye! Have a great day!",
        "See you later! Take care!",
        "Bye! Come back soon!"
    ],
    r'\b(thank you|thanks|thanx)\b': [
        "You're welcome!",
        "Happy to help!",
        "Anytime! Feel free to ask more."
    ],
    r'\b(help|assist|support)\b': [
        "I'm here to help! Just ask me anything.",
        "Sure! What do you need help with?",
        "How can I assist you today?"
    ]
}

fallback_responses = [
    "I'm not sure I understand. Could you rephrase that?",
    "Interesting! Tell me more about that.",
    "I don't have an answer for that, but I'm learning!"
]

def get_patterns():
    return patterns_responses

def get_fallback():
    return fallback_responses
