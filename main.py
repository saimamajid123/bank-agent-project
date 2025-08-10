# --------------------------
# Bank Agent Chatbot Project
# --------------------------

# ✅ IMPORTS
import os
import sys
import time
from dotenv import load_dotenv

# ✅ Load Environment Variables (like GEMINI API Key)
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# ✅ Optional Gemini Integration (only if you plan to use it later)
try:
    from google.generativeai import configure, GenerativeModel
    configure(api_key=GEMINI_API_KEY)
    model = GenerativeModel('gemini-pro')
except ImportError:
    print("❌ Gemini module not installed. Skipping Gemini setup.")
except Exception as e:
    print(f"❌ Gemini setup failed: {e}")

# 🔹 Main Virtual Assistant
def main():
    print("🟢 Welcome to TrustBank Virtual Assistant 🟢")
    print("How can I assist you today?")

    while True:
        print("\nPlease choose from the options below:")
        print("1. Check Account Balance")
        print("2. Loan Inquiry")
        print("3. Credit Card Support")
        print("4. Exit")

        user_choice = input("Enter your choice (1-4): ")

        # ✅ Input Guardrail
        if not user_choice.isdigit() or int(user_choice) not in range(1, 5):
            print("❌ Invalid input. Please enter a number between 1 and 4.")
            continue

        user_choice = int(user_choice)

        # ✅ Output Logic Handling
        if user_choice == 1:
            handle_account_balance()
        elif user_choice == 2:
            loan_agent()
        elif user_choice == 3:
            credit_card_agent()
        elif user_choice == 4:
            print("🔒 Thank you for using TrustBank Virtual Assistant. Goodbye!")
            break

# 🔹 Function: Handle Account Balance
def handle_account_balance():
    account_number = input("Please enter your 10-digit account number: ")
    if len(account_number) != 10 or not account_number.isdigit():
        print("❌ Invalid account number. Must be exactly 10 digits.")
        return

    print("✅ Fetching your account balance...")
    time.sleep(1)
    print("💰 Your current balance is: ₹35,250.50")

# 🔹 Function: Loan Department Agent
def loan_agent():
    print("\n📞 Connecting you to the Loan Department Agent...")
    print("Welcome to the Loan Department!")
    print("Please choose a service:")
    print("1. Apply for a Loan")
    print("2. Check Loan Status")

    choice = input("Enter your choice (1 or 2): ")

    if choice == '1':
        print("📝 Let's start your loan application process.")
        print("Please visit your nearest branch with valid documents.")
    elif choice == '2':
        ref = input("📋 Please enter your Loan Reference Number: ")
        if not ref.strip():
            print("❌ Invalid input. Reference number can't be empty.")
        else:
            print(f"🔍 Checking status for Loan Ref: {ref}...")
            time.sleep(1)
            print("✅ Your loan is under review. You will be notified soon.")
    else:
        print("❌ Invalid option. Please try again.")

# 🔹 Function: Credit Card Department Agent
def credit_card_agent():
    print("\n📞 Connecting you to the Credit Card Department Agent...")
    print("Welcome to the Credit Card Department!")
    print("Please choose a service:")
    print("1. Apply for a Credit Card")
    print("2. Block Lost/Stolen Card")

    choice = input("Enter your choice (1 or 2): ")

    if choice == '1':
        print("📝 You can apply online at www.trustbank.com/credit-card or visit your nearest branch.")
    elif choice == '2':
        phone = input("⚠️ Please confirm your registered phone number: ")
        if not (phone.isdigit() and len(phone) == 10):
            print("❌ Invalid phone number. Must be 10 digits.")
        else:
            print("✅ Card has been blocked. A new card will be issued shortly.")
    else:
        print("❌ Invalid option. Please try again.")

# 🔚 Run the Chatbot
if __name__ == "__main__":
    main()
