# Xác định 3 loại tam giác cạnh nhập vào 

import math 
# cho người dùng nhập vào 
# cũng có thể gây ra lỗi 
try:
    a,b,c = map(float, input().split()) 
except: 
    print('Lỗi') 
# kiểm tra điều kiện có phải là cạnh của tam giác hay không 

if a + b > c and a + c > b and b + c > a:
    # tính tam giác vuông  
    if a*a == b*b + c*c or b*b == a*a + c*c or c*c == a*a + b*b:
        Loaitamgiac = 'Vuong' 
    # tam giác đều 
    elif a == b and b == c: 
        Loaitamgiac = 'Deu'
    # tam giác cân
    elif a == b or  b == c or a == c: 
        Loaitamgiac = 'Can' 
    # tam giác tù
    elif a*a > b*b + c*c or b*b > a*a + c*c or c*c > a*a + b*b:
        Loaitamgiac = 'Tu' 
    else:
        Loaitamgiac = 'Nhon' 
    print('{}, {}, {}, Đây là 3 cạnh của tam giác {}'.format(a,b,c, Loaitamgiac))
else: 
    print('{}, {}, {} Đây không phải là 3 cạnh của tam giác'.format(a,b,c))


        

    
