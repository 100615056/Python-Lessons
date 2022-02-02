# Break and continue statement
# Break and continue
sentence = ["Mandarin", "is", "great","!"]
for word in sentence:
  if word == "is":
    continue
  if word == "!":
    break
  print(word)
