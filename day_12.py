import os
import string
from collections import Counter

print(os.getcwd())

# with open('veidenbaums.txt') as f:
#     print(len(f.read()))

 # it is quite possible that for large files we do not want it all at once

# 1a -> write the function file_line_len(fpath), which returns the number of lines in the file
# check file_line_len ("veidenbaums.txt") -> should be 971 or 972

def file_line_len(file_name):
    with open(file_name, encoding="utf-8") as f:
        line_len=len(f.readlines())
    return line_len
print(file_line_len("veidenbaums.txt"))
# create a file object

# 1b -> write the function get_poem_lines (fpath), which returns a list with only those lines that contain poetry.
# So we want to avoid/filter out those lines that contain whitespace and also those lines with poem titles.
# PS preferably use encoding = "utf-8"


def get_poem_lines(file_name):
    with open(file_name, encoding="utf-8") as f:
        nonempty_lines = [line.strip("\n") for line in f if line != "\n"]
    return nonempty_lines
print(get_poem_lines("veidenbaums.txt"))

# 1c -> write the function save_lines (destpath, lines)
# This function will store all lines into destpath file
#1d -> call save_lines with destpath being "veid_poems.txt" and lines being the poem lines we cleaned from 1b


def save_lines(new_file_name, lines):
    with open(new_file_name, "w", encoding="utf-8") as f:
        for line in lines:
            f.write(line +"\n")
        return lines
print(save_lines("veid_poems.txt", get_poem_lines("veidenbaums.txt")))


# 1e -> write the function clean_punkts (srcpath, destpath)
# function will open the srcpath file, clear it from https://docs.python.org/3/library/string.html#string.punctuation
# then function will save the cleaned text into destpath

def clean_punkts(srcpath, destpath, bad_chars=string.punctuation, encoded="UTF-8"):
    with open(srcpath, mode="r", encoding=encoded) as src_file, open(destpath, mode="w", encoding=encoded) as dest_file:
        text = src_file.read()
        for p in bad_chars:
            text = text.replace(p, "")  # we replace each bad char with empty string
        dest_file.write(text)


# clean_punkts("veidenbaums_clean.txt", "veidenbaums_clean_punkts.txt")
clean_punkts("veid_poems.txt", "veidenbaums_clean_punkts.txt", bad_chars=string.punctuation + "…")

# 1f -> write the function get_word_usage (srcpath, destpath)
# The function opens the file and finds the most frequently used words
# recommendation to use Counter module!
# assume that the words are separated by either whitespace or newline (the good old split will come in handy)
# the saved list of words and frequency should be saved in destpath in the following form:
# vards skaits
# un 3423
# es 3242
# PS to test, for srcpath use the file that is poetry only and has no punctuation and also the words are all in lowercase

#def get_word_usage (srcpath, destpath):
with open("veidenbaums_clean_punkts.txt", encoding="utf-8") as f:
    word_list=Counter(f)
    word_list.most_common((10))
print("", word_list.most_common(10))
#print(get_word_usage("veid_poems.txt", "common_words.txt")
