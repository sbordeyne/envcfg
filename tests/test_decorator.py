import os
from typing import Generic, TypeVar

import pytest

from classenv import environment
from classenv.models import BaseConfig


def test_parsed_config_correct(config):
    assert config.integer == 42
    assert config.octal == 42
    assert config.hexa == 42
    assert config.binary == 42
    assert config.string == "42"
    assert config.boolean is True
    assert config.bool_num is True
    assert config.bool_yes is True
    assert config.bool_y is True
    assert config.bool_no is False
    assert config.floating == 42.0
    assert tuple(config.map_str_str.keys()) == ("FOO",)
    assert tuple(config.map_str_int.values()) == ("42",)
    assert tuple(config.map_str_float.values()) == ("42.0",)
    assert tuple(config.map_str_bool.values()) == ("true",)
    assert config.array_str == ("42", "69")
    assert config.array_int == (42, 69)
    assert config.array_float == (42.0, 69.0)
    assert config.array_bool == (True, False)
    assert len(config.array_any) == 0
    assert not hasattr(config, "_private")
    assert isinstance(config.set_str, frozenset)
    assert config.set_str == frozenset(("42", "69"))
    assert config.base64 == b"hello"
    assert config.base85 == b"hello"
    assert config.json == {"foo": "bar"}
    assert config.path.name == "null"
    assert config.array_anyvalue == ("42", "69")
    assert config.set_anyvalue == frozenset(("42", "69"))


def test_raw_config_correct(raw_config):
    assert raw_config.integer == "42"
    assert raw_config.string == "42"
    assert raw_config.boolean == "true"
    assert raw_config.floating == "42.0"
    assert raw_config.array_str == "42,69"


def test_missing_env():
    with pytest.raises(ValueError):
        @environment(prefix="MISSING", delimiter=",")
        class Config:
            integer: int
        assert Config.integer == 42


def test_wrong_abc():
    with pytest.raises(TypeError):
        class CustomConfig(BaseConfig):
            pass
        CustomConfig()


def test_parsed_config_invalid_int():
    os.environ["INVALID_INTEGER"] = "abc"
    with pytest.raises(ValueError):
        @environment(prefix="INVALID", delimiter=",")
        class Config:
            integer: int
        assert Config.integer == 42


def test_parsed_config_customized():
    os.environ["CUSTOM_INTEGER"] = "42"
    PARSERS = {
        int: lambda n, v, t: int(v) * 2,
    }

    @environment(prefix="CUSTOM", delimiter=",", parsers=PARSERS)
    class Config:
        integer: int

    assert Config.integer == 84


def test_parsed_config_vartype_not_found():
    os.environ["NOTFOUND_BYTES"] = "hello"
    with pytest.raises(TypeError):
        @environment(prefix="NOTFOUND")
        class Config:
            bytes: bytes
        assert Config.bytes == b"hello"


def test_parsed_config_custom_collection():
    os.environ["CUSTOMCOLLECTION_TEST"] = "42,69"
    T = TypeVar("T")

    class Array(Generic[T]):
        def __init__(self, *a):
            self.args = a

        def __eq__(self, other):
            return self.args == other

    with pytest.raises(TypeError):
        @environment(prefix="CUSTOMCOLLECTION", delimiter=",")
        class Config:
            test: Array[int]
        assert Config.test == Array(42, 69)


def test_parsed_config_dict_no_prefix():
    os.environ["DICT_FOO"] = "BAR"

    @environment()
    class Config:
        dict: dict[str, str]

    assert "FOO" in Config.dict
    assert Config.dict["FOO"] == "BAR"
