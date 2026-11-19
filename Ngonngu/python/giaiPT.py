a = float(input("Nhap a: "))
b = float(input("Nhap b: "))
if a == 0:
    print("Phuong trinh vo so nghiem" if b == 0 else "Phuong trinh vo nghiem")
else:
    print("Nghiem x =", -b / a)
