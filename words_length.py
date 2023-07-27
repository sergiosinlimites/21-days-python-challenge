def count_words_by_length(words):
  # Tu código aquí 👈
  len_words = [len(word) for word in words]
  return {len(word): len_words.count(len(word)) for word in words}

result = count_words_by_length([
  "apple",
  "banana",
  "orange",
  "grapefruit",
  "pear",
  "kiwi"
])

print(result)