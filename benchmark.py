import time
import psutil

def cpu_benchmark():
    print("Starting CPU benchmark...")
    cpu_info = get_cpu_info()
    print("CPU Info:")
    for key, value in cpu_info.items():
        print(f"{key}: {value}")
    print("\n")
    start_time = time.time()
    prime_num = 999999
    count = 0
    while True:
        is_prime = True
        for i in range(2, prime_num):
            if prime_num % i == 0:
                is_prime = False
                break
        if is_prime:
            count += 1
            if count == 100:
                break
        prime_num += 1
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"CPU benchmark completed in {elapsed_time:.2f} seconds.\n")

def ram_benchmark():
    print("Starting RAM benchmark...")
    print("\nRAM Info:")
    ram_info = get_ram_info()
    for key, value in ram_info.items():
        print(f"{key}: {value}")
    print("\n")
    start_time = time.time()
    data = []
    for _ in range(1000000):
        data.append('x' * 1024)
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"RAM benchmark completed in {elapsed_time:.2f} seconds.\n")

def get_cpu_info():
    cpu_info = {}
    cpu_info['Physical cores'] = psutil.cpu_count(logical=False)
    cpu_info['Total cores'] = psutil.cpu_count(logical=True)
    cpu_info['Max frequency'] = f"{psutil.cpu_freq().max:.2f}Mhz"
    cpu_info['Min frequency'] = f"{psutil.cpu_freq().min:.2f}Mhz"
    cpu_info['Current frequency'] = f"{psutil.cpu_freq().current:.2f}Mhz"
    cpu_info['CPU Usage Per Core'] = psutil.cpu_percent(percpu=True)
    cpu_info['Total CPU Usage'] = psutil.cpu_percent()
    return cpu_info

def get_ram_info():
    ram = psutil.virtual_memory()
    ram_info = {}
    ram_info['Total'] = f"{ram.total / (1024**3):.2f} GB"
    ram_info['Available'] = f"{ram.available / (1024**3):.2f} GB"
    ram_info['Used'] = f"{ram.used / (1024**3):.2f} GB"
    ram_info['Percentage'] = f"{ram.percent}%"
    return ram_info
if __name__ == "__main__":
    cpu_benchmark()
    ram_benchmark()