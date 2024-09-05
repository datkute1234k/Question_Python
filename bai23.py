# Giải phương trình bậc nhất và bậc hai (Có xử lý ngoại lệ đầu vào) 

import math 

def giai_ptbac1(a,b): 
    if a == 0: 
        if b == 0: 
            return 'Phương trình có vô số nghiệm.' 
        else: 
            return 'Phương trình vô nghiêm.' 
    else: 
        return f'Phương trình có nghiệm x = {-b / a}' 
    
def giai_ptbac2(a,b,c): 
    if a == 0: 
        return giai_ptbac1 
    delta = b**2 - 4*a*c 
    if delta < 0: 
        return 'Phương trình vô nghiệm' 
    elif delta == 0: 
        return f'Phương trình có nghiệm kép x = {-b / 2*a}'
    else:
        x1 = -b + math.sqrt(delta) / 2*a
        x2 = -b - math.sqrt(delta) / 2*a
        return  f'Phương trình có 2 nghiệm phân biệt là x1 = {x1}, x2 = {x2}' 
    
print('Vui lòng chọn phương trình cần giải') 
print('1. Phương trình bậc nhất ax + b = 0') 
print('2. Phương trình bậc hai ax + b2 + c = 0') 
option = int(input('Vui lòng nhập chọn 1 hoặc hai:')) 

if option == 1: 
    a = float(input('Vui lòng nhập a')) 
    b = float(input('Vui lòng nhập b'))
    print(giai_ptbac1(a,b)) 
elif option == 2: 
    a = float(input('Vui lòng nhập a')) 
    b = float(input('Vui lòng nhập b'))
    c = float(input('Vui lòng nhập c')) 
    print(giai_ptbac2(a,b,c)) 
else: 
    print('Bạn vừa nhập sại Vui lòng nhập 1 hoặc 2')



    
    

