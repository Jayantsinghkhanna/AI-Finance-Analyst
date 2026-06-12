from graph.workflow import graph


def main():

    print("\n=== Agentic Finance Analyst ===\n")

    while True:

        query = input(
            "\nEnter Finance Query (or 'exit'): "
        )

        if query.lower() == "exit":
            break

        try:

            result = graph.invoke(
                {
                    "query": query
                }
            )

            print("\n========== STATE ==========\n")

            for key, value in result.items():

                print(f"\n{key.upper()}:")

                print(value)

            print(
                "\n===========================\n"
            )

        except Exception as e:

            print(
                f"\nERROR: {e}"
            )


if __name__ == "__main__":
    main()