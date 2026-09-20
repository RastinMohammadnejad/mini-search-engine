def search(index, idf, query, tokenize):
    query_words = tokenize(query)
    query_words = set(query_words)

    scores = {}

    for word in query_words:
        if word not in index:
            continue

        for filename, term_frequency in index[word].items():
            score = term_frequency * idf[word]

            if filename not in scores:
                scores[filename] = 0

            scores[filename] += score

    scores = {
        filename: score
        for filename, score in scores.items()
        if score > 0
    }

    return scores