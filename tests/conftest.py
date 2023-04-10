import os

import pytest

from envcfg import environment


@pytest.fixture()
def config():
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

    @environment(prefix="TEST", delimiter=",")
    class Config:
        integer: int
        string: str
        boolean: bool
        floating: float
        map_str_str: dict[str, str] = {}
        map_str_int: dict[str, int] = {}
        map_str_float: dict[str, float] = {}
        map_str_bool: dict[str, bool] = {}
        array_str: list[str]
        array_int: list[int]
        array_float: list[float]
        array_bool: list[bool]
    return Config
