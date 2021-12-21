m = 5
n = 5
for i in range(1,m+1):
    for j in range(1,m+1):
        if j>=m:
          print('*',end="")
        else:
          print(end=" ")

    m= m-1
    print()
