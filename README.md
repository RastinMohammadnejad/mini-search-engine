# Mini Search Engine

A simple search engine built with Python to demonstrate the core concepts behind text search and document ranking.

The project processes text documents, builds an inverted index, searches for matching terms, and ranks results using TF-IDF with logarithmic term frequency.

## Features

- Read and process text documents
- Text tokenization
- Inverted index
- Single-word and multi-word search
- Term Frequency (TF)
- Inverse Document Frequency (IDF)
- TF-IDF ranking
- Logarithmic Term Frequency
- Duplicate query term handling
- Zero-score result filtering
- Search result count
- Top-N result display
- Search result snippets
- Basic file reading error handling
- Automated tests with pytest

## How It Works

The search engine follows several main steps.

### 1. Load Documents

Text files inside the `documents/` directory are loaded and stored in memory.

### 2. Tokenization

The text is converted to lowercase and split into individual words.

For example:

```text
"Python, Django, and Python!"
```

becomes:

```text
["python", "django", "and", "python"]
```

### 3. Inverted Index

The search engine builds an inverted index that stores which documents contain each word and how many times the word appears.

Example:

```text
python:
    python.txt: 3
    django.txt: 1
```

This allows the search engine to quickly find documents containing a query term.

### 4. TF-IDF Ranking

Search results are ranked using TF-IDF.

The project uses logarithmic term frequency:

```text
TF = 1 + log(term_frequency)
```

The IDF value is calculated as:

```text
IDF = log(total_documents / document_frequency)
```

The final score for a term is:

```text
score = TF × IDF
```

Scores from multiple query terms are added together to produce the final document score.

### 5. Result Filtering

Documents with a final score of zero are removed from the results.

The remaining documents are sorted by score, and only the configured number of top results is displayed.

### 6. Search Snippets

For each result, the search engine displays a short part of the document related to the query.

Example:

```text
1. machine_learning.txt (score: 3.8459)
   Machine learning is a ...
```

## Project Structure

```text
mini-search-engine/
│
├── documents/
│   ├── python.txt
│   ├── django.txt
│   ├── machine_learning.txt
│   ├── data_science.txt
│   └── databases.txt
│
├── main.py
├── text_processor.py
├── indexer.py
├── search.py
├── snippet.py
│
├── test_indexer.py
├── test_search.py
├── test_snippet.py
├── test_tokenization.py
│
├── .gitignore
└── README.md
```

### Main Files

| File                   | Description                                            |
| ---------------------- | ------------------------------------------------------ |
| `main.py`              | Runs the search engine and handles the interactive CLI |
| `text_processor.py`    | Contains text processing and tokenization logic        |
| `indexer.py`           | Builds the inverted index and calculates IDF           |
| `search.py`            | Performs searches and calculates document scores       |
| `snippet.py`           | Generates short snippets for search results            |
| `test_indexer.py`      | Tests indexing and IDF calculation                     |
| `test_search.py`       | Tests searching and ranking                            |
| `test_snippet.py`      | Tests snippet generation                               |
| `test_tokenization.py` | Tests tokenization                                     |

## Installation

Clone the repository:

```bash
git clone https://github.com/RastinMohammadnejad/mini-search-engine.git
```

Move into the project directory:

```bash
cd mini-search-engine
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

Install pytest:

```bash
python -m pip install pytest
```

## Usage

Run the search engine:

```bash
python main.py
```

The application will display the number of available documents:

```text
Found 5 document(s).
```

Enter a search query:

```text
Search (type 'exit' to quit): python machine learning
```

Example output:

```text
Results: 2
Showing top 2 result(s):

1. machine_learning.txt (score: 3.8459)
   Machine learning is a ...

2. python.txt (score: 1.8326)
   Python is a popular ...
```

To exit the application:

```text
exit
```

## Running Tests

The project uses `pytest` for automated testing.

Run:

```bash
pytest
```

Current test suite:

```text
14 passed
```

The tests cover:

- Tokenization
- Inverted index creation
- IDF calculation
- TF-IDF search
- Multi-word queries
- Duplicate query terms
- Unknown search terms
- Empty queries
- Empty documents
- Zero-score filtering
- Logarithmic TF ranking
- Search snippets

## Configuration

The maximum number of displayed results can be changed in `main.py`:

```python
MAX_RESULTS = 5
```

For example:

```python
MAX_RESULTS = 10
```

would display up to 10 results.

## Limitations

This project is intentionally kept as a small search engine and does not currently include:

- Web interface
- REST API
- Database-backed document storage
- Elasticsearch or other external search engines
- Stemming or lemmatization
- Spell correction
- Autocomplete
- Distributed search
- Persistent search index

## Future Improvements

Possible future improvements include:

- Better text normalization
- Improved snippet generation
- More advanced ranking algorithms
- Phrase search
- Search result highlighting
- Stemming or lemmatization
- Persistent indexing
- Web interface
- REST API
- Larger document collections

## Technologies

- Python
- pytest
- Git
- GitHub

## Purpose

This project was built as a practical implementation of fundamental information retrieval concepts, including tokenization, inverted indexes, TF-IDF, and document ranking.

Author

## Rastin Mohammadnejad

- GitHub: https://github.com/RastinMohammadnejad
- Repository: https://github.com/RastinMohammadnejad/mini-search-engine