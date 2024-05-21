A=int(0)
B=int(0)
C=int(0)
D=int(0)
def get_transcriptions(t):
  global A,B,C,D
  ni=t.find('-',0,len(t))
  np=t.find(':',0,len(t))
  if t[ni+1:np]=="перевод":
    A+=1
    B+=int(t[np+1:len(t)])
  elif t[ni+1:np]=="оплата_жкх":
    C+=1
    D+=int(t[np+1:len(t)])
  return 0


re=int(0)

while re == 0:
  print("Введите транзакцию")
  str1=str(input())
  get_transcriptions(str1)
  print("Чтобы ввести ещё одну транзакцию нажмите: 0")
  re=int(input())
print(A," перевод ",B,"\n",C," оплата жкх ",D)

 
