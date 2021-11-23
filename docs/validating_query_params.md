# Validating query params

#### Create validator
```python
from sanic_pydantic import RequestValidator

validator = RequestValidator()
```

---

#### Create schema
```
from pydantic import BaseModel


class QuerySchema(BaseModel):
    param: int
```

---

#### Use your validator as decorator
```python
from sanic import Sanic, response

app = Sanic('app')


@app.get('/')
@validator(query_schema=QuerySchema)
async def endpoint(request, query_: QuerySchema):
    return response.json(query_.dict())
```
