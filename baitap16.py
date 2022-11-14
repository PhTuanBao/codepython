x = int(input(" Nhap so x ="))
n = int(input(" Nhap so n ="))
a=0
Tong=0
i=0
for i in range(1,n+1):
    a=a+i
    Tong +=  (x ** i) / a
print("Tong =",Tong)