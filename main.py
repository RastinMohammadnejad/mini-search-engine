from pathlib import Path

from indexer import build_index, calculate_idf
from search import search
from snippet import get_snippet
from text_processor import tokenize


DOCUMENTS_DIR = Path("documents")
MAX_RESULTS = 5


def load_documents():
    documents = {}

    for file_path in DOCUMENTS_DIR.glob("*.txt"):
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                documents[file_path.name] = file.read()
        except OSError as error:
            print(f"Could not read {file_path.name}: {error}")

    return documents


def display_results(results, documents, query):
    if not results:
        print("\nNo results found.")
        return

    sorted_results = sorted(
        results.items(),
        key=lambda item: item[1],
        reverse=True
    )

    total_results = len(sorted_results)
    displayed_results = sorted_results[:MAX_RESULTS]

    print(f"\nResults: {total_results}")
    print(f"Showing top {len(displayed_results)} result(s):")

    for position, (filename, score) in enumerate(displayed_results, start=1):
        snippet = get_snippet(documents[filename], query)

        print(f"\n{position}. {filename} (score: {score:.4f})")
        print(f"   {snippet}")


def main():
    documents = load_documents()

    print(f"Found {len(documents)} document(s).")

    index = build_index(documents, tokenize)
    idf = calculate_idf(index, len(documents))

    while True:
        query = input("\nSearch (type 'exit' to quit): ").strip()

        if query.lower() == "exit":
            print("Goodbye!")
            break

        if not query:
            print("Please enter a search query.")
            continue

        results = search(index, idf, query, tokenize)

        display_results(results, documents, query)


if __name__ == "__main__":
    main()