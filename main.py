from stats import count_words, count_chars, sort_chars
import sys

def get_book_text(filepath):
    try:
        with open(filepath) as f:
            text = f.read()
        return text
    except OSError as e:
        print(f"Error reading file '{filepath}': {e}")
        sys.exit(1)
    
def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book = sys.argv[1]
    text = get_book_text(book)
    word_count = count_words(text)
    char_count = count_chars(text)
    sorted_chars = sort_chars(char_count)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for item in sorted_chars:
        c = item["char"]
        if c.isalpha():
            print(f"{c}: {item['num']}")
    print("============= END ===============")
    return

main()