from gemini.client import Client
from websocket.client import create_connection

api_key = "your_api_key"  
client = Client(api_key)

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
