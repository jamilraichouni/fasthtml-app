from fasthtml import ft  # type: ignore
from fasthtml.common import fast_app, serve  # type: ignore

BTNCLS = "px-4 py-2 bg-blue-500 text-white rounded"

app, rt = fast_app(
    hdrs=(
        ft.Script(
            src="static/js/tailwind-3.4.15.js",
        ),
    ),
    # default_hdrs=False,
    pico=False,
    live=True,
)


@app.get("/")
def index():
    return ft.Div(
        nav(),
        home(),
        cls="flex flex-col grow min-h-screen",
    )


@app.get("/home")
def home():
    return (
        ft.Div(
            ft.P("Home", id="paragraph", cls="text-white"),
            id="main",
            cls="bg-gray-900 min-h-screen",
        ),
    )


@app.get("/projects")
def projects():
    return (
        ft.Div(
            ft.P("Projects", cls="text-white"),
            id="main",
            cls="bg-gray-900 min-h-screen",
        ),
    )


def buttons(button_defs):
    button_elements = [
        ft.Button(
            b["label"],
            cls=BTNCLS,
            hx_target="#main",
            hx_get=b["url"],
            hx_swap="outerHTML",
        )
        for b in button_defs
    ]

    div = ft.Div(
        *button_elements,
        cls="flex items-center space-x-4",
    )
    return div


def nav():
    button_defs = [
        {"label": "Home", "url": "/home"},
        {"label": "Projects", "url": "/projects"},
        {"label": "Sessions", "url": "/sessions"},
        {"label": "Session overview", "url": "/session-over"},
    ]
    return (
        ft.Nav(
            ft.Div(
                buttons(button_defs),
                cls="flex justify-between items-center p-4",
            ),
            cls="bg-gray-300 shadow-md",
        ),
    )


if __name__ == "__main__":
    serve()
