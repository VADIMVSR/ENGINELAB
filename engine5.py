def same_by (lam,val):
  r=list(map(lam,val))
  t=len(val)
  k=int(0)
  for i in range (0,t):
    if r[i]==0:
      k+=1
  return t==k

ish = []
n=int(input())
for i in range(0,n):
  print(i+1,"Число:")
  ii=int(input())
  ish.append(ii)
if (same_by(lambda x:x%2,ish)):
  print("SAME")
else:
  print("different") 
