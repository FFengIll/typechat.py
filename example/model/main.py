import sys

from typechatpy.translator import Translator

from model import *

prompt = "Provide 3 suggestions for specific places to go to in Seattle on a rainy day."


def main():
    t = Translator()

    # auto filter values
    models = t.filter(globals().values())
    fmt = t.process(*models)
    print(fmt)

    res = t.generate(prompt, fmt)
    print(res)


if __name__ == "__main__":
    main()
