from src.agent import assistant_agent

def main():
    print("Welcome to your Personal Assistant.")
    print("Type 'exit' to quit.")
    while True:
        user_input = input("Enter your command: ")
        if user_input.strip().lower() == 'exit':
            break
        try:
            response = assistant_agent.run(user_input)
            print("Response:", response)
        except Exception as e:
            print("Error:", str(e))

if __name__ == "__main__":
    main()
