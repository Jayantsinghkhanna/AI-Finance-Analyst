from pydantic import BaseModel

class SentimentOutput(BaseModel):

    sentiment: str
    score: int
    summary: str