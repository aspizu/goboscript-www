from __future__ import annotations

from typing import TYPE_CHECKING

from .db import db
from .templates import templates

if TYPE_CHECKING:
    from starlette.requests import Request
    from starlette.responses import Response


async def user(request: Request) -> Response:
    user = None
    async with await db() as conn, conn.cursor() as cur:
        if username := request.path_params.get("username"):
            await cur.execute(
                """
                SELECT * FROM account WHERE username = %(username)s
                """,
                {"username": username},
            )
            user = await cur.fetchone()
    return templates.TemplateResponse("user.jinja", {"request": request, "user": user})
