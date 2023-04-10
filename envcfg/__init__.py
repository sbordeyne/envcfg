"""
Use a decorator to specify environment variables with automatic type parsing!
"""
__version__ = "1.0.0"
from envcfg.decorator import environment
from envcfg.models import ParsedConfig, RawConfig

__all__ = (
    "environment",
    "ParsedConfig",
    "RawConfig",
)
