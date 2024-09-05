try: 
    with open('copyy.txt', 'r') as Input:
            dongDauTien = Input.readline().rstrip('\n') 

    a, b, c = map(float, dongDauTien.split())

    # Kiểm tra điều kiện tam giác
    if (a + b > c) and (a + c > b) and (b + c > a): 
        if (a ** 2 == b ** 2 + c ** 2) or (b ** 2 == a ** 2 + c ** 2) or (c ** 2 == a ** 2 + b ** 2):
            Tamgiac = 'Vuông' 
        elif a == b == c: 
            Tamgiac = 'Đều' 
        elif a == b or b == c or a == c: 
            Tamgiac = 'Cân' 
        elif (a ** 2 > b ** 2 + c ** 2) or (b ** 2 > a ** 2 + c ** 2) or (c ** 2 > a ** 2 + b ** 2):
            Tamgiac = 'Tù' 
        else: 
            Tamgiac = 'Nhọn' 
        thongBao = ('Kết quả: 3 cạnh của bạn nhập vào {}, {}, {} là tam giác {}'.format(a, b, c, Tamgiac)) 
    else: 
        thongBao = 'Đây không phải là 3 cạnh của một tam giác'
except FileNotFoundError:
    thongBao = 'Không tìm thấy file đầu vào'
except: 
    thongBao = ('Định dạng của bạn không hợp lệ')

# Ghi kết quả vào file 
with open('output.txt', 'w') as Output: 
    Output.write(thongBao) 