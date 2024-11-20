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
        self.__url_prefixes = ("http://", "socks5://", "ss://")

    @property
    def splitted(self) -> list[str]:
        _proxy = self.__proxy
        for url_prefix in self.__url_prefixes:
            if not self.__proxy.startswith(url_prefix):
                continue
            _url_prefix = url_prefix.replace("//", "")
            _proxy = self.__proxy.replace(url_prefix, _url_prefix, 1)
            if "@" in _proxy:
                _splitted = _proxy.split("@", maxsplit=1)
                _creds = _splitted[0].replace(_url_prefix, "", 1)
                return f"{_url_prefix}{_splitted[-1]}:{_creds}".split(":")
        return _proxy.split(self.__splitter)

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
        _message = f"[ProxyParser] Некорректно задан порт в прокси: {self.__proxy}"
        if self.__proxy.startswith(self.__prefixes):
            try:
                return int(self.splitted[2])
            except (ValueError, TypeError, IndexError) as e:
                raise ValueError(_message) from e
        try:
            return int(self.splitted[1])
        except (ValueError, TypeError, IndexError) as e:
            raise ValueError(_message) from e

    @property
    def user(self) -> str | None:
        if self.splitted[0] in self.__prefixes:
            # [type, ip, port, user, pswd]
            if len(self.splitted) == 5:
                return self.splitted[3]
        # [ip, port, user, pswd]
        if len(self.splitted) == 4:
            return self.splitted[2]

    @property
    def pswd(self) -> str | None:
        if self.splitted[0] in self.__prefixes:
            # [type, ip, port, user, pswd]
            if len(self.splitted) == 5:
                return self.splitted[4]
        # [ip, port, user, pswd]
        if len(self.splitted) == 4:
            return self.splitted[3]

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
