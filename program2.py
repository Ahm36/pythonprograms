#2leapyear
cyear=int(input("enter the current year:"))
lyear=int(input("enter the last year:"))
for i in range(cyear,lyear+1):
  if(i%4==0 and i%100!=0 or i%400==0):
    print(i)
  i=i+1