from stats import get_num_words,get_char_count

def get_book_text(filepath):
  with open(filepath) as f:
    file_contents = f.read()
    return file_contents

def sort_on(items):
  return items[1]

def main():
  book_text = get_book_text("books/frankenstein.txt")
  print(f"{get_num_words(book_text)} words found in the document")
  char_count = get_char_count(book_text)

  sorted_char_count = dict(sorted(char_count.items(), key=sort_on, reverse=True))

  for char in sorted_char_count:
    print(f"'{char}': {sorted_char_count[char]}")

main()