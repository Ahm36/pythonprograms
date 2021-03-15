#8$
word=input("enter the word:")
word1=word
frst=word[0]
word=word.replace(frst,"$")
word=frst+word[1:]
print(word1,">>",word)