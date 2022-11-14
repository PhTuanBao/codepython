x = int(input(" Nhap so x ="))
n = int(input(" Nhap so n ="))
S=0
i =0
for i in range(n):
    S += x ** (2*i+1)
print("Tong S",S)
