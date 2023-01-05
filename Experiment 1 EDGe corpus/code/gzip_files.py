# Python code for zipping all files in a directory and writing them to a new directory, using gzip

import gzip
import os
import glob


if __name__ == '__main__':
    os.chdir(r'C:/Users/EDGe') # insert directory that contains the files
    my_files = glob.glob('*.txt')
    path = r'C:/Users/EDGe/Zipped/' # insert directory to send the zipped files to
    # iterate over files and gzip them
    for my_file in my_files:
        with open(my_file, 'rb') as f_in, gzip.open(path + my_file + '.gz', 'wb') as f_out:
            f_out.writelines(f_in)
