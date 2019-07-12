from collections import Counter
a1=int(input())
a2=list(map(int,input().split()))
a3=Counter(a2)
list=[]
for a in a3.items():
  if(a[1] != 1):
   print(a[0],end ='')
for b in a3.items():
  list.append(b[1])
if(max(list) == 1):
 print("unique")
  
