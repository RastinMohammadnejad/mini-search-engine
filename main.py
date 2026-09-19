from pathlib import Path

from indexer import build_index, calculate_idf
from search import search
from text_processor import tokenize


DOCUMENTS_DIR = Path("documents")


def load_documents():
    documents = {}

    for file_path in DOCUMENTS_DIR.glob("*.txt"):
        with open(file_path, "r", encoding="utf-8") as file:
            documents[file_path.name] = file.read()

    return documents


def main():
    documents = load_documents()

    print(f"Found {len(documents)} document(s).\n")

    index = build_index(documents, tokenize)
    idf = calculate_idf(index, len(documents))

    query = input("Search: ")

    results = search(index, idf, query, tokenize)

    if results:
        print("\nResults:")

        sorted_results = sorted(
            results.items(),
            key=lambda item: item[1],
            reverse=True
        )

        for filename, score in sorted_results:
            print(f"- {filename} (score: {score:.4f})")
    else:
        print("\nNo results found.")


if __name__ == "__main__":
    main()