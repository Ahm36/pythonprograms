dict={
    "ABC":101,
    "BCS":999,
    "JKL":888,
    "IHG":897,
    "XYZ":345,
    "MKF":998
}
print("Ascending order")
for i in sorted(dict.keys()):
    print(i,dict[i])
print("Descending order")
for i in sorted(dict.keys(),reverse=-1):
    print(i,dict[i])