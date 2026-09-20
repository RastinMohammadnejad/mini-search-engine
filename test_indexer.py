from indexer import build_index, calculate_idf
from text_processor import tokenize


def test_build_index():
    documents = {
        "doc1.txt": "Python Python Django",
        "doc2.txt": "Python Django Django",
    }

    index = build_index(documents, tokenize)

    assert index["python"]["doc1.txt"] == 2
    assert index["python"]["doc2.txt"] == 1

    assert index["django"]["doc1.txt"] == 1
    assert index["django"]["doc2.txt"] == 2


def test_calculate_idf():
    documents = {
        "doc1.txt": "python django",
        "doc2.txt": "python django",
        "doc3.txt": "machine learning",
    }

    index = build_index(documents, tokenize)
    idf = calculate_idf(index, len(documents))

    assert idf["python"] > 0
    assert idf["django"] > 0

    assert idf["machine"] > 0
    assert idf["learning"] > 0