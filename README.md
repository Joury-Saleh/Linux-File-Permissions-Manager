# Linux-File-Permissions-Manager

This project explains and implements how to **understand and set Linux file permissions** using Python. It also includes a **flowchart image** to visually guide the chmod process.


## What it Does

- Explains Linux file permission structure (symbolic and numeric)
- Converts symbolic format like `rwxrwxr-x` into numeric `775`
- Uses Python to apply permissions using `os.chmod()`
- Visualizes the workflow using a flowchart

## Flowchart Included

![photo]

📌 The included image `permissions_flowchart.png` visually explains:
- When and why to change permissions
- How to convert symbolic to numeric
- What `chmod` command to use

## Python Script Example

```python
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
```

## Permission Breakdown

| Entity    | Permission | Numeric |
| --------- | ---------- | ------- |
| Owner     | rwx        | 7       |
| Group     | rwx        | 7       |
| Others    | r-x        | 5       |
| **Total** | rwxrwxr-x  | **775** |


##  How to Use

1. Update the file_path in the script.

2. Run the script: `python3 permission_changer.py `

3. Confirm the result: `ls -l your_file.py`

نسخ
تحرير


