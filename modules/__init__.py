"""
Feature modules for the Price Tracker.
Each module handles a specific aspect of the application.
"""

# Import all module classes
from .product_tracker import ProductTracker
from .price_scraper import PriceScraper
from .price_alerts import PriceAlerts

# Export for easy access
__all__ = [
    'ProductTracker',
    'PriceScraper', 
    'PriceAlerts',
]

# Package information
__version__ = "1.0.0"
__description__ = "Feature modules for price tracking application"