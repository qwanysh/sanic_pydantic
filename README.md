# sanicpydantic
Pydantic validation for Sanic framework

#### Install:
```bash
pip install sanicpydantic
```

#### Example:
```python
from pydantic import BaseModel
from sanic_pydantic import RequestValidator

validator = RequestValidator()

...

class QueryModel(BaseModel):
    str_param: str
    int_param: int
    bool_param: bool


@app.get('/')
@validator(query_schema=QueryModel)
def get_endpoint(request, query_: QueryModel):
    ...


class JsonModel(BaseModel):
    str_field: str
    int_field: int
    bool_field: bool


@app.post('/')
@validator(json_schema=JsonModel)
def post_endpoint(request, json_: JsonModel):
    ...

```
