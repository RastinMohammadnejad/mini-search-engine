import re


def tokenize(text):
    text = text.lower()

    words = re.findall(r"\b\w+\b", text)

    return words