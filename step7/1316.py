n = int(input())
cnt = 0
for i in range(n):
  a=input()
  for j in range(len(a)):
    if j!=len(a)-1:
      if a[j]==a[j+1]:
        pass
      elif a[j] in a[j+1:]:
        break
    else:
      cnt+=1
print(cnt)