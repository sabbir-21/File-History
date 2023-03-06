import shutil
import os
import time

user = os.getenv("UserName")
src_dirs = [f"C:\\Users\\{user}\\Desktop", f"C:\\Users\\{user}\\Downloads"]
dest_dir = r"D:\FileHistory"
os.makedirs(dest_dir, exist_ok=True)
timetosleep=420
while True:
    for src_dir in src_dirs:
        dest_subdir = os.path.join(dest_dir, os.path.basename(src_dir))
        
        os.makedirs(dest_subdir, exist_ok=True)
            
        for file_name in os.listdir(src_dir):
            src_file_path = os.path.join(src_dir, file_name)
            dest_file_path = os.path.join(dest_subdir, file_name)
            
            if not os.path.exists(dest_file_path):
                shutil.copy2(src_file_path, dest_subdir)
                print(f"Copied {file_name}")
        
    time.sleep(timetosleep)