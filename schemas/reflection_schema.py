from pydantic import BaseModel
from typing import Optional


class ReflectionOutput(
    BaseModel
):

    enough_information: bool

    next_skill: Optional[str] = None

    reasoning: str