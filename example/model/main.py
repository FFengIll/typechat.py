from typechatpy.translator import Translator

prompt = "Provide 3 suggestions for specific places to go to in Seattle on a rainy day."


def main():
    t = Translator()

    # step by step filter values
    models = t._filter_model(*globals().values())
    constraint = t._to_constraint(*models)
    print(constraint)
    res = t._format(prompt, constraint)
    print(res)

    # all in one
    res = t.generate(prompt, *globals().values())
    print(res)


if __name__ == "__main__":
    main()
