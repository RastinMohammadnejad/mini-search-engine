from snippet import get_snippet


def test_snippet_contains_query_word():
    text = "Python is a popular programming language."

    result = get_snippet(text, "python")

    assert "Python" in result


def test_snippet_returns_part_of_long_text():
    text = (
        "Python is a popular programming language. "
        "It is used for web development, automation, "
        "data science, and machine learning."
    )

    result = get_snippet(text, "machine")

    assert "machine" in result
    assert len(result) <= 100


def test_snippet_with_empty_query():
    text = "Python is a programming language."

    result = get_snippet(text, "")

    assert result == text


def test_snippet_when_query_not_found():
    text = "Python is a programming language."

    result = get_snippet(text, "database")

    assert result == text