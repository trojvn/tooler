import pytest

from tooler import ProxyParserFromUrl


def test_wrong_proxy_type():
    proxy_parser = ProxyParserFromUrl("wrong://127.0.0.1:9050")
    with pytest.raises(ValueError):
        assert proxy_parser.proxy_type == "wrong"


def test_proxy_parser_https():
    proxy_parser = ProxyParserFromUrl("https://127.0.0.1:9050")
    assert proxy_parser.proxy_type == "http"
    assert proxy_parser.addr == "127.0.0.1"
    assert proxy_parser.port == 9050
    assert not proxy_parser.with_creds


def test_proxy_parser_wrong_port():
    proxy_parser = ProxyParserFromUrl("http://127.0.0.1")
    with pytest.raises(IndexError):
        assert proxy_parser.port == 9050


def test_proxy_parser_wrong_port_type():
    proxy_parser = ProxyParserFromUrl("http://127.0.0.1:wrong")
    with pytest.raises(ValueError):
        assert proxy_parser.port == 9050


def test_proxy_parser():
    proxy_parser = ProxyParserFromUrl("socks5://user:pass@127.0.0.1:9050")
    assert proxy_parser.proxy_type == "socks5"
    assert proxy_parser.addr == "127.0.0.1"
    assert proxy_parser.port == 9050
    assert proxy_parser.user == "user"
    assert proxy_parser.pswd == "pass"
    assert proxy_parser.with_creds


def test_proxy_parser_no_creds():
    proxy_parser = ProxyParserFromUrl("socks5://127.0.0.1:9050")
    assert proxy_parser.proxy_type == "socks5"
    assert proxy_parser.addr == "127.0.0.1"
    assert proxy_parser.port == 9050
    assert not proxy_parser.with_creds
    assert proxy_parser.user is None
    assert proxy_parser.pswd is None


def test_proxy_parser_http():
    proxy_parser = ProxyParserFromUrl("http://127.0.0.1:9050")
    assert proxy_parser.proxy_type == "http"
    assert proxy_parser.addr == "127.0.0.1"
    assert proxy_parser.port == 9050
    assert not proxy_parser.with_creds
    assert proxy_parser.user is None
    assert proxy_parser.pswd is None


def test_proxy_parser_socks5():
    proxy_parser = ProxyParserFromUrl("socks5://127.0.0.1:9050")
    assert proxy_parser.proxy_type == "socks5"
    assert proxy_parser.addr == "127.0.0.1"
    assert proxy_parser.port == 9050
    assert not proxy_parser.with_creds
    assert proxy_parser.user is None
    assert proxy_parser.pswd is None
