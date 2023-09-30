import psutil,time,os
def get_system_info():
    # Get CPU usage
    cpu_usage = psutil.cpu_percent(interval=1)
    # Get memory usage
    memory = psutil.virtual_memory()
    memory_usage = memory.percent
    # Get disk space
    disk = psutil.disk_usage('/')
    total_disk_space = disk.total
    used_disk_space = disk.used
    disk_space_percentage = disk.percent
    print(f"Single Core CPU Usage: {cpu_usage}%")
    print(f"Memory Usage: {memory_usage}%")
    print(f"Local Disk C Space Used: {used_disk_space / (1024 ** 3):.2f} GB")
    print(f"Total Disk Space: {total_disk_space / (1024 ** 3):.2f} GB")
    print(f"Disk Space Percentage: {disk_space_percentage}%")
get_system_info()

    



    
    

    
 
    





