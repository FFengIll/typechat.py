from typechatpy import Translator
from pydantic import BaseModel


def test_translator():
    t = Translator()

    class Tmp(BaseModel):
        data: str
        id: int

    prompt = "Random generate."
    typed_prompt = t.generate(prompt, Tmp)
    print(typed_prompt)
