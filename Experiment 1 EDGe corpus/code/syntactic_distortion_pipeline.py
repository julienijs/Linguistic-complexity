# This script contains the whole pipeline for syntactically distorting all files in a directory, 
# zipping them and writing all the zipped file sizes to an excel file
# Syntactic distortion means that random 10% of the words in a file will be deleted

import glob
import os
import random
import gzip
import pandas
import re


# split text into tokens
def tokenize(s: str) -> list[str]:
    return s.split()


# randomly deletes 10% of the words in a file
def delete_pct_words(s: str, pct: float = 0.1) -> str:
    word_patt = r"\b([\w'-]+)\b"
    matched_tokens: list[re.Match] = list(re.finditer(word_patt, s))
    tokens_count: int = len(matched_tokens)
    pct_is_k: int = int(tokens_count * pct)
    matches_to_replace: list[re.Match] = random.sample(matched_tokens, k=pct_is_k)
    matches_to_replace.sort(key=lambda x: x.end(), reverse=True)
    for match in matches_to_replace:
        s = s[:match.start(1)] + s[match.end(1):]
    return s


# returns the file size
def check_size(file):
    file_stats = os.stat(file)
    file_size = file_stats.st_size
    return file_size


if __name__ == '__main__':
    os.chdir(r'C:/Users/EDGe') # insert directory with the files
    my_files = glob.glob('nl*.txt')
    path = r'C:/Users/EDGe/Zipped' # insert directory to write the distorted files to
    all_zipped = []
    # iterate over the files
    for my_file in my_files:
        # get size of original file
        original_file_size = check_size(my_file)
        # gzip the original file
        with open(my_file, 'rb') as f_in, gzip.open(path + my_file + '.gz', 'w') as f_out:
            f_out.writelines(f_in)
        # get the file size of the zipped file
        zipped_file_size = check_size(path + my_file + '.gz')
        # open and read the file
        text = open(my_file, "r")
        text = text.read()
        # do 1000 times
        zipped = [my_file]
        for x in range(1000):
            # randomly delete 10 percent of the characters of the file
            new_text = delete_pct_words(text, 0.1)
            # get the file name
            name = os.path.splitext(my_file)
            # write the distorted text to a new file
            with open(path + name[0] + '_deletion.txt', 'w') as new_file:
                new_file.write(new_text)
            # gzip the distorted file
            with open(path + name[0] + '_deletion.txt', 'rb') as in_f, gzip.open(
                    path + name[0] + '_deletion.txt' + '.gz', 'w') as out_f:
                out_f.writelines(in_f)
            # get file size zipped and distorted file
            zipped_distorted_file_size = check_size(path + name[0] + '_deletion.txt.gz')
            # add the file size of the distorted zipped file to zipped list
            zipped.append(zipped_distorted_file_size)
        # add zipped to all_unzipped
        all_zipped.append(zipped)
    df_zipped = pandas.DataFrame(all_zipped)
    df_zipped.to_excel('synt_zipped_all.xlsx')
