# Kiểm tra 3 số có là cạnh của tam giác
# nhập input từ người dùng 
# ép kiểu sang float 
# sử lệnh cậu lệnh if else để kiểm tra 
# nếu a + b > c and a + c > b and b + c > a và ngược lại

print('Vui lòng nhập 3 cạnh là tam giác vào') 
try: 
    a, b, c = map(float, input().split()) 

    if a + b > c and a + c > b and b + c > a: 
        print(" {}, {}, {} Là ba cạnh của tam giác".format(a,b,c)) 
    else: 
        print("{}, {}, {} Không phải là 3 cạnh của tam giác".format(a,b,c)) 
except: 
    print("Không hợp lệ") 