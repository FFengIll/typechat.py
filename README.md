# typechat.py

A python implement to makes it easy to build natural language interfaces using types.

# example
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
- [ ] llm interact

# ref
- [pydantic](https://github.com/pydantic/pydantic)
- [typechat](https://github.com/microsoft/TypeChat)