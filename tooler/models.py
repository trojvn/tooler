from dataclasses import dataclass
from typing import Literal


@dataclass
class ThonProxy:
    proxy_type: Literal["http", "socks5"] | str
    addr: str
    port: int
    username: str | None
    password: str | None
    rdns: bool = True


@dataclass
class ProxyDrony:
    hostname: str
    port: int
    user: str | None
    pswd: str | None
    type: str
