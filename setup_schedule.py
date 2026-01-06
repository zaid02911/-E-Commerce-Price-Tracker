import os
import platform
import subprocess
from pathlib import Path

def schedule_script():
    """Schedule the price tracker to run automatically."""
    script_path = Path("main.py").resolve()
    system_os = platform.system()

    print("📅 Setting up automatic scheduling...")
    print("=" * 40)

    if system_os == "Windows":
        task_name = "WeeklyPriceAlert"
        print(f"🪟 Creating Windows Task Scheduler job: '{task_name}'")
        print("⏰ Schedule: Every Monday at 9:00 PM")
        print("🔐 Run with: Highest privileges")
        
        try:
            subprocess.run([
                "schtasks", "/Create",
                "/SC", "WEEKLY",
                "/D", "MON",
                "/TN", task_name,
                "/TR", f'python "{script_path}" auto',
                "/RL", "HIGHEST",
                "/F"
            ], check=True)
            print("✅ Successfully scheduled weekly task in Windows Task Scheduler!")
        except subprocess.CalledProcessError as e:
            print("❌ Failed to create scheduled task. Please run as administrator.")
            print(f"   Error: {e}")

    elif system_os in ["Linux", "Darwin"]:
        cron_job = f"0 9 * * 1 python3 {script_path} auto  # Price Tracker - Every Monday at 9:00 AM\n"
        print(f"🐧 Setting up cron job on {system_os}")
        print("⏰ Schedule: Every Monday at 9:00 AM")
        
        try:
            # Check if crontab exists
            cron_exists = subprocess.run(
                "crontab -l", 
                shell=True, 
                capture_output=True, 
                text=True
            )
            
            if str(script_path) not in cron_exists.stdout:
                new_cron = cron_exists.stdout + cron_job if cron_exists.returncode == 0 else cron_job
                subprocess.run(f'echo "{new_cron}" | crontab -', shell=True, check=True)
                print("✅ Successfully scheduled weekly cron job!")
            else:
                print("⚠️  Cron job already exists. Skipping...")
                
        except subprocess.CalledProcessError as e:
            print("❌ Failed to set up cron job.")
            print(f"   Error: {e}")
    else:
        print(f"❌ Unsupported operating system: {system_os}")
        print("   Automatic scheduling is only available for Windows, Linux, and macOS.")

schedule_script()

