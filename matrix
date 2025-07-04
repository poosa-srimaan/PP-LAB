r=int(input("enter row size : "))
col=int(input("enter column size : "))
mat1=[]
print("enter matrix 1 ")
for i in range(r):
    row=[]
    for j in range(col):
        n=int(input(f"enter element in mat{[i]}{[j]} : "))
        row.append(n)
    mat1.append(row)
    
mat2=[]
print("enter matrix 2 ")
for i in range(r):
    row =[]
    for j in range(col):
        n=int(input(f"enter element in mat{[i]}{[j]} : "))
        row.append(n)
    mat2.append(row)

sum_mat=[]
print("sum of matrix")
if len(mat1)==len(mat2):
    for i in range(r):
        row=[]
        for j in range(col):
            sum=mat1[i][j]+mat2[i][j]
            row.append(sum)
        sum_mat.append(row)
            
print(sum_mat)

print("multplication of mat")
mult_mat=[]
for i in range(r):
    row=[]
    for j in range(col):
        s=0
        for k in range(r):
            s+=mat1[i][k]*mat2[k][j]
        row.append(s)
    mult_mat.append(row)
print(mult_mat)
    
