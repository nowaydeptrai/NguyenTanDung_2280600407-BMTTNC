def chia_het_cho_5(nhi_phan):  
    return int(nhi_phan, 2) % 5 == 0  

input_str = input("Nhập chuỗi số nhị phân (cách nhau bởi dấu phẩy): ")  
so_nhi_phan_list = input_str.split(',')  

ket_qua = [so for so in so_nhi_phan_list if chia_het_cho_5(so)]  

if ket_qua:  
    print(",".join(ket_qua))  
else:  
    print("Không có số nào hợp lệ")
