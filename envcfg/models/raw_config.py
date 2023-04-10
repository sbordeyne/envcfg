from envcfg.models import BaseConfig
from envcfg.types import VarType


class RawConfig(BaseConfig):
    def _parse(self, varname: str, varvalue: str, vartype: VarType) -> VarType:
        return str(varvalue)
