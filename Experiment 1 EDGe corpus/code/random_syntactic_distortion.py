import glob
import os
import re
import random


def tokenize(s: str) -> list[str]:
    return s.split()


def delete_pct_words(s: str, pct: float = 0.1) -> str:
    word_patt = r"\b([\w'-]+)\b"
    matched_tokens: list[re.Match] = list(re.finditer(word_patt, s))
    tokens_count: int = len(matched_tokens)
    pct_is_k: int = int(tokens_count * pct)
    matches_to_replace: list[re.Match] = random.sample(matched_tokens, k=pct_is_k)
    matches_to_replace.sort(key=lambda x: x.end(), reverse=True)
    for match in matches_to_replace:
        s = s[:match.start(1)] + s[match.end(1):]
    # Clean up double spaces
    # s = re.sub(r"[ ]{2,}", ' ', s)
    # s = re.sub(r"(\n|^)( )(?=\w)", '', s)
    return s


if __name__ == '__main__':
    os.chdir(r'C:/Users/u0149275/OneDrive - KU Leuven/Demography/Datasets/EDGe/EDGe_Original')
    my_files = glob.glob('*.txt')
    path = r'C:/Users/u0149275/OneDrive - KU Leuven/Demography/Datasets/EDGe/EDGe_Syntactic_Deletion/'
    for my_file in my_files:
        text = open(my_file, "r")
        text = text.read()
        new_text = delete_pct_words(text, 0.1)
        name = os.path.splitext(my_file)
        with open(path + name[0] + '_syntactic_deletion.txt', 'w') as new_file:
            new_file.write(new_text)
