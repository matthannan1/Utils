import os
from tkinter import filedialog, Tk


def which_directory():
    """This function provides an easy GUI for the user to select the
        working directory of the files.
    """
    # Ask for the directory to get the files from
    root = Tk().withdraw() # .withdraw() hides that second blank window
    # This sets to the users home directory
    init_dir = os.path.expanduser('~')
    # These options in .askdirectory seem to get the job done!
    filedirectory = filedialog.askdirectory(initialdir=init_dir,
                                            title='Please select a directory')
    return filedirectory

def renameSubfolders(basedir):
    for fn in os.listdir(basedir):
        if not os.path.isdir(os.path.join(basedir, fn)):
            continue # Not a directory
        if fn[0] == '0' or fn[0] == '1':
            new1fn = fn.replace(" ", "")
            new2fn = new1fn.split('-')
            new3fn = new2fn[0]
            if len(new2fn) > 1:
                new4fn = new3fn[4]+new3fn[5]+new3fn[6]+new3fn[7]+new3fn[0]+new3fn[1]+new3fn[2]+new3fn[3]+'-'+new2fn[1]
            else:
                new4fn = new3fn[4]+new3fn[5]+new3fn[6]+new3fn[7]+new3fn[0]+new3fn[1]+new3fn[2]+new3fn[3]

            os.rename(os.path.join(basedir, fn), os.path.join(basedir, new4fn))


renameSubfolders(which_directory())
