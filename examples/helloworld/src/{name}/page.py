from evergreenpy import Green
from evergreenpy.responses import HTMLResponse


@Green.page
async def say_hello(request):
    name = request.path_params["name"]
    return HTMLResponse(f"<h1>Hello {name}</h1>")
