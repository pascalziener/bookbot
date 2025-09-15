def get_num_words(text):
  return len(text.split())


def get_char_count(text):
  char_count = {}
  for char in text:
    c = char.lower()
    if not c.isalpha():
      continue
    if c in char_count:
      char_count[c] += 1
    else:
      char_count[c] = 1

  return char_count
