from text_processor import tokenize


def test_tokenize():
    text = "Python, Django, and Python!"

    result = tokenize(text)

    assert result == ["python", "django", "and", "python"]