from agent import AIAgent

def main():
    agent = AIAgent()

    print("🤖 Simple AI Agent (type 'exit' to quit)")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Agent: Goodbye 👋")
            break

        response = agent.ask(user_input)
        print(f"Agent: {response}")

if __name__ == "__main__":
    main()
