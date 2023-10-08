import inspect
from typing import List, Type

from pydantic import BaseModel
from pydantic.fields import inspect as pydantic_inspect


class Translator:
    __template = """{prompt}
Respond strictly with JSON. The JSON should be compatible with the Python pydantic type Response from the following:
```
{constraint}
```"""

    def filter_model(self, *vars: List[object]):
        res = []
        for v in vars:
            if inspect.isclass(v) and issubclass(v, BaseModel):
                # ignore `BaseModel` it self
                if v.__name__ == BaseModel.__name__:
                    continue
                res.append(v)
        return res

    def to_constraint(self, *args: Type[BaseModel]):
        pending = []

        # for given class type
        for c in args:
            code = pydantic_inspect.getsource(c)
            # print(code)
            pending.append(code)

        return "\n".join(pending)

    def generate(self, prompt, *models: Type[BaseModel]):
        models = self.filter_model(*models)
        constraint = self.to_constraint(*models)
        res = self.format(prompt=prompt, constraint=constraint)
        return res

    def format(self, prompt, constraint):
        res = self.__template.format(prompt=prompt, constraint=constraint)
        return res


class TranslatorLegacy:
    __template = """{prompt}
Respond strictly with JSON. The JSON should be compatible with the Python pydantic type Response from the following:
```
{constraint}
```"""

    def filter(self, vars: List[object]):
        res = []
        for v in vars:
            if inspect.isclass(v) and issubclass(v, BaseModel):
                # ignore `BaseModel` it self
                if v.__name__ == BaseModel.__name__:
                    continue
                res.append(v)
        return res

    def process(self, *args: Type[BaseModel]):
        pending = []

        # for given class type
        for c in args:
            code = pydantic_inspect.getsource(c)
            # print(code)
            pending.append(code)

        return "\n".join(pending)

    def generate(self, prompt, fmt):
        res = self.__template.format(prompt=prompt, constraint=fmt)
        return res
