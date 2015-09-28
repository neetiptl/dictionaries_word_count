# put your code here.
text_file = open("test.txt")
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



