from schemas.router_schema import (
    RouterOutput
)

from llm import llm as router_llm

from prompts.router_prompt import (
    ROUTER_PROMPT
)


def router_agent(state):

    structured_llm = (
        router_llm.with_structured_output(
            RouterOutput
        )
    )

    result = structured_llm.invoke(
        ROUTER_PROMPT +
        "\n\n" +
        state["query"]
    )

    state["intent"] = result.intent
    state["ticker"] = result.ticker

    return state