# put your code here.
import sys

file_name = sys.argv[1]

def counting_words(file_name):
    text_file = open(file_name)
    word_count = {}
    puctuation = ',.?!@#$%^&*~-:;-_"'
    
    for line in text_file:
        strip_line = line.strip()
        poem = strip_line.split()
        for word in poem:
            no_punct =""
            for char in word:
                if char not in puctuation:
                    no_punct = no_punct + char
            word = no_punct.lower()
            if word in word_count:
                word_count[word] = word_count[word] +1
            elif word not in word_count:
                word_count[word] = 1
    text_file.close()

    for word in word_count:
        print word, word_count[word]


counting_words(file_name)
