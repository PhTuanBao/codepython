n = int(input(" Nhap so n="))
a=1
Tong=0
for i in range(n):
    a=a+i
    Tong += 1 / a
print("Tong =",Tong)