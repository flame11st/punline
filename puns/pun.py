def pun(words):
    word1 = str( input() ).lower()
    find_words_last_1 = []
    find_words_last_2 = []
    find_words_first_1 = []
    find_words_first_2 = []

    for word in words:
        if word1[len(word1)-2::] == word[:2:]:
            find_words_last_2.append(word1[:len(word1)-2:]+word.upper())
        elif word1[len(word1)-1::] == word[:1:]:
            find_words_last_1.append(word1[:len(word1)-1:]+word.upper())
        elif word1[:2:] == word[len(word)-2::]:
            find_words_first_2.append(word.upper()+word1[2::])
        elif word1[:1:] == word[len(word)-1::]:
            find_words_first_1.append(word.upper()+word1[1::])

    if find_words_last_2: print( 'Last 2: '+','.join(find_words_last_2) )
    if find_words_last_1: print( 'Last 1: '+','.join(find_words_last_1) )
    if find_words_first_2: print( 'First 2: '+','.join(find_words_first_2) )
    if find_words_first_1: print( 'First 2: '+','.join(find_words_first_1) )