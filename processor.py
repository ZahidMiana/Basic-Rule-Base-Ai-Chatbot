import re
import random
from rules import get_patterns, get_fallback

def preprocess_input(user_input):
    processed = user_input.lower().strip()
    processed = re.sub(r'\s+', ' ', processed)
    return processed

def process_input(user_input):
    processed = preprocess_input(user_input)
    patterns = get_patterns()
    
    for pattern, responses in patterns.items():
        if re.search(pattern, processed):
            return random.choice(responses)
    
    return random.choice(get_fallback())
