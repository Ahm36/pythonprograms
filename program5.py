#5listint
list=[]
for i in range(10):
  x=int(input('enter the elements:'))
  if x<100:
    list.append(x)
  else:
    list.append('over')
print(list)