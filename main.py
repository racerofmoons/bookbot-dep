def main():
    file_path = "books/frankenstein.txt"
    text = read_book(file_path)
    word_count = word_counter(text)
    print(f"There are {word_count} words.")

def read_book(book):
    with open(book) as f:
        return f.read()

def word_counter(text):
    words = text.split()
    return len(words)

if __name__ == "__main__":
    main()