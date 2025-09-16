import sys
from stats import get_num_words,get_char_count, get_sorted_char_count

def get_book_text(filepath):
  with open(filepath) as f:
    file_contents = f.read()
    return file_contents



def main():
  if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
  book_text = get_book_text(sys.argv[1])
  char_count = get_char_count(book_text)
  sorted_char_count = get_sorted_char_count(char_count)

  print("===================== BOOKBOT =====================")
  print(f"Analyzing book found at {sys.argv[1]}...")
  print("------------------- Word Count --------------------")
  print(f"Found {get_num_words(book_text)} total words")
  print("----------------- Character Count -----------------")
  for char in sorted_char_count:
    print(f"{char["char"]}: {char["num"]}")

main()