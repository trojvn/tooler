from dataclasses import dataclass
from typing import Literal


@dataclass
class ThonProxy:
    """Тип для прокси, который используется в Thon"""

    proxy_type: Literal["http", "socks5"] | str
    addr: str
    port: int
    username: str | None = None
    password: str | None = None
    rdns: bool = True
