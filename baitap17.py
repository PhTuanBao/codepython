x = int(input(" Nhap so x = "))
n = int(input(" Nhap so n = "))
a = 1 
S = 0
for i in range(1,n+1):
    a = a*i
    S += (x ** i) / a
print("Tong =",S)