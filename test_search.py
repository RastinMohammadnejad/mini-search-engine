from indexer import build_index, calculate_idf
from search import search
from text_processor import tokenize


def test_search_with_tfidf():
    documents = {
        "doc1.txt": "python python django",
        "doc2.txt": "python django django",
        "doc3.txt": "machine learning",
    }

    index = build_index(documents, tokenize)
    idf = calculate_idf(index, len(documents))

    results = search(
        index,
        idf,
        "django",
        tokenize
    )

    assert "doc1.txt" in results
    assert "doc2.txt" in results
    assert results["doc2.txt"] > results["doc1.txt"]


def test_duplicate_query_terms():
    documents = {
        "doc1.txt": "python django",
        "doc2.txt": "python machine learning",
    }

    index = build_index(documents, tokenize)
    idf = calculate_idf(index, len(documents))

    result1 = search(
        index,
        idf,
        "django",
        tokenize
    )

    result2 = search(
        index,
        idf,
        "django django django",
        tokenize
    )

    assert result1 == result2


def test_search_unknown_word():
    documents = {
        "doc1.txt": "python django",
        "doc2.txt": "machine learning",
    }

    index = build_index(documents, tokenize)
    idf = calculate_idf(index, len(documents))

    results = search(
        index,
        idf,
        "database",
        tokenize
    )

    assert results == {}


def test_empty_query():
    documents = {
        "doc1.txt": "python django",
        "doc2.txt": "machine learning",
    }

    index = build_index(documents, tokenize)
    idf = calculate_idf(index, len(documents))

    results = search(
        index,
        idf,
        "",
        tokenize
    )

    assert results == {}


def test_empty_document():
    documents = {
        "doc1.txt": "",
        "doc2.txt": "python django",
    }

    index = build_index(documents, tokenize)
    idf = calculate_idf(index, len(documents))

    results = search(
        index,
        idf,
        "python",
        tokenize
    )

    assert "doc1.txt" not in results
    assert "doc2.txt" in results


def test_logarithmic_tf_ranking():
    documents = {
        "doc1.txt": "python",
        "doc2.txt": "python python python",
        "doc3.txt": "django",
    }

    index = build_index(documents, tokenize)
    idf = calculate_idf(index, len(documents))

    results = search(
        index,
        idf,
        "python",
        tokenize
    )

    assert results["doc2.txt"] > results["doc1.txt"]


def test_logarithmic_tf_grows_less_than_linearly():
    documents = {
        "doc1.txt": "python",
        "doc2.txt": "python python python python",
        "doc3.txt": "django",
    }

    index = build_index(documents, tokenize)
    idf = calculate_idf(index, len(documents))

    results = search(
        index,
        idf,
        "python",
        tokenize
    )

    ratio = results["doc2.txt"] / results["doc1.txt"]

    assert ratio < 4