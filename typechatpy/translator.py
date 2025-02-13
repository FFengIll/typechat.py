import inspect
from typing import List, Type

import loguru
from pydantic import BaseModel
from pydantic.fields import inspect as pydantic_inspect

log = loguru.logger


class Translator:
    __default_template = """{prompt}
Respond strictly with JSON. The JSON should be compatible with the Python pydantic type Response from the following:
```python
{constraint}
```"""

    def __init__(self, template=__default_template) -> None:
        """
        init with a template or the default
        """
        self.template = template

    def _filter_model(self, *vars: List[object]):
        res = set()
        for v in vars:
            if inspect.isclass(v) and issubclass(v, BaseModel):
                # ignore `BaseModel` it self
                if v.__name__ == BaseModel.__name__:
                    continue
                if v in res:
                    log.warning(
                        "found duplicated model, check your code: {}", v.__name__
                    )
                res.add(v)
        return list(res)

    def _to_constraint(self, *args: Type[BaseModel]):
        pending = []

        # for given class type
        for c in args:
            code = pydantic_inspect.getsource(c)
            # print(code)
            pending.append(code)

        return "\n".join(pending)

    def generate(self, prompt, *models: Type[BaseModel], auto=False):
        """
        according to the instruction/prompt and related model define,
        generate typed instruction/prompt
        """
        if models:
            models = self._filter_model(*models)

        elif auto:
            # auto collect from caller

            # Get the current frame
            current_frame = inspect.currentframe()

            # Get the caller's frame
            caller_frame = current_frame.f_back

            # Get the caller's global variables
            caller_globals = caller_frame.f_globals

            models = list(caller_globals.values())

        constraint = self._to_constraint(*models)
        res = self._format(prompt=prompt, constraint=constraint)
        return res

    def _format(self, prompt, constraint):
        res = self.template.format(prompt=prompt, constraint=constraint)
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
