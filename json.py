import os
import datetime

def write_file_info(dir_path, file_path):
    with open(file_path, 'w+') as f:
        for filename in os.listdir(dir_path):
            file_path = os.path.join(dir_path, filename)
            file_info = os.stat(file_path)
            file_size = file_info.st_size
            file_extension = os.path.splitext(filename)[1]
            file_created = datetime.datetime.fromtimestamp(file_info.st_ctime)
            f.write(f"File: {filename}, Extension: {file_extension}, Size: {file_size} bytes, Created: {file_created}\n")
write_file_info(dir_path, file_path)
