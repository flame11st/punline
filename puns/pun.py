def pun(words, input_word):
    find_words = []
    details = []
    for word in words:
        if input_word[len(input_word)-2::] == word[:2:]:
            find_words.append(input_word[:len(input_word)-2:]+word)
            details.append(input_word+' + '+word)
        if input_word[len(input_word)-1::] == word[:1:]:
            find_words.append(input_word[:len(input_word)-1:]+word)
            details.append( input_word + ' + ' + word )
        if input_word[:2:] == word[len(word)-2::]:
            find_words.append(word+input_word[2::])
            details.append( word + ' + ' + input_word )
        if input_word[:1:] == word[len(word)-1::]:
            find_words.append(word+input_word[1::])
            details.append( word + ' + ' + input_word )

    return find_words, details
