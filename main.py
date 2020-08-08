import os
import sys

def find_sub_dirs(root_dir):
    builder = ""
    for directory in os.listdir(root_dir):
        if os.path.isdir(directory):
            continue
        total_size = 0
        for parent_dir, sub_dirs, filenames in os.walk(directory):
            for f in filenames:
                fp = os.path.join(parent_dir, f)
                if not os.path.islink(fp):
                    total_size += os.path.getsize(fp)
        builder += directory + " - " + str(total_size) + " bytes\n"
    return builder


print(find_sub_dirs(sys.argv[1]))
