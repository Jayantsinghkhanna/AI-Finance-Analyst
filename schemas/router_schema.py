from pydantic import BaseModel


class RouterOutput(
    BaseModel
):

    intent: str

    ticker: str