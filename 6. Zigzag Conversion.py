string = input("Enter the string  :")
n = int(input("Enter the number of rows  : "))
lst = [[]]*n
count = 0
charlst = list(string)
print(charlst)
"""
for i in charlst:
    if count == n:
        count = 0
    lst[count].append(i)
    count+=1

for i in lst:
    for j in lst:
        print(i, end=" ")
    print("\n")
    """
iter = 0
for i in range(1,n):
    for j in charlst.length:
        print(charlst[i])
        print(" ")
        j = j + (n-i)
    print('\n')


