import glob
import os
import math
import random


def count_characters(file):
    data = file.replace(" ", "")
    number_of_characters = len(data)
    return number_of_characters


def calculate_10_percent(num):
    return math.ceil((num / 100) * 10)


def delete_characters(f, n):
    for _ in range(n):
        index = random.randint(0, len(f) - 1)
        while f[index].isspace():
            index = index - 1
        f = f[:index] + f[index + 1:]
    return f


if __name__ == '__main__':
    os.chdir(r'C:/Users/u0149275/OneDrive - KU Leuven/Demography/Datasets/EDGe/EDGe_Original')
    my_files = glob.glob('*.txt')
    path = r'C:/Users/u0149275/OneDrive - KU Leuven/Demography/Datasets/EDGe/EDGe_Random_Deletion/'
    for my_file in my_files:
        text = open(my_file, "r")
        text = text.read()
        number = count_characters(text)
        number_to_delete = calculate_10_percent(number)
        new_text = delete_characters(text, number_to_delete)
        name = os.path.splitext(my_file)
        with open(path + name[0] + '_deletion.txt', 'w') as new_file:
            new_file.write(new_text)
