# This script contains the whole pipeline for morphologically distorting all files in a directory, 
# zipping them and writing all the zipped file sizes to an excel file
# Morphological distortion means that random 10% of the characters in a file will be deleted

import glob
import os
import math
import random
import gzip
import pandas


# returns the number of characters in a file
def count_characters(file):
    data = file.replace(" ", "")
    number_of_characters = len(data)
    return number_of_characters


# calculates 10% of a given number
def calculate_10_percent(num):
    return math.ceil((num / 100) * 10)


# deletes random characters and returns the text
def delete_characters(file, n):
    for _ in range(n):
        index = random.randint(0, len(file) - 1)
        while file[index].isspace():
            index = index - 1
        file = file[:index] + file[index + 1:]
    return file


# returns the size of the file
def check_size(file):
    file_stats = os.stat(file)
    file_size = file_stats.st_size
    return file_size


if __name__ == '__main__':
    os.chdir(r'C:/Users/EDGe') # insert directory with the files
    my_files = glob.glob('*.txt')
    path = r'C:/Users/EDGe/Zipped' # insert new directory to write the distorted files to
    all_zipped = []
    for my_file in my_files:
        # open and read the file
        text = open(my_file, "r")
        text = text.read()
        # get the total number of characters of the file
        number = count_characters(text)
        # calculate 10 percent of the total number of characters
        number_to_delete = calculate_10_percent(number)
        # do 1000 times
        zipped = [my_file]
        # get the file name
        name = os.path.splitext(my_file)
        for x in range(1000):
            # randomly delete 10 percent of the characters of the file
            new_text = delete_characters(text, number_to_delete)
            # write the distorted text to a new file in the new directory defined in path
            with open(path + name[0] + '_deletion.txt', 'w') as new_file:
                new_file.write(new_text)
            # gzip the distorted file
            with open(path + name[0] + '_deletion.txt', 'rb') as in_f, gzip.open(
                    path + name[0] + '_deletion.txt' + '.gz', 'w') as out_f:
                out_f.writelines(in_f)
            # get file size zipped and distorted file
            zipped_distorted_file_size = check_size('path + name[0] + '_deletion.txt.gz')
            # add the file size of the distorted zipped file to zipped list
            zipped.append(zipped_distorted_file_size)
        # add zipped to all_unzipped
        all_zipped.append(zipped)
    df_zipped = pandas.DataFrame(all_zipped)
    df_zipped.to_excel('morph_zipped_all.xlsx')
