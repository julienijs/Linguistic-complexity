import glob
import os
import math
import random
import gzip
import pandas


def delete_verses(f, n):
    for _ in range(n):
        index = random.randint(0, len(f)-1)
        f = f[:index] + f[index + 1:]
    return f


def check_size(file):
    file_stats = os.stat(file)
    file_size = file_stats.st_size
    return file_size


if __name__ == '__main__':
    os.chdir(r'C:/Users/EDGe')
    my_files = glob.glob('*.txt') # insert own directory
    path = r'C:/Users/EDGe/EDGe_Workspace/' # insert own directory
    all_zipped = []
    all_unzipped = []
    for my_file in my_files:
        # open and read the file
        text = open(my_file, "r")
        text = text.readlines()
        # get the total number of characters of the file
        number = len(text)
        # calculate 10 percent of the total number of characters
        number_to_delete = math.ceil((number / 100) * 10)
        # make list
        zipped = [my_file]
        unzipped = [my_file]
        # get the file name
        name = os.path.splitext(my_file)
        # do 1000 times
        for x in range(1000):
            # randomly delete 10 percent of the characters of the file
            new_text = delete_verses(text, number_to_delete)
            # write the distorted text to a new file
            with open(path + name[0] + '_deletion.txt', 'w') as new_file:
                new_file.writelines(new_text)
            # get the file size of the distorted file
            distorted_file_size = check_size(path + name[0] + '_deletion.txt')
            # add the file size of the distorted file to unzipped list
            unzipped.append(distorted_file_size)
            # gzip the distorted file
            with open(path + name[0] + '_deletion.txt', 'rb') as in_f, gzip.open(
                    path + name[0] + '_deletion.txt' + '.gz', 'w') as out_f:
                out_f.writelines(in_f)
            # get file size zipped and distorted file
            zipped_distorted_file_size = check_size(path + name[0] + '_deletion.txt.gz')
            # add the file size of the distorted zipped file to zipped list
            zipped.append(zipped_distorted_file_size)
        # add unzipped to all_unzipped
        all_unzipped.append(unzipped)
        # add zipped to all_unzipped
        all_zipped.append(zipped)
    df_unzipped = pandas.DataFrame(all_unzipped)
    df_zipped = pandas.DataFrame(all_zipped)
    df_zipped.to_excel('pragmatic_zipped.xlsx')
    df_unzipped.to_excel('pragmatic_unzipped.xlsx')
