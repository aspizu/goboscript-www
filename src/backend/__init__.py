from __future__ import annotations

from starlette.applications import Starlette
from starlette.middleware import Middleware
from starlette.middleware.sessions import SessionMiddleware
from starlette.routing import Mount, Route
from starlette.staticfiles import StaticFiles

from . import routes
from .env import env

# <https://bugfactory.io/articles/disabling-304-not-modified-in-fastapi-staticfiles/>
if env.DEBUG:
    StaticFiles.is_not_modified = lambda self, *args, **kwargs: False  # noqa: ARG005


app = Starlette(
    debug=env.DEBUG,
    routes=[
        Route("/user/{username}", routes.user),
        Mount("/static", StaticFiles(directory="static", html=True), name="static"),
    ],
    middleware=[
        Middleware(
            SessionMiddleware,
            secret_key=env.SECRET_KEY,
            https_only=True,
            same_site="strict",
        )
    ],
)
