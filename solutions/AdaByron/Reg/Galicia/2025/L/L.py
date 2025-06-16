len = int(input())
l1 = [int(x) for x in input().split()]
l2 = [int(x) for x in input().split()]
l3 = []

i = 0
j = 0

while i<len and j<len:
    if l1[i] <= l2[j]:
        l3.append(l1[i])
        i+= 1

    else:
        l3.append(l2[j])
        j+=1

if j == len:
    l3.extend(l2[j:])
else:
    l3.extend(l1[i:])

result = (l3[len-1] + l3[len]) / 2
print(result)