from agents.orchestrator import OrchestratorAgent
import sys

def print_welcome():
    print("\n=== Welcome to Coding Ninjas Learning Assistant ===")
    print("I can help you with:")
    print("1. Understanding programming concepts")
    print("2. Getting help with code")
    print("3. Creating study plans")
    print("4. Providing motivation")
    print("\nJust type your question or request, and I'll help you!")
    print("Type 'exit' or 'quit' to end the session.")
    print("==============================================\n")

def main():
    # Initialize the orchestrator
    orchestrator = OrchestratorAgent()
    
    # Print welcome message
    print_welcome()
    
    while True:
        try:
            # Get user input
            user_input = input("\nYou: ").strip()
            
            # Check for exit command
            if user_input.lower() in ['exit', 'quit']:
                print("\nThank you for using Coding Ninjas Learning Assistant. Goodbye!")
                break
            
            # Skip empty input
            if not user_input:
                continue
            
            # Process the request
            print("\nAssistant: ", end="")
            response = orchestrator.process_request(user_input)
            
        except KeyboardInterrupt:
            print("\n\nThank you for using Coding Ninjas Learning Assistant. Goodbye!")
            break
        except Exception as e:
            print(f"\nAn error occurred: {str(e)}")
            print("Please try again or type 'exit' to quit.")

if __name__ == "__main__":
    main()