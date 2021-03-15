#9replace
word=str(input("enter a word"))
copy=word
word=word[-1:] + word[1:-1] + word[:1]
print(copy,">>",word)