"""
Core components of the Price Tracker.
Contains database operations, validation, and constants.
"""

# Import and expose the main classes
from .database import Database
from .database import PriceDatabase
from .validators import ValidationInputs
from .constants import CATEGORIES , STORES

# Export for easy access
__all__ = [
    'Database',
    'ValidationInputs',
    'CATEGORIES',
    'PriceDatabase',
    'STORES'
]

# Package information
__version__ = "1.0.0"
__description__ = "Core functionality for price tracking"
