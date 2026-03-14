from agents.supervisor_agent import SupervisorAgent


def start_rosteriq_console():
    # Initialize the main agent
    ai_agent = SupervisorAgent()

    print("RosterIQ Assistant Started. Type 'exit' to stop.\n")

    while True:
        user_input = input("Ask RosterIQ: ")

        # Exit condition
        if user_input.lower() in ["exit", "quit"]:
            print("Shutting down RosterIQ...")
            break

        # Process query through supervisor agent
        response = ai_agent.handle_query(user_input)

        print("\nResponse:")
        print(response)
        print("-" * 40)


if __name__ == "__main__":
    start_rosteriq_console()