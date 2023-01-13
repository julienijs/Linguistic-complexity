# This script calculates all file sizes in a directory

import os
import glob
import pandas


# definition that returns the file size
def check_size(file):
    file_stats = os.stat(file)
    file_size = file_stats.st_size
    return file_size


# definition that returns the language based on the first 2 characters of the filename
def get_language(file):
    file_language = file[0:2]
    if file_language == 'nl':
        return 'Dutch'
    elif file_language == 'en':
        return 'English'
    elif file_language == 'de':
        return 'German'
    else:
        return none


# definition that returns the year based on the filename
def get_year(file):
    file_year = file[3:7]
    return file_year


if __name__ == '__main__':
    my_dict = {'filename': [], 'language': [], 'year': [], 'size': []} # make empty dict
    os.chdir(r'C:/Users/EDGe') # insert directory that contains the files
    my_files = glob.glob('*.gz')
    # iterate over the files
    for my_file in my_files:
        size = check_size(my_file) # check the size
        language = get_language(my_file) # get the language
        year = get_year(my_file) # get the year
        my_dict["filename"].append(my_file) # append filename to dict
        my_dict["language"].append(language) # append language to dict
        my_dict["year"].append(int(year)) # append year to dict
        my_dict["size"].append(size) # append size to dict
    data = pandas.DataFrame.from_dict(my_dict)
    data.to_excel('File_Sizes.xlsx')
