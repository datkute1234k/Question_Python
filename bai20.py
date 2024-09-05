# giải phương trình bậc 2 

# tính denta 

import math

def giaiphuongtrinhbac2(a,b,c): 
    # tính denta 
    delta = b**2 - 4*a*c 

    if delta > 0: 
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        return f'Phương trình có 2 nghiệm phân biệt là: x1 = {x1:.3f}, x2 = {x2:.3f}'
    elif delta == 0: 
        x = (-b / 2*a) 
        return f'Phương trình có nghiệm kép là: {x:.3f} '
    else: 
        return 'Phương trình vô nghiệm' 
    
a = map(float(input('Vui lòng nhập hệ số của a:'.split())))
b = map(float(input('Vui lòng nhập hệ số của b:'.split())))
c = map(float(input('Vui lòng nhập hệ số của c:'.split())))

call = giaiphuongtrinhbac2(a,b,c)  
print(call)




