import os
import stat

# Your target file
file_path = 'your_file.py'

# Permissions: rwxrwxr-x (775)
permissions = stat.S_IRUSR | stat.S_IWUSR | stat.S_IXUSR | \
              stat.S_IRGRP | stat.S_IWGRP | stat.S_IXGRP | \
              stat.S_IROTH | stat.S_IXOTH

os.chmod(file_path, permissions)
print(f"Permissions for {file_path} set to rwxrwxr-x (775)")