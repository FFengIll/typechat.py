import typechatpy
from pydantic import BaseModel


def test_translate():
    class Tmp(BaseModel):
        data: str
        id: int

    prompt = "Random generate."

    res = typechatpy.translate(prompt, Tmp)
    print(res)


def test_Translator():
    t = typechatpy.Translator()

    class Tmp(BaseModel):
        data: str
        id: int

    prompt = "Random generate."
    typed_prompt = t.generate(prompt, Tmp)
    print(typed_prompt)
