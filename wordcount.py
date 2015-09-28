# put your code here.
def counting_words(file_name):
    text_file = open(file_name)
    word_count = {}
    for line in text_file:
        strip_line = line.strip()
        poem = strip_line.split(' ')
        for word in poem: 
            if word in word_count:
                word_count[word] = word_count[word] +1
            elif word not in word_count:
                word_count[word] = 1
    text_file.close()

    for word in word_count:
        print word, word_count[word]


counting_words("twain.txt")
