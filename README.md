# Typechat.py

A python implement to makes it easy to build natural language interfaces using types.

# Install
`pip install typechatpy`

# Usage
see [simple](example/simple) and more in [example](example).

```python
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

    # manual set
    res = t.generate(prompt, Response, VenueData)

    # auto analyse
    res = t.generate(prompt, auto=True)

    # set from globals
    res = t.generate(prompt, *globals().values())

    print(res)

if __name__ == "__main__":
    main()
```

# Example
see [simple](example/simple) for more detail (the `response` sample as bellow).

```json
{
  "data": [
    {
      "venue": "Seattle Art Museum",
      "description": "Explore the extensive collection of art from around the world at the Seattle Art Museum. From contemporary art to ancient artifacts, there is something for everyone to enjoy."
    },
    {
      "venue": "Pike Place Market",
      "description": "Indulge in a unique shopping experience at Pike Place Market. Browse through local produce, crafts, and specialty shops, and enjoy a variety of delicious food options."
    },
    {
      "venue": "Chihuly Garden and Glass",
      "description": "Marvel at the stunning glass artworks created by Dale Chihuly at the Chihuly Garden and Glass exhibit. The vibrant colors and intricate designs are sure to captivate your senses."
    }
  ]
}
```


# TODO
- [x] translator
- [ ] validator
- [ ] ~~llm interact~~

# Ref
- [pydantic](https://github.com/pydantic/pydantic)
- [typechat](https://github.com/microsoft/TypeChat)