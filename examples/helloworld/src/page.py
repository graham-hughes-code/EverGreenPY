from evergreenpy import Green
from evergreenpy.responses import HTMLResponse


@Green.page
async def home(request):
    return HTMLResponse("<h1>Hello World</h1>")
