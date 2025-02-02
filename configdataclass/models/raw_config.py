from configdataclass.models import BaseConfig
from configdataclass.types import VarType


class RawConfig(BaseConfig):
    def _parse(self, varname: str, varvalue: str, vartype: VarType) -> VarType:
        return str(varvalue)
