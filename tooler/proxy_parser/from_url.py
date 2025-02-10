from dataclasses import asdict

from .models import ThonProxy


class ProxyParserFromUrl:
    """Парсер прокси из URL"""

    def __init__(self, proxy: str):
        self.__splitted = proxy.split("://")

    @property
    def with_creds(self) -> bool:
        """
        Проверяет, содержит ли строка символ "@".
        Возвращает:
            bool: True, если содержит, иначе False
        """
        return "@" in self.__splitted[1]

    @property
    def splitted_with_dog(self) -> list[str]:
        """
        Разделяет строку на части по символу "@".
        Возвращает:
            list[str]: Список строк
        """
        if self.with_creds:
            return self.__splitted[1].split("@")
        return self.__splitted

    @property
    def proxy_type(self) -> str:
        """
        Парсит тип прокси.
        Поддерживаемые типы: http, socks5
        Возвращает:
            str: Тип прокси
        Исключения:
            ValueError: Если тип прокси не поддерживается
        """
        proxy_type = self.__splitted[0]
        if proxy_type == "https":
            proxy_type = "http"
        if proxy_type not in ["http", "socks5"]:
            raise ValueError(f"Invalid proxy type: {proxy_type}")
        return proxy_type

    @property
    def addr(self) -> str:
        """
        Парсит адрес прокси.
        Возвращает:
            str: Адрес прокси
        """
        if self.with_creds:
            return self.splitted_with_dog[1].split(":")[0]
        return self.splitted_with_dog[1].split(":")[0]

    @property
    def port(self) -> int:
        """
        Парсит порт прокси.
        Возвращает:
            int: Порт прокси
        Исключения:
            ValueError: Если порт не является числом
            IndexError: Если нет порта
        """
        if self.with_creds:
            return int(self.splitted_with_dog[1].split(":")[1])
        return int(self.splitted_with_dog[1].split(":")[1])

    @property
    def user(self) -> str | None:
        """
        Парсит имя пользователя для прокси.
        Возвращает:
            str | None: Имя пользователя или None
        """
        if self.with_creds:
            return self.splitted_with_dog[0].split(":")[0]

    @property
    def pswd(self) -> str | None:
        """
        Парсит пароль для прокси.
        Возвращает:
            str | None: Пароль или None
        """
        if self.with_creds:
            return self.splitted_with_dog[0].split(":")[1]

    @property
    def thon(self) -> ThonProxy:
        """
        Возвращает объект ThonProxy.
        """
        return ThonProxy(
            proxy_type=self.proxy_type,
            addr=self.addr,
            port=self.port,
            username=self.user,
            password=self.pswd,
        )

    @property
    def thon_dict(self) -> dict:
        """
        Возвращает словарь, содержащий параметры прокси для Thon.
        """
        return asdict(self.thon)
