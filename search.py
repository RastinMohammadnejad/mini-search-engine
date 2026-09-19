def search(index, query, tokenize):
    query_words = tokenize(query)

    scores = {}

    for word in query_words:
        if word not in index:
            continue

        for filename, count in index[word].items():
            if filename not in scores:
                scores[filename] = 0

            scores[filename] += count

    return scores