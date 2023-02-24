# File History Backup
 ## Windows file history clone in python

This Python script is designed to automatically backup the contents of the Desktop and Downloads folders in the user directory to a specified destination directory. The script utilizes the shutil and os modules to copy the files from the source directories to the destination directory, while checking for duplicates to prevent overwriting. The script runs continuously in a loop, checking for new files to copy every ***x*** seconds.

 > Windows File History is a useful feature for backing up personal files and folders, but it is not a complete backup solution. Users should still consider creating full system images and using additional backup tools for complete data protection.
 

**Disadvantages of windows FileHistory** While Windows File History provides a simple and automated way to back up files, it has some limitations and disadvantages:

 - It only backs up user files and folders, not system files or applications.

 - It does not create a full system image, so it cannot be used to restore an entire system.

 - It requires an external drive or network location to store backups, which can be a security risk if the drive is lost or stolen.

 - It can take up a significant amount of disk space, especially if backups are kept indefinitely.

 - It is not available on Windows 7 or earlier versions of Windows.


## Requirements

`Python 3.x`
`shutil module`
`os module`

## How to Use
Download the script and save it to a location of your choice.
Open the script in a Python editor or IDE.
Modify the `src_dirs` and `dest_dir` variables to reflect your desired source and destination directories.
Save the script and run it in your Python environment.
The script will continuously monitor the source directories for new files and copy them to the destination directory.

## Modification
You can make an executable file and save it in `C:\Users\~\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup` for auto start.
*Pyinstaller* command
```
pip install pyinstaller
pyinstaller -F -w -i icon.ico main.py
```
Use an icon file in working directory before running pyinstaller

*** Any logical pull request is accepted and much more appreciated ***
