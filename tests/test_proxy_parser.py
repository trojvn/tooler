from tooler import ProxyParser


def test_proxy_parser():
    proxy = "http:1.1.1.1:80:user:pswd"
    parser = ProxyParser(proxy)
    assert parser.type == "http"
    assert parser.ip == "1.1.1.1"
    assert parser.port == 80
    assert parser.user == "user"
    assert parser.pswd == "pswd"


def test_proxy_parser_from_url():
    proxy = "http://user:pswd@1.1.1.1:80"
    parser = ProxyParser(proxy)
    assert parser.type == "http"
    assert parser.ip == "1.1.1.1"
    assert parser.port == 80
    assert parser.user == "user"
    assert parser.pswd == "pswd"
