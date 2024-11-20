import contextlib
from dataclasses import asdict
from typing import Literal

from .models import ProxyDrony, ThonProxy


class ProxyParser:
    """Парсер проксей, если что-то не так, то райзит ValueError"""

    def __init__(self, proxy: str, splitter: str = ":"):
        proxy = proxy.replace("https:", "http:")
        self.__proxy, self.__splitter = proxy, splitter
        self.__prefixes = ("http", "socks5", "ss")

    @property
    def splitted(self) -> list[str]:
        return self.__proxy.split(self.__splitter)

    @property
    def type(self) -> Literal["http", "socks5", "ss"]:
        p_type = self.splitted[0]
        match p_type:
            case "http":
                return "http"
            case "socks5":
                return "socks5"
            case "ss":
                return "ss"
        return "http"

    @property
    def ip(self) -> str:
        if self.__proxy.startswith(self.__prefixes):
            try:
                return self.splitted[1]
            except IndexError as e:
                _message = f"[ProxyParser] Не найден IP в прокси: {self.__proxy}"
                raise ValueError(_message) from e
        return self.splitted[0]

    @property
    def port(self) -> int:
        try:
            return int(self.splitted[2])
        except (ValueError, TypeError, IndexError) as e:
            _message = f"[ProxyParser] Некорректно задан порт в прокси: {self.__proxy}"
            raise ValueError(_message) from e

    @property
    def user(self) -> str | None:
        with contextlib.suppress(IndexError):
            return self.splitted[3]

    @property
    def pswd(self) -> str | None:
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
