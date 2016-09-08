# Filename: backup_ver1.py

import os
import time

# 1. The files and directories to be backed up are specified in a list.
source = [r'C:\Users\Rui\Work', r'D:\Doc']

# 2. The backup must be stored in a main backup directory.
target_dir = 'C:\\Users\\Rui\\Backup\\'

# 3. The files are backed up into a 7z file.
# 4. The name of the 7z archive is the current date and time
target = target_dir + time.strftime('%Y%m%d%H%M%S') + '.7z'

# 5. We use the 7z command to put the files in a 7z archive
zip_command = 'C:\\Progra~1\\7-Zip\\' + '7z a %s %s' % (target,' '.join(source)) + '>null'

# Run the backup
if os.system(zip_command) == 0:
    print 'Successful backup to', target
else:
    print 'Backup FAILED'