# 🛒 E-Commerce Price Tracker

<div align="center">

![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Status](https://img.shields.io/badge/status-active-success.svg)

**Track prices • Set alerts • Save money**

A powerful, automated price tracking system that monitors product prices across multiple online stores and sends desktop alerts when prices drop below your target.

</div>

## ✨ Features

- **🛍️ Multi-Store Support**: Track prices from Instant Gaming, Eneba, Ivory, 
- **🔔 Desktop Notifications**: Get real-time alerts when prices hit your targets
- **📊 Price History**: View historical price data with trends and analytics
- **🔄 Automatic Scheduling**: Set up weekly automatic price checks
- **📱 Import/Export**: Easily manage your tracking list via CSV or Excel
- **💾 Local Database**: SQLite database ensures data privacy and portability

## 📋 Prerequisites

- **Python 3.8+** installed on your system
- **Google Chrome** browser installed
- **ChromeDriver** (automatically managed or can be manually installed)
- **Internet connection** for price scraping

## 🚀 Quick Start

### 1. Clone or Download the Project
```bash
git clone <repository-url>
cd price_tracker_project
```
## 2. Install Dependencies
```bash
pip install -r requirements.txt
```
## 3. First Run
```bash
python main.py
```
## 📁 Project Structure
```text
price_tracker_project/
│
├── main.py                    # Main application entry point
├── setup_schedule.py          # Automatic scheduling setup
├── requirements.txt           # Python dependencies
├── README.md                  # This documentation
├── FUTURE_UPDATES.md          # Planned improvements
│
├── core/                      # Core application logic
│   ├── __init__.py
│   ├── database.py           # SQLite database operations
│   ├── validators.py         # Input validation functions
│   └── constants.py          # Categories and store lists
│
├── modules/                   # Feature modules
│   ├── __init__.py
│   ├── product_tracker.py    # Product management
│   ├── price_scraper.py      # Web scraping engine
│   └── price_alerts.py       # Price alert notifications
│
├── utils/                     # Utility functions
│   ├── __init__.py
│   ├── menu_utils.py         # Menu display and navigation
│   └── formatting.py         # Data formatting and display
│
└── data/                      # Data storage directory
    ├── database.sqlite       # SQLite database (created on first run)
    └── sites.json           # Store-specific scraping configurations
```
## 🎮 User Guide
Main Menu Options
## 1. 📋 Product Management
Add New Product: Start tracking a new product

View All Products: See all tracked products with status

Remove Product: Stop tracking a product

Edit Product: Update product details or target price

## 2. 🔍 Price Checking
Check All Prices: Scrape current prices for all tracked products

Check Specific Product: Get price for a single product by ID

View Price History: See historical prices for all products

View Product History: Detailed price history for specific product

## 3. 💾 Data Management
Export Data: Save your tracking list to CSV or Excel

Import Data: Load products from a CSV or Excel file

Adding Your First Product
Run the application:

```bash
python main.py
```
Select option 1 (Product Management)

Select option 1 (Add New Product)

Enter the product details:

Product Name: Name of the product

Product URL: Full URL to the product page

Store: Select from supported stores (Instant Gaming, Eneba, Ivory)

Target Price: Your desired purchase price

Category: Product category from the list

Supported Stores
Currently supported stores (configured in data/sites.json):

## ⚙️ Automatic Scheduling
Setting Up Automatic Price Checks
The application can be set to run automatically and check prices on a schedule:

```bash
python setup_schedule.py
```
Default Schedule:
Windows: Runs every Monday at 9:00 PM via Task Scheduler

Linux/macOS: Runs every Monday at 9:00 AM via cron job

Customizing the Schedule
Edit setup_schedule.py to change the schedule frequency:

python
## For Windows - Change from WEEKLY to DAILY
"/SC", "DAILY",

## For Linux/macOS - Change cron schedule
"0 9 * * *"  # Daily at 9 AM instead of weekly
Permissions Required:
Windows: Run as Administrator for Task Scheduler setup

Linux/macOS: Standard user permissions for cron jobs


<div align="center"> ✨ <strong>Happy Price Tracking!</strong> ✨ </div>
