from typing import List

from pydantic import BaseModel

from typechatpy.translator import Translator


class VenueData(BaseModel):
    venue: str
    description: str


class Response(BaseModel):
    data: List[VenueData]


prompt = "Provide 3 suggestions for specific places to go to in Seattle on a rainy day."


def main():
    t = Translator()

    res = t.generate(prompt, auto=True)

    print(res)


if __name__ == "__main__":
    main()
