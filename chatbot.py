import nltk
from transformers import pipeline
from gemini.client import Client

from gemini.client import Client

# Initialize the Gemini client
api_key = "AIzaSyBGI2clcp9kl1L-MrGAjAiKNg283suCAWc"  
client = Client(api_key)

# Function to interact with the Gemini API
def get_account_balance():
    balance = client.get_balance()
    return balance

# Main function
def main():
    print("Welcome! How can I assist you today?")
    while True:
        user_input = input("User: ")
        if "account balance" in user_input:
            balance = get_account_balance()
            print(f"Bot: Your account balance is {balance}.")
        else:
            print("Bot: Sorry, I couldn't understand your request.")

if __name__ == "__main__":
    main()
