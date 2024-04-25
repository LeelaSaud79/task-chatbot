import nltk
from transformers import pipeline

# Download NLTK data
nltk.download('punkt')

# Load the pre-trained model
nlp = pipeline("question-answering")

# Example documents (you can replace these with your own documents)
documents = {
    "document1": "The quick brown fox jumps over the lazy dog.",
    "document2": "Python is an interpreted, high-level, general-purpose programming language.",
    # Add more documents as needed
}

# Function to answer user queries from documents
def answer_query(question, context):
    result = nlp(question=question, context=context)
    return result["answer"]

# Function to collect user information
def collect_user_info():
    print("Sure, I can help you with that. Please provide the following information:")
    name = input("What's your name? ")
    phone = input("What's your phone number? ")
    email = input("What's your email address? ")
    return name, phone, email

# Main function to interact with the user
def main():
    print("Welcome! How can I assist you today?")
    while True:
        user_input = input("User: ")
        if "call me" in user_input:
            name, phone, email = collect_user_info()
            print(f"Thank you, {name}! I'll call you at {phone} or email you at {email}.")
        else:
            best_document = None
            best_answer = None
            max_score = 0
            question = user_input
            for doc_name, doc_text in documents.items():
                answer = answer_query(question, doc_text)
                # Calculate score based on answer length
                score = len(answer)
                if score > max_score:
                    max_score = score
                    best_document = doc_name
                    best_answer = answer
            print(f"Bot: From {best_document}, {best_answer}")

if __name__ == "__main__":
    main()
