import gzip
import os
import glob


if __name__ == '__main__':
    os.chdir(r'C:/Users/u0149275/OneDrive - KU Leuven/Demography/Datasets/EDGe/EDGe_Syntactic_Deletion')
    my_files = glob.glob('*.txt')
    path = r'C:/Users/u0149275/OneDrive - KU Leuven/Demography/Datasets/EDGe/EDGe_Syntactic_Deletion_Zipped/'
    for my_file in my_files:
        with open(my_file, 'rb') as f_in, gzip.open(path + my_file + '.gz', 'wb') as f_out:
            f_out.writelines(f_in)
