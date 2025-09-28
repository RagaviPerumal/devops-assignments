import psutil
import logging
from datetime import datetime
CPU_THRESHOLD = 80.0  
MEMORY_THRESHOLD = 80.0 
DISK_THRESHOLD = 90.0  

LOG_FILE = 'system_health.log'
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def log_and_print(message, level=logging.INFO):
    """Prints a message to the console and logs it to the file."""
    print(message)
    if level == logging.INFO:
        logging.info(message)
    elif level == logging.WARNING:
        logging.warning(message)
    elif level == logging.ERROR:
        logging.error(message)

def check_cpu_usage():
    """Checks the current CPU usage and alerts if it exceeds the threshold."""
    cpu_percent = psutil.cpu_percent(interval=1)
    if cpu_percent > CPU_THRESHOLD:
        alert_message = f"ALERT: High CPU usage detected: {cpu_percent}%"
        log_and_print(alert_message, logging.WARNING)
    else:
        log_and_print(f"INFO: CPU usage is normal: {cpu_percent}%")

def check_memory_usage():
    """Checks the current memory usage and alerts if it exceeds the threshold."""
    memory_info = psutil.virtual_memory()
    memory_percent = memory_info.percent
    if memory_percent > MEMORY_THRESHOLD:
        alert_message = f"ALERT: High Memory usage detected: {memory_percent}%"
        log_and_print(alert_message, logging.WARNING)
    else:
        log_and_print(f"INFO: Memory usage is normal: {memory_percent}%")

def check_disk_space():
    """Checks the disk space for all partitions and alerts if any exceed the threshold."""
    partitions = psutil.disk_partitions()
    for partition in partitions:
        try:
            usage = psutil.disk_usage(partition.mountpoint)
            disk_percent = usage.percent
            if disk_percent > DISK_THRESHOLD:
                alert_message = f"ALERT: Low disk space on {partition.mountpoint}: {disk_percent}% used"
                log_and_print(alert_message, logging.WARNING)
            else:
                log_and_print(f"INFO: Disk space on {partition.mountpoint} is normal: {disk_percent}% used")
        except PermissionError:
            log_and_print(f"WARN: Could not access disk stats for {partition.mountpoint}. Skipping.", logging.WARNING)


def check_running_processes():
    """Provides a count of the total number of running processes."""
    process_count = len(psutil.pids())
    log_and_print(f"INFO: Total number of running processes: {process_count}")

def main():
    """Main function to run all the health checks."""
    log_and_print("--- Starting System Health Check ---")
    check_cpu_usage()
    check_memory_usage()
    check_disk_space()
    check_running_processes()
    log_and_print("--- System Health Check Complete ---")

if __name__ == "__main__":
    main()
