from graph.workflow import graph


def main():

    print(
        "\n=== Autonomous Finance Analyst ===\n"
    )

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

            print(
                "\n===================================="
            )

            print(
                f"\nTicker: "
                f"{result.get('ticker', 'N/A')}"
            )

            print(
                f"\nIntent: "
                f"{result.get('intent', 'N/A')}"
            )

            recommendation = result.get(
                "recommendation",
                {}
            )

            if recommendation:

                print(
                    f"\nRecommendation: "
                    f"{recommendation.get('recommendation')}"
                )

                print(
                    f"Confidence: "
                    f"{recommendation.get('confidence')}%"
                )

            print(
                f"\nExecuted Skills:"
            )

            print(
                result.get(
                    "executed_skills",
                    []
                )
            )

            print(
                f"\nPDF Report:"
            )

            print(
                result.get(
                    "pdf_path",
                    "Not Generated"
                )
            )

            print(
                "\n===================================="
            )

            view_report = input(
                "\nShow full report? (y/n): "
            )

            if view_report.lower() == "y":

                print(
                    "\n========== REPORT ==========\n"
                )

                print(
                    result.get(
                        "final_report",
                        "No report generated."
                    )
                )

                print(
                    "\n============================\n"
                )

        except Exception as e:

            print(
                f"\nERROR: {e}"
            )


if __name__ == "__main__":
    main()