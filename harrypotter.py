f=open("harry_potter.txt","r")
txt=f.read()
# print(txt)
txt=txt.split('\n')
book=txt[0]
author=txt[-1]

year=[]
parts=[]
for i in range(1,len(txt)-1):
  year.append(int(txt[i][-5:-1]))
  parts.append(txt[i][:-7])


harry={}
for i in range(len(year)):
  harry[book+"-"+str(i+1)]={"title":parts[i],"year":year[i],"author":author}

for i in harry:
  print(i,harry[i])

f.close()
