from agent import StoryAgent

def main():
    agent = StoryAgent()

    print("📖 Bhagwat Gita Storyteller (type 'exit' to quit)")
    while True:
        quote = input("\nEnter a Bhagwat Gita quote/shloka: ")
        if quote.lower() in ["exit", "quit"]:
            print("Agent: Goodbye 👋")
            break

        try:
            story = agent.create_story(quote)
            print(f"\nAgent's Story:\n{story}")
        except Exception as e:
            print(f"⚠️ Error: {e}")

if __name__ == "__main__":
    main()
