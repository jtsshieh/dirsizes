import os
import sys

def find_sub_dirs(root_dir):
    builder = ""
    for directory in os.scandir(root_dir):
        if not directory.is_dir():
            continue
        total_size = 0
        for parent_dir, sub_dirs, filenames in os.walk(directory):
            for f in filenames:
                fp = os.path.join(parent_dir, f)
                if not os.path.islink(fp):
                    total_size += os.path.getsize(fp)
        builder += f"{directory.path} - {total_size} bytes\n"
    return builder


print(find_sub_dirs(sys.argv[0]))
