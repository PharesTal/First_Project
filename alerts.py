from system_data import get_cpu_info , get_disk_info ,  get_memory_info


import time


THRESHOLDS = {
    "cpu_usage": 80,
    "memory_usage": 75,
    "disk_usage": 80,
}

def check_thresholds():
    alerts = []

    cpu_info = get_cpu_info()
    memory_info = get_memory_info()
    disk_info = get_disk_info()

    if cpu_info["cpu_usage"] > THRESHOLDS["cpu_usage"]:
        alerts.append(f"CPU usage is high: {cpu_info['cpu_usage']}% (threshold: {THRESHOLDS['cpu_usage']}%)")

    if memory_info["memory_usage"] > THRESHOLDS["memory_usage"]:
        alerts.append(f"Memory usage is high: {memory_info['memory_usage']}% (threshold: {THRESHOLDS['memory_usage']}%)")

    if disk_info["disk_usage"] > THRESHOLDS["disk_usage"]:
        alerts.append(f"Disk usage is high: {disk_info['disk_usage']}% (threshold: {THRESHOLDS['disk_usage']}%)")

    return alerts

def send_alerts(alerts):
    for alert in alerts:
        print(f"ALERT: {alert}")

def monitor_system(interval=10):
    print("Starting system monitor...")
    while True:
        alerts = check_thresholds()
        if alerts:
            send_alerts(alerts)
        else:
            print("System is stable.")
        time.sleep(interval)

monitor_system(interval=15)  # בדיקה כל 15 שניות
