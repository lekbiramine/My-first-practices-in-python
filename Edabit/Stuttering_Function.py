# def stutter(word):
#     return (word[0:2]+ "...") * 2 + " " + word + "?"
# print(stutter("incredible"))

def stutter(word):
    prefix = word[:2]
    return f"{prefix}... {prefix}... {word}?"
print(stutter('outstanding'))