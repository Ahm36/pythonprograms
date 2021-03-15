#3listcomp
#a
l1=[21,-10,0,-19,57,-18,13,-1]
l2=[x for x in l1 if x>0]
print(l2)
#b
li1=[]
num=int(input("enter the number of element:"))
for i in range(num):
    ele=int(input("enter element:"))
    li1.append(ele)
print(" list entered:",li1)
Square=[x**2 for x in li1]
print("square of list elements:",Square)
#c
n=input("enter the word:")
result=[x for x in n if x in ['a','e','i','o','u']]
print(result)
#d
word=input("enter the word:")
ordvalue=[ord(i) for i in word]
print(ordvalue)ṣ