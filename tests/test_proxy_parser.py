from tooler import ProxyParser


def test_proxy_parser():
    proxy = "http:1.1.1.1:80:user:pswd"
    parser = ProxyParser(proxy)
    assert parser.type == "http"
    assert parser.ip == "1.1.1.1"
    assert parser.port == 80
    assert parser.user == "user"
    assert parser.pswd == "pswd"


def test_proxy_parser_without_type():
    proxy = "1.1.1.1:80:user:pswd"
    parser = ProxyParser(proxy)
    assert parser.type == "http"
    assert parser.ip == "1.1.1.1"
    assert parser.port == 80
    assert parser.user == "user"
    assert parser.pswd == "pswd"


def test_proxy_parser_without_type_and_creds():
    proxy = "1.1.1.1:80"
    parser = ProxyParser(proxy)
    assert parser.type == "http"
    assert parser.ip == "1.1.1.1"
    assert parser.port == 80
    assert parser.user is None
    assert parser.pswd is None


def test_proxy_parser_from_url():
    proxy = "http://user:pswd@1.1.1.1:80"
    parser = ProxyParser(proxy)
    assert parser.type == "http"
    assert parser.ip == "1.1.1.1"
    assert parser.port == 80
    assert parser.user == "user"
    assert parser.pswd == "pswd"


def test_proxy_parser_from_url_without_creds():
    proxy = "http://1.1.1.1:81"
    parser = ProxyParser(proxy)
    assert parser.type == "http"
    assert parser.ip == "1.1.1.1"
    assert parser.port == 81
    assert parser.user is None
    assert parser.pswd is None


def test_proxy_parser_socks5():
    proxy = "socks5:1.1.1.1:80:user:pswd"
    parser = ProxyParser(proxy)
    assert parser.type == "socks5"
    assert parser.ip == "1.1.1.1"
    assert parser.port == 80
    assert parser.user == "user"
    assert parser.pswd == "pswd"


def test_proxy_parser_from_url_socks5():
    proxy = "socks5://user:pswd@1.1.1.1:80"
    parser = ProxyParser(proxy)
    assert parser.type == "socks5"
    assert parser.ip == "1.1.1.1"
    assert parser.port == 80
    assert parser.user == "user"
    assert parser.pswd == "pswd"


def test_proxy_parser_from_url_without_creds_socks5():
    proxy = "socks5://1.1.1.1:81"
    parser = ProxyParser(proxy)
    assert parser.type == "socks5"
    assert parser.ip == "1.1.1.1"
    assert parser.port == 81
    assert parser.user is None
    assert parser.pswd is None
