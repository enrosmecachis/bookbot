def main():
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)
    word_count = get_word_count(book_text)
    chars = get_chars(book_text)
    sorted_chars = sort_chars(chars)

    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
                'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in the document")

    for char in sorted_chars:
        # if char["char"].isalpha():  # return true if character is alphabetic
        if char["char"] in alphabet:
            print(f"The '{char['char']}' character was found {
                char['count']} times")

    print("--- End report ---")


def get_book_text(path):
    with open(path) as f:
        return f.read()


def get_word_count(text):
    return len(text.split())


def get_chars(contents):
    chars = {}

    for char in contents.lower():
        if char not in chars:
            chars[char] = 1
        else:
            chars[char] += 1

    return chars


def sort_chars(chars):
    char_list = []
    for char in chars:
        char_count = chars[char]
        char_list.append({"char": char, "count": char_count})

    def sort_on(dict):
        return dict["count"]

    char_list.sort(key=sort_on, reverse=True)
    return char_list


main()
