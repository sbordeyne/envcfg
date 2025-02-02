import os
from pathlib import Path

import pytest

from configdataclass import environment, Base64, Base85, JSON


@pytest.fixture()
def config():
    os.environ["TEST_INTEGER"] = "42"
    os.environ["TEST_OCTAL"] = "0o52"
    os.environ["TEST_HEXA"] = "0x2a"
    os.environ["TEST_BINARY"] = "0b101010"
    os.environ["TEST_STRING"] = "42"
    os.environ["TEST_BOOLEAN"] = "true"
    os.environ["TEST_BOOL_NUM"] = "1"
    os.environ["TEST_BOOL_YES"] = "yes"
    os.environ["TEST_BOOL_Y"] = "y"
    os.environ["TEST_BOOL_NO"] = "no"
    os.environ["TEST_FLOATING"] = "42.0"
    os.environ["TEST_MAP_STR_STR_FOO"] = "42"
    os.environ["TEST_MAP_STR_INT_FOO"] = "42"
    os.environ["TEST_MAP_STR_FLOAT_FOO"] = "42.0"
    os.environ["TEST_MAP_STR_BOOL_FOO"] = "true"
    os.environ["TEST_ARRAY_STR"] = "42,69"
    os.environ["TEST_ARRAY_INT"] = "42,69"
    os.environ["TEST_ARRAY_FLOAT"] = "42.0,69.0"
    os.environ["TEST_ARRAY_BOOL"] = "true,false"
    os.environ["TEST_SET_STR"] = "42,69"
    os.environ["TEST_BASE64"] = "aGVsbG8="
    os.environ["TEST_BASE85"] = "Xk~0{Zv"
    os.environ["TEST_JSON"] = '{"foo": "bar"}'
    os.environ["TEST_PATH"] = "/dev/null"
    os.environ["TEST_ARRAY_ANYVALUE"] = "42,69"
    os.environ["TEST_SET_ANYVALUE"] = "42,69"

    @environment(prefix="TEST", delimiter=",")
    class Config:
        _private: bool
        integer: int
        octal: int
        hexa: int
        binary: int
        string: str
        boolean: bool
        bool_num: bool
        bool_yes: bool
        bool_y: bool
        bool_no: bool
        floating: float
        map_str_str: dict[str, str]
        map_str_int: dict[str, int] = {}
        map_str_float: dict[str, float] = {}
        map_str_bool: dict[str, bool] = {}
        array_str: list[str]
        array_int: list[int]
        array_float: list[float]
        array_bool: list[bool]
        array_any: list
        array_anyvalue: list
        set_str: set[str]
        set_any: set
        set_anyvalue: set
        base64: Base64
        base85: Base85
        json: JSON
        path: Path

    return Config


@pytest.fixture()
def raw_config():
    os.environ["TEST_INTEGER"] = "42"
    os.environ["TEST_STRING"] = "42"
    os.environ["TEST_BOOLEAN"] = "true"
    os.environ["TEST_FLOATING"] = "42.0"
    os.environ["TEST_MAP_STR_STR_FOO"] = "42"
    os.environ["TEST_MAP_STR_INT_FOO"] = "42"
    os.environ["TEST_MAP_STR_FLOAT_FOO"] = "42.0"
    os.environ["TEST_MAP_STR_BOOL_FOO"] = "true"
    os.environ["TEST_ARRAY_STR"] = "42,69"
    os.environ["TEST_ARRAY_INT"] = "42,69"
    os.environ["TEST_ARRAY_FLOAT"] = "42.0,69.0"
    os.environ["TEST_ARRAY_BOOL"] = "true,false"

    @environment(prefix="TEST", delimiter=",", parse=False)
    class Config:
        integer: int
        string: str
        boolean: bool
        floating: float
        map_str_str: dict[str, str]
        map_str_int: dict[str, int] = {}
        map_str_float: dict[str, float] = {}
        map_str_bool: dict[str, bool] = {}
        array_str: list[str]
        array_int: list[int]
        array_float: list[float]
        array_bool: list[bool]
    return Config
