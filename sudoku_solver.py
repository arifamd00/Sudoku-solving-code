h  = []
count = 1
countc =1
while True:
   n = input()
   if n=='':
      break
   else:
      h.append(n)
from datetime import datetime
start = datetime.now()
row = {}.fromkeys([X for X in range(1,len(h)+1)])
col = {}.fromkeys([X for X in range(1,len(h)+1)])
for H in range(len(h)):
   temp_row = []
   for J in range(len(h[H])):
      m = int(h[H][J])
      temp_row.append(m)
   row[count] = temp_row
   count +=1
for a in range(len(h)):
   c = 0
   temp_col =[]
   while c< len(h):
      A = int(h[c][a])
      temp_col.append(A)
      c +=1
   col[countc] = temp_col
   countc +=1
print('row',row,'\n','col',col)
complete_1 =[]
complete_2 = []
complete_3 = []
if len(h)==4:
   for C in range(len(h)):
      sub = []
      for M in range(2):
         M_ = int(h[C][M])
         sub.append(M_)
      complete_1.append(sub)
   for C in range(len(h)):
      sub = []
      for M in range(2,4):
         M_ = int(h[C][M])
         sub.append(M_)
      complete_2.append(sub)
print(complete_1,'\n',complete_2)
if len(h)==9:
   for C in range(len(h)):
      sub = []
      for M in range(3):
         M_ = int(h[C][M])
         sub.append(M_)
      complete_1.append(sub)
   for C in range(len(h)):
      sub = []
      for M in range(3,6):
         M_ = int(h[C][M])
         sub.append(M_)
      complete_2.append(sub)
   for C in range(len(h)):
      sub = []
      for M in range(6,9):
         M_ = int(h[C][M])
         sub.append(M_)
      complete_3.append(sub)
print(complete_1,'\n',complete_2,'\n',complete_3)
mat = {}.fromkeys([X for X in range(len(complete_1))])
m=0
l=0
mp=0
if len(h)==4:
   while mp<4:
      temp_1 =[]
      temp_2 =[]
      if mp<2:
         while l<2 and m<2: 
            temp_1.append(complete_1[l])
            temp_2.append(complete_2[m])
            l+=1
            m +=1
         mat[mp] =temp_1
         mp +=1
         mat[mp] =temp_2
         temp_1 =[]
         temp_2 =[]
         mp +=1
      if mp>=2:
         while l<4 and m<4:
            temp_1.append(complete_1[l])
            temp_2.append(complete_2[m])
            l +=1
            m+=1
         mat[mp] = temp_1
         mp+=1
         mat[mp] = temp_2
         mp+=1
n =0
if len(h)==9:
   while mp<9:
      temp_1 =[]
      temp_2 =[]
      temp_3 =[]
      if mp<3:
         while l<3 and m<3 and n<3: 
            temp_1.append(complete_1[l])
            temp_2.append(complete_2[m])
            temp_3.append(complete_3[n])
            l+=1
            m +=1
            n +=1
         mat[mp] =temp_1
         mp +=1
         mat[mp] =temp_2
         mp+=1
         mat[mp] = temp_3
         temp_1 =[]
         temp_2 =[]
         temp_3 =[]
         mp +=1
      if mp>=3 and mp<6:
         while l<6 and m<6 and n<6:
            temp_1.append(complete_1[l])
            temp_2.append(complete_2[m])
            temp_3.append(complete_3[n])
            l +=1
            m+=1
            n+=1
         mat[mp] = temp_1
         mp+=1
         mat[mp] = temp_2
         mp+=1
         mat[mp] =temp_3
         temp_1 =[]
         temp_2 =[]
         temp_3 =[]
         mp+=1
      if mp>=6 and mp<9:
         while l<9 and m<9 and n<9:
            temp_1.append(complete_1[l])
            temp_2.append(complete_2[m])
            temp_3.append(complete_3[n])
            l +=1
            m+=1
            n+=1
         mat[mp] = temp_1
         mp+=1
         mat[mp] = temp_2
         mp+=1
         mat[mp] =temp_3
         mp +=1
end = datetime.now()
print(end-start)
print(mat)

