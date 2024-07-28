import os
import sqlite3
from groq import Groq
from email.parser import Parser
import re

# Set up the Groq client
client = Groq(api_key="YOUR_GROQ_API_KEY")

# Function to check equipment availability in the database
def check_availability(item_name):
    conn = sqlite3.connect('film_equipment.db')
    cursor = conn.cursor()
    cursor.execute('SELECT name, availability, price FROM equipment WHERE name = ?', (item_name,))
    result = cursor.fetchone()
    conn.close()
    return result

# Function to handle inquiry emails
def handle_inquiry(email_content):
    item_name = extract_item_name_from_email(email_content)
    equipment = check_availability(item_name)
    if equipment:
        name, availability, price = equipment
        if availability:
            return f'The {name} is available for ${price} per day.'
        else:
            return f'The {name} is not available. We suggest checking out similar items.'
    else:
        return 'The requested item is not found in our inventory.'

# Function to handle review emails
def handle_review(email_content):
    if re.search(r'\b(?:good|great|positive|excellent|fantastic|love|happy)\b', email_content, re.IGNORECASE):
        return 'Thank you for your positive review! Please share your experience on social media.'
    else:
        return 'We are sorry for your negative experience. Our customer service will contact you soon with a gift voucher.'

# Function to handle assistance request emails
def handle_assistance(email_content):
    response = client.chat.completions.create(
        model="llama3-70b-8192",
        messages=[{"role": "user", "content": email_content}],
        max_tokens=100,
        temperature=1.2
    )
    solution = response.choices[0].message.content
    return solution if solution else 'No suitable solution found. Escalating to customer service.'

# Function to classify and respond to emails
def classify_and_respond(email_content):
    if re.search(r'\binquire|availability|rent|price|available|stock\b', email_content, re.IGNORECASE):
        return handle_inquiry(email_content)
    elif re.search(r'\breview|feedback|rating|rate|happy|good|bad\b', email_content, re.IGNORECASE):
        return handle_review(email_content)
    elif re.search(r'\bhelp|support|assist|problem|issue\b', email_content, re.IGNORECASE):
        return handle_assistance(email_content)
    else:
        return 'Email forwarded to customer service for further evaluation.'

# Helper function to extract item name from email content (this can be more complex in real scenarios)
def extract_item_name_from_email(email_content):
    # List of known equipment names
    equipment_names = ['Camera', 'Tripod', 'Microphone', 'Lighting Kit']
    for name in equipment_names:
        if re.search(r'\b' + re.escape(name) + r'\b', email_content, re.IGNORECASE):
            return name
    return None

# Main loop to simulate email processing
def main():
    while True:
        user_input = input("Email Content: ")
        response = classify_and_respond(user_input)
        print("Response:", response)

if __name__ == "__main__":
    main()
