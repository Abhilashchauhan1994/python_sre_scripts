import psutil
import socket

def get_hostname()-> str:
    return socket.gethostname()

def get_cpu_usage()->float:
    cpu_usage=psutil.cpu_percent()
    return float(cpu_usage)

def get_mem_usage()->float:
    mem=psutil.virtual_memory()
    return float(mem.percent)

def get_disk_usage()->float:
    disk_usage=psutil.disk_usage("/")
    return float(disk_usage.percent)

def get_status(cpu:float,mem:float,disk:float) -> str:
    if((cpu < 75) and (disk < 75) and (mem < 75)):
        return "Healthy"
    return "Unhealthy"

def print_report(hostname:str,cpu:float,mem:float,disk:float,status:str) -> None:
    print("=" * 30)
    print("SYSTEM HEALTH CHECK")
    print("=" * 30)
    print("\n")
    print(f"Hostname : {hostname}")
    print(f"CPU Usage : {cpu:.2f}%")
    print(f"Memory Usage : {mem: .2f}%")
    print(f"Disk Usage : {disk: .2f}%")
    print("\n")
    print(f"Overall Status : {status}")
    print("\n" "\n")
    print("=" * 30)

def system_health() -> None:
    cpu=get_cpu_usage()
    mem=get_mem_usage()
    hostname=get_hostname()
    disk=get_disk_usage()
    status=get_status(cpu,mem,disk)
    print_report(hostname,cpu,mem,disk,status)

if __name__ == "__main__":
    system_health()