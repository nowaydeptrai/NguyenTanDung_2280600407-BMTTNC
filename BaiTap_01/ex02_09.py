def la_so_nguyen_to(n):  
    if n < 2:  
        return False  
    for i in range(2, int(n ** 0.5) + 1):  
        if n % i == 0:  
            return False  
    return True  

number = int(input("Nhập số cần kiểm tra: "))  

if la_so_nguyen_to(number):  
    print(f"{number} là số nguyên tố.")  
else:  
    print(f"{number} không phải là số nguyên tố.")
