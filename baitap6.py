n=int(input("Nhap n ="))
i=0
S=0
for i in range (1,n+1):
    S += 1 / (i*(i+1))
print("Tong S=",S)