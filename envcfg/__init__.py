"""
Use a decorator to specify environment variables with automatic type parsing!
"""
__version__ = "1.1.0"
from envcfg.decorator import environment
from envcfg.models import ParsedConfig, RawConfig
from envcfg.types import JSON, Base64, Base85


__all__ = (
    "environment",
    "ParsedConfig",
    "RawConfig",
    "JSON",
    "Base64",
    "Base85",
)
