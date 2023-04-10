def test_config_correct(config):
    assert config.integer == 42
    assert config.string == "42"
    assert config.boolean is True
    assert config.floating == 42.0
    assert tuple(config.map_str_str.keys()) == ("FOO",)
    assert tuple(config.map_str_int.values()) == ("42",)
    assert tuple(config.map_str_float.values()) == ("42.0",)
    assert tuple(config.map_str_bool.values()) == ("true",)
    assert config.array_str == ("42", "69")
    assert config.array_int == (42, 69)
    assert config.array_float == (42.0, 69.0)
    assert config.array_bool == (True, False)
