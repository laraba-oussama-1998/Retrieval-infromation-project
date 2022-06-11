def stringify_file(meta):
    file_words = ''
    try:
        file_words = file_words + ' ' + meta['title']
    except KeyError:
        pass
    try:
        file_words = file_words + ' ' + meta['summary']
    except KeyError:
        pass
    try:
        for word in meta['authors']:
            file_words = file_words + ' ' + word
    except KeyError:
        pass
    return file_words
