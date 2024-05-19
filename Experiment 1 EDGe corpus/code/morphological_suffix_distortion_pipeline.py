import glob
import os
import math
import random
import gzip
import pandas


def count_characters(file):
    data = file.replace(" ", "")
    number_of_characters = len(data)
    return number_of_characters


def calculate_10_percent(num):
    return math.ceil((num / 100) * 10)


def delete_word_endings(text):
    words = text.split()

    # Select a random word if there are words in the text
    if words:
        # Select a random word
        random_word = random.choice(words)

        # Check if the word is at least 3 characters long
        if len(random_word) >= 3:
            # Find the index of the first occurrence of random_word
            start_index = text.find(random_word)

            # Check if the word is found in the text
            if start_index != -1:
                # Calculate the end index of the word
                end_index = start_index + len(random_word)

                # Delete any of the last 3 characters of the word
                random_index = random.randint(max(end_index - 3, start_index), end_index - 1)

                # Replace the original word with the modified word in the text
                modified_text = text[:random_index] + text[random_index + 1:]

                return modified_text
    else:
        print("Warning: No words found in the text. No modifications made.")

    # If there are no words or the selected word is too short, find another word to replace
    return delete_word_endings(text)


def delete_word_endings_n_times(text, n):
    modified_text = text
    for _ in range(n):
        modified_text = delete_word_endings(modified_text)
    return modified_text


def check_size(file):
    file_stats = os.stat(file)
    file_size = file_stats.st_size
    return file_size


if __name__ == '__main__':
    os.chdir(r'C:/Users/u0149275/OneDrive - KU Leuven/Complexity/EDGe/EDGe_Original/')
    my_files = glob.glob('*.txt')
    path = r'C:/Users/u0149275/OneDrive - KU Leuven/Complexity/EDGe/EDGe_Workspace/'
    all_zipped = []
    for my_file in my_files:
        # open and read the file
        text = open(my_file, "r", encoding='utf-8')
        text = text.read()
        # get the total number of characters of the file
        number = count_characters(text)
        # calculate 10 percent of the total number of characters
        number_to_delete = calculate_10_percent(number)
        zipped = [my_file]
        # get the file name
        name = os.path.splitext(my_file)
        for x in range(100):
            print(x)
            try:
                new_text = delete_word_endings_n_times(text, number_to_delete)
                # write the distorted text to a new file
                with open(path + name[0] + '_deletion.txt', 'w', encoding='utf-8') as new_file:
                    new_file.write(new_text)
                # gzip the distorted file
                with open(path + name[0] + '_deletion.txt', 'rb') as in_f, gzip.open(
                        path + name[0] + '_deletion.txt' + '.gz', 'w') as out_f:
                    out_f.writelines(in_f)
                zipped_distorted_file_size = check_size(path + name[0] + '_deletion.txt.gz')
                zipped.append(zipped_distorted_file_size)
            except:
                print(my_file)
        # add zipped to all_unzipped
        all_zipped.append(zipped)
    df_zipped = pandas.DataFrame(all_zipped)
    df_zipped.to_excel('EDGe_Morph_Suffix_Zipped.xlsx')
