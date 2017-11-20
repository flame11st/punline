import random

transl = {
    'w': 'в', 'e': 'е', 'r': 'р', 't': 'т', 'u': 'у', 'i': 'и', 'o': 'о', 'p': 'п', 'a': 'а', 's': 'с', 'd': 'д',
    'f': 'ф', 'g': 'г', 'h': 'х', 'k': 'к', 'l': 'л', 'z': 'з', 'c': 'ц', 'v': 'в', 'b': 'б', 'n': 'н', 'm': 'м',
    'ch': 'ч', 'sh': 'ш', 'к': 'k', 'е': 'e', 'н': 'n', 'г': 'g', 'ф': 'f', 'в': 'v', 'а':'a', 'п': 'p', 'р': 'r',
    'о': 'o', 'л': 'l', 'д': 'd', 'м': 'm', 'и': 'i', 'т': 't', 'б': 'b','с':'s',
}


def pun(words, input_word, bool):
    find_words = []     #dict to return
    parts = []      #for check if word is added in find words
    count = 0
    len_words = len(words)

    if bool:        #combi puns
        for el in range( 1000 ):
            ind = random.randint( 0, len_words - 1 )

            # random word
            word = words[ind]

            # check if word is added in find words
            if parts.count( input_word + ' + ' + word ) == 1 or parts.count( word + ' + ' + input_word ) == 1: continue

            # if we need only 6 words
            if count >= 6:
                return find_words

            # algoritm for searching puns
            try:
                if transl[input_word[-2::]] == word[:1:]:
                    find_words.append( [input_word.capitalize(), word[1::], input_word + ' + ' + word] )
                    parts.append( input_word + ' + ' + word )
                    count += 1
            except KeyError:
                pass
            try:
                if transl[input_word[-1::]] == word[:1:] and word[:2:] != 'sh':
                    find_words.append( [input_word.capitalize(), word[1::], input_word + ' + ' + word] )
                    parts.append( input_word + ' + ' + word )
                    count += 1
            except KeyError:
                pass

    else:       #common puns
        for el in range(1000):
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
                find_words.append([input_word.capitalize(), word[2::], input_word+' + '+word])
                parts.append(input_word+' + '+word)
                count += 1
            if input_word[-1::] == word[:1:]:
                find_words.append([input_word.capitalize(), word[1::],input_word + ' + ' + word])
                parts.append( input_word + ' + ' + word )
                count += 1
            if input_word[:2:] == word[-2::]:
                find_words.append([word[:-2:].capitalize(), input_word, word + ' + ' + input_word])
                parts.append( word + ' + ' + input_word )
                count += 1
            if input_word[:1:] == word[-1::]:
                find_words.append([word[:-1:].capitalize(), input_word, word + ' + ' + input_word])
                parts.append( word + ' + ' + input_word )
                count += 1
    return find_words
