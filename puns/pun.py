import random


def pun(words, input_word):
    find_words = []     #dict to return
    parts = []      #for check if word is added in find words
    count = 0
    len_words = len(words)

    for el in range(500):
        ind = random.randint(0, len_words-1)

        #random word
        word = words[ind]

        #check if word is added in find words
        if parts.count(input_word + ' + ' + word) == 1 or parts.count(word + ' + ' + input_word) == 1: continue

        #if we need only 6 words
        if count >= 6:
            return find_words

        #algoritm for searching puns
        if input_word[-2::] == word[:2:]:
            find_words.append([input_word[:-2:].capitalize()+word, input_word+' + '+word])
            parts.append(input_word+' + '+word)
            count += 1
        if input_word[-1::] == word[:1:]:
            find_words.append([input_word[:-1:].capitalize()+word,input_word + ' + ' + word])
            parts.append( input_word + ' + ' + word )
            count += 1
        if input_word[:2:] == word[-2::]:
            find_words.append([word.capitalize()+input_word[2::], word + ' + ' + input_word])
            parts.append( word + ' + ' + input_word )
            count += 1
        if input_word[:1:] == word[-1::]:
            find_words.append([word.capitalize()+input_word[1::], word + ' + ' + input_word])
            parts.append( word + ' + ' + input_word )
            count += 1
    return find_words
