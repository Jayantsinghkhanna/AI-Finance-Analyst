from llm import llm

from schemas.reflection_schema import (
    ReflectionOutput
)

from prompts.reflection_prompt import (
    REFLECTION_PROMPT
)


def reflection_agent(state):

    structured_llm = (
        llm.with_structured_output(
            ReflectionOutput
        )
    )

    prompt = f"""
    {REFLECTION_PROMPT}

    USER QUERY:
    {state['query']}

    INTENT:
    {state['intent']}

    EXECUTED SKILLS:
    {state.get('executed_skills', [])}

    CURRENT STATE:
    {state}
    """

    result = (
        structured_llm.invoke(
            prompt
        )
    )

    state["enough_information"] = (
        result.enough_information
    )

    state["next_skill"] = (
        result.next_skill
    )

    state["reflection_reasoning"] = (
        result.reasoning
    )

    print("\n===== REFLECTION =====")

    print(
        f"\nEnough Information: "
        f"{state['enough_information']}"
    )

    print(
        f"\nNext Skill: "
        f"{state['next_skill']}"
    )

    print(
        f"\nReasoning: "
        f"{state['reflection_reasoning']}"
    )

    return state