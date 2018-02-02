#! python3
"""
    This script will move my uploaded iPhone photos and videos
    to more permanent housing, sorted by year and two-digit month.

    The two source directories are
    C:\\Users\\matth\\Dropbox\\Camera Uploads
    and 
    C:\\Users\\matth\\Dropbox\\Camera Uploads from Jenny

    NOTE:
    Username is a variable based on machine, but the Dropbox stuff is static.
    Spaces could be an issue, but I am sure we can work around it.

    Target directory for photos (.jpg, .png) is
    C:\\Users\\matth\\Dropbox\\Photos\\{year}\\{month in two digits}
    This will more than likely need to be created, but no biggie.

    Target directory for videos is 
    C:\\Users\\matth\\Dropbox\\Home Movies\\{year}\\{month in two digits}

"""

import shutil, os
from datetime import date

def dir_make(target):
    if os.path.exists(target):
        print(target,"already exists.")
    else:
        os.makedirs(target)
        print(target,"created.")

def move_files(source):
    os.chdir(source)
    for filename in os.listdir():
        if filename.endswith('.jpg') or filename.endswith('.png'):
            shutil.move(filename, photo_target_dir)
        if filename.endswith('.mov'):
            shutil.move(filename, video_target_dir)


# Get date and format into useable variables year and month
d = date.today()
year = str(d.year)
# loop this to check for l or t
answer = input(r,"Move (l)ast month's pictures or (t)his month's? ")
if answer == 'l':
    month = '%02d' % d.month - 1
else:
    month = '%02d' % d.month    

# Check target locations and see if the folders exist
photo_target_dir = os.path.join('C:\\Users\\matth\\Dropbox\\Photos', year, month)
video_target_dir = os.path.join('C:\\Users\\matth\\Dropbox\\Home Movies', year, month)
dir_make(photo_target_dir)
dir_make(video_target_dir)

# Move the source photos
source_dir1 = os.path.join('C:\\Users\\matth\\Dropbox\\Camera Uploads')
source_dir2 = os.path.join('C:\\Users\\matth\\Dropbox\\Camera Uploads from Jenny')
move_files(source_dir1)
move_files(source_dir2)














