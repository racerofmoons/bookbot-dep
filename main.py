def main():
    file_path = "books/frankenstein.txt"
    text = read_book(file_path)
    word_count = word_counter(text)
    alpha = "abcdefghijklmnopqrstuvwxyz"
    print(f"There are {word_count} words. Letters have the following frequency:")
    letter_count = letter_counter(checker(list(text), alpha), build_dictionary(alpha))
    print(letter_count)

def read_book(book):
    with open(book) as f:
        return f.read()

def word_counter(text):
    words = text.split()
    return len(words)

def build_dictionary(alpha):
    letter = {}
    for i in range(26):
        letter[alpha[i]] = 0
    return letter

def checker(letter_list, alpha):
    alpha_list = []
    for i in letter_list:
        if i in alpha:
            alpha_list.append(i)
    return alpha_list

def letter_counter(letters, dictionary):
    for l in letters:
        dictionary[l] += 1
    return dictionary

if __name__ == "__main__":
    main()