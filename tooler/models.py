from dataclasses import dataclass
from typing import Literal, Optional


@dataclass
class ThonProxy:
    proxy_type: Literal["http", "socks5"] | str
    addr: str
    port: int
    username: Optional[str]
    password: Optional[str]
    rdns: bool = True


@dataclass
class ProxyDrony:
    hostname: str
    port: int
    user: Optional[str]
    pswd: Optional[str]
    type: str
