import contextlib
from dataclasses import asdict
from typing import Literal, Optional

from tooler.models import ThonProxy, ProxyDrony


class ProxyParser:
    """Парсер проксей, если что-то не так, то райзит ValueError"""

    def __init__(self, proxy: str, splitter: str = ":"):
        self.__proxy = proxy
        self.__splitter = splitter

    @property
    def proxy(self) -> str:
        return self.__proxy

    @property
    def splitter(self) -> str:
        return self.__splitter

    @property
    def splitted(self) -> list[str]:
        return self.proxy.split(self.splitter)

    @property
    def type(self) -> Literal["http", "socks5", "ss"]:
        p_type = self.splitted[0]
        if p_type == "http":
            return "http"
        elif p_type == "socks5":
            return "socks5"
        elif p_type == "ss":
            return "ss"
        return "http"

    @property
    def ip(self) -> str:
        try:
            return self.splitted[1]
        except IndexError:
            raise ValueError("IP не задан!")

    @property
    def port(self) -> int:
        try:
            return int(self.splitted[2])
        except (ValueError, TypeError, IndexError):
            raise ValueError("Порт должен быть целым числом!")

    @property
    def user(self) -> Optional[str]:
        with contextlib.suppress(IndexError):
            return self.splitted[3]

    @property
    def pswd(self) -> Optional[str]:
        with contextlib.suppress(IndexError):
            return self.splitted[4]

    @property
    def url(self) -> str:
        if self.type == "ss":
            return ""
        if not self.user or not self.pswd:
            return f"{self.type}://{self.ip}:{self.port}"
        return f"{self.type}://{self.user}:{self.pswd}@{self.ip}:{self.port}"

    @property
    def thon(self) -> ThonProxy:
        return ThonProxy(self.type, self.ip, self.port, self.user, self.pswd)

    @property
    def asdict_thon(self) -> dict:
        return asdict(self.thon)

    @property
    def drony(self) -> ProxyDrony:
        return ProxyDrony(self.ip, self.port, self.user, self.pswd, self.type)

    @property
    def check(self) -> str:
        if not self.user or not self.pswd:
            return f"{self.type}:{self.ip}:{self.port}"
        return f"{self.type}:{self.ip}:{self.port}:{self.user}:{self.pswd}"


if __name__ == "__main__":
    print(ProxyParser("http:addr:1000:user:pswd").thon)
    print(ProxyParser("http:addr:1000:user:pswd").url)
