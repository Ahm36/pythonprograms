#7listcheck
list1=[12,56,43,10,9]
list2=[41,34,65,9,0,100,10]
if len(list1)==len(list2):
  print('same length')
else:
  print("not same")
total=sum(list1)
print('sum of the list1',total)
total=sum(list2)
print('sum of the list2',total)
print("numbers occuring in both")
for number in list1:
  if number in list2:
    print(number)