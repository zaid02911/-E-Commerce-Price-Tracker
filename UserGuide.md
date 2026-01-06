# 🛒 E-Commerce Price Tracker

<div align="center">

![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Status](https://img.shields.io/badge/status-active-success.svg)

**Track prices • Set alerts • Save money**

A powerful, automated price tracking system that monitors product prices across multiple online stores and sends desktop alerts when prices drop below your target.

</div>

## 🎮 User Guide

### Main Menu Options

#### 1. 📋 Product Management
- **Add New Product**: Start tracking a new product
- **View All Products**: See all tracked products with status
- **Remove Product**: Stop tracking a product
- **Edit Product**: Update product details or target price

#### 2. 🔍 Price Checking
- **Check All Prices**: Scrape current prices for all tracked products
- **Check Specific Product**: Get price for a single product by ID
- **View Price History**: See historical prices for all products
- **View Product History**: Detailed price history for specific product

#### 3. 💾 Data Management
- **Export Data**: Save your tracking list to CSV or Excel
- **Import Data**: Load products from a CSV or Excel file

### Adding Your First Product

1. **Run the application:**
   ```bash
   python main.py
Select option 1 (Product Management)

Select option 1 (Add New Product)

Enter the product details:

Product Name: Name of the product

Product URL: Full URL to the product page

Store: Select from supported stores (Instant Gaming, Eneba, Ivory)

Target Price: Your desired purchase price

Category: Product category from the list

⚙️ Automatic Scheduling
Setting Up Automatic Price Checks
The application can be set to run automatically and check prices on a schedule:

bash
python setup_schedule.py
Default Schedule:
Platform	Schedule	Time
Windows	Every Monday	9:00 PM via Task Scheduler
Linux/macOS	Every Monday	9:00 AM via cron job
Customizing the Schedule
Edit setup_schedule.py to change the schedule frequency:

python
# For Windows - Change from WEEKLY to DAILY
"/SC", "DAILY",

# For Linux/macOS - Change cron schedule
"0 9 * * *"  # Daily at 9 AM instead of weekly
Permissions Required:
Platform	Permissions
Windows	Run as Administrator for Task Scheduler setup
Linux/macOS	Standard user permissions for cron jobs
<div align="center"> ✨ <strong>Happy Price Tracking!</strong> ✨ </div> 
