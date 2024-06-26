# EverGreenPY

Directory based routing python web framework built on top of [Starlette](https://www.starlette.io/).

## Example

/app.py:
```python
from evergreenpy import Green

app = Green()
```

/src/page.py:
```python
from evergreenpy import Green
from evergreenpy.responses import HTMLResponse


@Green.page
async def home(request):
    return HTMLResponse("<h1>Hello World</h1>")
```

/src/{name}/page.py:
```python
from evergreenpy import Green
from evergreenpy.responses import HTMLResponse


@Green.page
async def say_hello(request):
    name = request.path_params["name"]
    return HTMLResponse(f"<h1>Hello {name}</h1>")
```

Then run the application using Uvicorn:

`$ uvicorn app:app`

You can find more examples [here](/examples/).