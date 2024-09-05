# Viết 1 chương trình người dùng nhập vào và xuất toàn bộ số nguyên 
# cách nhau bởi dấu cách và tự tính tổng 

print('Vui lòng nhập số cần tính của bạn vào: ') 

Giayso = input() 

Xyludaucach = Giayso

 
Ganco: False 

try: 
    Xulysonguyen = map(int, Xyludaucach) 
    Xulytinhtong = sum(Xulysonguyen) 

    Ganco = True 

except: 
    print("Không hợp lệ")

if Ganco:
    print("Sau khi tính tổng của bạn là: ", Xulytinhtong) 