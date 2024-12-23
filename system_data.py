import psutil


def get_cpu_info():
    cpu_usage = psutil.cpu_percent(interval=1)
    logical_cores = psutil.cpu_count(logical=True)
    physical_cores = psutil.cpu_count(logical=False)
    cpu_freq = psutil.cpu_freq()
    cpu_times = psutil.cpu_times()
    for name, value in locals().items():
        print(f"{name}: {value}")

    return locals()

def get_memory_info():
    virtual_memory = psutil.virtual_memory()
    total_memory = virtual_memory.total / (1024 ** 3)
    available_memory = virtual_memory.available / (1024 ** 3)
    used_memory = virtual_memory.used / (1024 ** 3)
    memory_usage = virtual_memory.percent
    swap_memory = psutil.swap_memory()
    total_swap = swap_memory.total / (1024 ** 3)
    used_swap = swap_memory.used / (1024 ** 3)
    free_swap = swap_memory.free / (1024 ** 3)
    swap_usage = swap_memory.percent
    for name, value in locals().items():
        print(f"{name}: {value}")

    return locals()

def get_disk_info():
    disk_usage = psutil.disk_usage('/')
    total_disk = disk_usage.total / (1024 ** 3)
    used_disk = disk_usage.used / (1024 ** 3)
    free_disk = disk_usage.free / (1024 ** 3)
    percent_used = disk_usage.percent
    for name, value in locals().items():
        print(f"{name}: {value}")

    return locals()

