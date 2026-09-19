from collections import Counter


def build_index(documents, tokenize):
    index = {}

    for filename, content in documents.items():
        words = tokenize(content)
        word_counts = Counter(words)

        for word, count in word_counts.items():
            if word not in index:
                index[word] = {}

            index[word][filename] = count

    return index