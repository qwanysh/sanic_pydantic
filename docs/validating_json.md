# Validating JSON

#### Create validator
```python
from sanic_pydantic import RequestValidator

validator = RequestValidator()
```

---

#### Create schema
```
from pydantic import BaseModel


class JsonSchema(BaseModel):
    param: int
```

---

#### Use your validator as decorator
```python
from sanic import Sanic, response

app = Sanic('app')


@app.post('/')
@validator(json_schema=JsonSchema)
async def endpoint(request, json_: JsonSchema):
    return response.json(json_.dict())
```
