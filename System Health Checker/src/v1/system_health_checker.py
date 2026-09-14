import subprocess

def get_hostname()-> str:
    host=subprocess.run(["hostname"],capture_output=True,text=True,check=True)
    hostname=host.stdout.strip()
    return hostname

def get_cpu()->float:
    top_cmd=subprocess.Popen(["top","-bn1"],stdout=subprocess.PIPE,text=True)
    awk_cmd=subprocess.Popen(["awk", r"/Cpu\(s\)/ {print 100 - $8}"],stdin=top_cmd.stdout,stdout=subprocess.PIPE,text=True)
    top_cmd.stdout.close()
    cpu_usage,_=awk_cmd.communicate()
    return float(cpu_usage.strip())

def get_memory() -> float:
    mem=subprocess.run(["free","-m"],capture_output=True, text=True,check=True)
    mem_data=mem.stdout.splitlines()
    memory_values=mem_data[1].split()
    total_memory=float(memory_values[1])
    used_memory=float(memory_values[2])
    mem_usage=(used_memory/total_memory)*100
    return mem_usage

def get_disk()-> float:
    disk=subprocess.run(["df","-h","/","--output=pcent"],capture_output=True,text=True)
    disk_data=disk.stdout.splitlines()
    disk_usage=disk_data[1].strip()
    return float(disk_usage.replace("%",""))

def get_status(cpu:float,mem:float,disk:float) -> str:
    if((cpu < 75) and (disk < 75) and (mem < 75)):
        return "Healthy"
    return "Unhealthy"

def print_report(hostname:str,cpu:float,mem:float,disk:float,status:str) -> None:
    print("=" * 30)
    print("\n" "SYSTEM HEALTH CHECK")
    print("=" * 30)
    print("\n" "\n")
    print(f"Hostname : {hostname}")
    print(f"CPU Usage : {cpu:.2f}%")
    print(f"Memory Usage : {mem: .2f}%")
    print(f"Disk Usage : {disk: .2f}%")
    print("\n" "\n")
    print(f"Overall Status : {status}")
    print("\n" "\n")
    print("=" * 30)

def system_health() -> None:
    cpu=get_cpu()
    mem=get_memory()
    hostname=get_hostname()
    disk=get_disk()
    status=get_status(cpu,mem,disk)
    print_report(hostname,cpu,mem,disk,status)

if __name__ == "__main__":
    system_health()