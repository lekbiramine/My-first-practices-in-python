def remove_duplicate_words_from(sentence):
  hi = []

  for word in sentence : 
    if word[0] == word[1]: 
      word[1].append(hi)


  return sentence



# Testing Ouput
print(remove_duplicate_words_from("Hello Elzero Web Web Hello School"))
# Hello Elzero Web School