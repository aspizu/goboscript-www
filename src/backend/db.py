from __future__ import annotations

from typing import Any

import psycopg
import psycopg.rows

from .env import env


async def db() -> psycopg.AsyncConnection[Any]:
    return await psycopg.AsyncConnection.connect(
        env.DATABASE_URL,
        row_factory=psycopg.rows.namedtuple_row,
    )
