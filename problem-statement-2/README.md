# Problem Statement 2: Monitoring Scripts

This folder contains two Python scripts for monitoring system and application health.

## 1. System Health Monitor

This script monitors CPU, memory, and disk usage.

### How to Run
1. **Navigate to the script directory:**
   `cd system-health-monitor`
2. **Install dependencies:**
   `pip install psutil`
3. **Run the script:**
   `python system_health_monitor.py`

## 2. Application Health Checker

This script checks the status of any given URL.

### How to Run
1. **Navigate to the script directory:**
   `cd application-health-checker`
2. **Create and activate a virtual environment (Recommended).**
3. **Install dependencies:**
   `pip install requests`
4. **Run the script:**
   `python app_health_checker.py <URL_to_check>`
   Example: `python app_health_checker.py https://www.google.com`