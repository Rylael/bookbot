def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    report = count_and_sort_chars(text)
    print(f"{num_words} words found in the document")


def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()

    
def count_and_sort_chars(text):
    char_dict = {}
    text = text.lower()
    for char in text:
        if char.isalpha():
            if char in char_dict:
                char_dict[char] += 1
            else:
                char_dict[char] = 1
    for key in sorted(char_dict, key=char_dict.get, reverse=True):
        print(f"'{key}': {char_dict[key]}")
main()