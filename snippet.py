from text_processor import tokenize


def get_snippet(text, query, max_length=100):
    query_words = set(tokenize(query))

    if not query_words:
        return text[:max_length]

    words = text.split()

    for index, word in enumerate(words):
        word_tokens = tokenize(word)

        if any(token in query_words for token in word_tokens):
            start = max(0, index - 3)
            end = min(len(words), index + 4)

            snippet = " ".join(words[start:end])

            if start > 0:
                snippet = "... " + snippet

            if end < len(words):
                snippet += " ..."

            return snippet[:max_length]

    return text[:max_length]