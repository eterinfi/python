# Filename: backup_ver2.py

import os
import time

# 1. The files and directories to be backed up are specified in a list.
source = [r'C:\Users\Rui\Work', r'D:\Doc']

# 2. The backup must be stored in a main backup directory.
target_dir = r'C:\Users\Rui\Backup'

# 3. The files are backed up into a 7z file.
# 4. The current day is the name of the subdirectory in the main directory
today = target_dir + os.sep + time.strftime('%Y%m%d')

#    The current time is the name of the zip archive
now = time.strftime('%H%M%S')

#    Create the subdirectories if they ain't already there
if not os.path.exists(target_dir):
    os.mkdir(target_dir) # make target_dir
    print 'Successfully created directory', target_dir
if not os.path.exists(today):
    os.mkdir(today) # make today directory
    print 'Successfully created directory', today

#    The name of the zip file
target = today + os.sep + now + '.7z'

# 5. We use the 7z command to put the files in a 7z archive
zip_command = r'C:\Progra~1\7-Zip' + os.sep + '7z a %s %s' % (target,' '.join(source)) + '>null'

# Run the backup
if os.system(zip_command) == 0:
    print 'Successful backup to', target
else:
    print 'Backup FAILED'