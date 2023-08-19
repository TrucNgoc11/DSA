n = int(input())
ar = [int(i) for i in input().split()]

new = sorted((ar[i],i+1) for i in range(n))
print(new)
res = [new[i][1] for i in range(n)]
print(res)
swap = []
for i in range(n-1):
  if new[i][0] == new[i+1][0]:
    swap.append((i,i+1))
    if len(swap) == 2:
      print("YES")
      print(" ".join(str(i) for i in res))
      for j,k in swap:
        res[j],res[k] = res[k],res[j]
        print(" ".join(str(i) for i in res))
      quit()
print("NO")