from evergreenpy import Green
from evergreenpy.responses import HTMLResponse


@Green.page
async def home(request):
    return HTMLResponse("""
        <h1>Static Dir Example</h1>
        <img src="static/python-logo.png" alt="python">
    """)
