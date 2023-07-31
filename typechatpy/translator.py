from typing import Type

from pydantic.fields import inspect

from pydantic import BaseModel

template = """{prompt}
Respond strictly with JSON. The JSON should be compatible with the Python pydantic type Response from the following:
```
{constraint}
```"""


class Translator:
    def process(self, *args: Type[BaseModel]):
        pending = []
        for c in args:
            code = inspect.getsource(c)
            # print(code)
            pending.append(code)

        return "\n".join(pending)

    def generate(self, prompt, fmt):
        res = template.format(prompt=prompt, constraint=fmt)
        return res
