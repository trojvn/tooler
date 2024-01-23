from typing import Literal


class ProxyParser:
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
    def type(self) -> Literal["http", "socks5"]:
        p_type = self.splitted[0]
        if p_type == "http":
            return "http"
        elif p_type == "socks5":
            return "socks5"
        return "http"

    def __main(self):
        """Точка входа"""
