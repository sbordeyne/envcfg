import abc
import os
from typing import Type

from envcfg.types import VarType, T, ParserCallback


class BaseConfig(metaclass=abc.ABCMeta):
    def __init__(
        self,
        klass: Type[T],
        *,
        prefix: str = "",
        delimiter: str = ",",
        parsers: dict[type, ParserCallback] = None,
        **kwargs,
    ):
        self.__annotations__ = klass.__annotations__
        self.__doc__ = klass.__doc__
        self._delimiter = delimiter
        self._prefix = prefix
        self._parsers = parsers or {}
        for varname, vartype in klass.__annotations__.items():
            if varname.startswith("_"):
                continue
            envname = varname
            if prefix:
                envname = f"{prefix}_{envname}"
            envname = envname.upper()
            default = getattr(klass, varname, None)
            varvalue = os.getenv(envname, default)
            if varvalue is None:
                raise ValueError(
                    f"{envname} is a required environment variable, no default value provided."
                )
            setattr(self, varname, self._parse(varname, varvalue, vartype))

    @abc.abstractmethod
    def _parse(self, varname: str, varvalue: str, vartype: VarType) -> VarType:
        raise NotImplementedError()
