from __future__ import annotations

import environs

_env = environs.Env()
_env.read_env()


class env:  # noqa: N801
    DEBUG: bool = _env.bool("DEBUG")
    HOST: str = _env.str("HOST")
    DATABASE_URL: str = _env.str("DATABASE_URL")
    SECRET_KEY: str = _env.str("SECRET_KEY")
