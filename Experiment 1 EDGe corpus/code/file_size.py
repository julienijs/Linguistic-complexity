import os
import glob
import pandas


def check_size(file):
    file_stats = os.stat(file)
    file_size = file_stats.st_size
    return file_size


def get_language(file):
    file_language = file[0:2]
    if file_language == 'nl':
        return 'Dutch'
    elif file_language == 'en':
        return 'English'
    elif file_language == 'de':
        return 'German'
    else:
        return 'XXX'


def get_year(file):
    file_year = file[3:7]
    return file_year


if __name__ == '__main__':
    my_dict = {'filename': [], 'language': [], 'year': [], 'size': []}
    os.chdir(r'C:/Users/u0149275/OneDrive - KU Leuven/Demography/Datasets/EDGe/EDGe_Syntactic_Deletion_Zipped')
    my_files = glob.glob('*.gz')
    for my_file in my_files:
        size = check_size(my_file)
        language = get_language(my_file)
        year = get_year(my_file)
        my_dict["filename"].append(my_file)
        my_dict["language"].append(language)
        my_dict["year"].append(int(year))
        my_dict["size"].append(size)
    data = pandas.DataFrame.from_dict(my_dict)
    print(data)
    data.to_excel('EDGe_Syntactic_Deletion_Zipped_Sizes.xlsx')
