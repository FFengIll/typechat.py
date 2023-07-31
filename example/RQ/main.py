from typing import List

from pydantic import BaseModel

from typechatpy.translator import Translator


class RelatedQ(BaseModel):
    question: str


class Response(BaseModel):
    answer: str
    rq: List[RelatedQ]


def main():
    t = Translator()
    fmt = t.process(Response)

    prompt = "Provide `answer` of my question and 3 related question (as `rq`). Question: what is redis?"

    res = t.generate(prompt, fmt)
    print(res)


if __name__ == "__main__":
    main()
