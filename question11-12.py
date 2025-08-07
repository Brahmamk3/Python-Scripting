import os
import shutil
#Q11.print filename and last modified time
import os
from datetime import datetime

# Q12: Print filename and last modified time
for file in os.listdir(os.getcwd()):
    if os.path.isfile(file):
        mtime = os.path.getmtime(file)  # Last modified time in seconds
        formatted_time = datetime.fromtimestamp(mtime).strftime("%Y-%m-%d %H:%M:%S")
        print(f"{file} - Last Modified: {formatted_time}")



# Q12. print total, used, free disk space of current disk in GB
total, used, free = shutil.disk_usage(os.getcwd())

# Convert bytes to GB
gb_divisor = 1024 ** 3
print(f"Total: {total / gb_divisor:.2f} GB")
print(f"Used: {used / gb_divisor:.2f} GB")
print(f"Free: {free / gb_divisor:.2f} GB")

