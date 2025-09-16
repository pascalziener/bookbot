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

def sort_on(items):
  return items["num"]

def get_sorted_char_count(char_counts):
  sorted_char_count = list({"char": k, "num": v} for k,v in char_counts.items())
  sorted_char_count.sort(reverse=True, key=sort_on)
  return sorted_char_count


