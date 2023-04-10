# envcfg


[![PyPI](https://img.shields.io/pypi/v/envcfg.svg)](https://pypi.python.org/pypi/envcfg)
[![Documentation Status](https://readthedocs.org/projects/envcfg/badge/?version=latest)](https://readthedocs.org/projects/envcfg/badge/?version=latest)


Use a decorator to specify environment variables with automatic type parsing!


* Free software: MIT license
* Documentation: https://envcfg.readthedocs.io.

Have you ever wanted to use dataclasses to parse environment variables ? With this python package, you can do so pretty easily:

```python
from envcfg import environment


@environment(prefix="MYAPP")
class Config:
    log_level: str
    n_workers: int
    worker_id: int
    timeout_seconds: float
    value_mapping: dict[str, str] = {"foo": "bar"}
    retry_timeouts: list[int] = [1000, 2000, 5000, 10000]
```

`envconfig` supports the following types out of the box :
- primitive literal types (`int`, `float`, `bool`, `str`)
- primitive collection types (`list`, `dict`, `set`, `tuple`, `frozenset`)
- JSON with the `envconfig.types.JSON` type
- `bytes` through the `envconfig.types.Base64` and `envconfig.types.Base85` types


The types are retrieved from the environment, and you can easily namespace your types using
the `prefix` keyword argument. If need be, you can provide your own parser-like function
to parse additional types by providing the `parsers` keyword argument to the decorator,
as demonstrated below. The provided parsers will take precedence over the parsers defined
by this library, except for collection types, which requires more advanced parsing.

```python
from envcfg import environment, ParserCallback

class Foo:
    ...

def parse_foo(varname: str, varvalue: str, vartype: type) -> Foo:
    return Foo()


PARSERS: dict[type, ParserCallback] = {
    Foo: parse_foo,
}

@environment(parsers=PARSERS)
class Config:
    foo: Foo

```

The expected environment variables are mapped one-to-one to their name in the
decorated class, prefixed with the provided `prefix` if applicable. For dict values,
one environment variable corresponds to one key in the dictionnary, as such :

```python
import os
from envcfg import environment


os.environ["FOO_KEY"] = "42"
os.environ["FOO_BAR"] = "34"

@environment()
class Config:
    foo: dict[str, int]

config = Config()
print(config.foo)  # Prints {"key": 42, "bar": 34}
```

When parsing collections, this library takes the liberty of parsing every collection
as its immutable counterpart, since the process should not have an impact on the environment
it executes in. This means that

- `list` types turn into `tuple`
- `set` types turn into `frozenset`
- `dict` remains unchanged, as there is no frozendict type
