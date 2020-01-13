ProFile = open("project_twitter_data.csv", "r")
ResFile = open("resulting_data.csv", "w")

punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']

def strip_punctuation(str):
    for x in punctuation_chars:
        str = str.replace(x, '')
    return str

# lists of words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())

def get_pos(str):
    str = strip_punctuation(str)
    cp = 0
    for x in str.split():
        if x in positive_words:
            cp = cp + 1
    return cp

negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())

def get_neg(str):
    str = strip_punctuation(str)
    cp = 0
    for x in str.split():
        if x in negative_words:
            cp = cp + 1
    return cp

ResFile.write("Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score")
ResFile.write("\n")
read = ProFile.readlines()
read.pop(0)
for lines in read:
    lst = lines.strip().split(",")
    ResFile.write("{}, {}, {}, {}, {}".format(lst[1], lst[2], get_pos(lst[0]), get_neg(lst[0]), (get_pos(lst[0])-get_neg(lst[0]))))
    ResFile.write("\n")
ProFile.close()
ResFile.close()