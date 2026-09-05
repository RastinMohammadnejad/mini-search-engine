
def build_index(documents, tokenize):
    index = {}

    for filename, content in documents.items():
        words = tokenize(content)

        for word in words:
            if word not in index:
                index[word] = set()

            index[word].add(filename)

    return index