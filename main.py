from MongoAgent import MongoAgent
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

def main():
    try:
        # Read environment variables
        mongo_url = os.getenv("MONGO_URL")
        openai_token = os.getenv("OPENAI_TOKEN")
        db_name = os.getenv("DB_NAME")

        if not all([mongo_url, openai_token, db_name]):
            raise ValueError("One or more environment variables are missing. Please check your .env file.")

        # Initialize the agent
        agent = MongoAgent(
            mongoURL=mongo_url,
            openAI_token=openai_token,
            db_name=db_name
        )

        # Start interactive session
        while True:
            user_prompt = input("\nEnter your query (or type 'q' to quit): ")
            if user_prompt.lower() == 'q':
                print("👋 Exiting. Goodbye!")
                break

            # AI generates query
            ai_query = agent.execute(prompt=user_prompt)
            print("\n🤖 AI Response:\n", ai_query)

            # Execute generated query
            result = agent.execute_from_ai_query(ai_query)
            print("\n📄 Query Result:\n", result)

    except Exception as e:
        print(f"❌ An error occurred: {e}")

if __name__ == "__main__":
    main()
