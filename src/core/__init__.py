"""
Core package initialization
"""
from .config import Config
from .workshop import WorkshopManager
from .addon_json import AddonJSON

__all__ = ['Config', 'WorkshopManager', 'AddonJSON']
