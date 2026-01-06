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
