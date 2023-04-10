from typing import Callable, Type

from envcfg.models import ParsedConfig, RawConfig
from envcfg.types import T, ParserCallback


def environment(
    *,
    parse: bool = True,
    prefix: str = "",
    delimiter: str = ",",
    parsers: dict[type, ParserCallback] = None,
) -> Callable[..., ParsedConfig | RawConfig]:
    def wrapper(klass: Type[T]) -> ParsedConfig | RawConfig:
        if parse:
            return ParsedConfig(
                klass,
                prefix=prefix,
                delimiter=delimiter,
                parsers=parsers,
            )
        return RawConfig(
            klass,
            prefix=prefix,
            delimiter=delimiter,
            parsers=parsers,
        )
    return wrapper
