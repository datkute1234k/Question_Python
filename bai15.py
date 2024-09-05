# tính chiều cao có xử lý ngoại lệ
print('Vui lòng nhập tên or chiều cao vào:') 
try:
    yourname1, tall1 = input().split() 
    yourname2, tall2 = input().split() 

    if tall1.endswith('cm'): 
        tall1 = tall1[:-2]
    if tall2.endswith('cm'): 
        tall2 = tall2[:-2]

 
    tall11 = int(tall1) 
    tall11 = int(tall2)


    if tall1 > tall2: 
        print(yourname1 + " Cao hơn "+ yourname2) 

    elif tall1 ==  tall2: 
        print(yourname1 + " Bằng " + yourname2)

    else: 
        print(yourname2 + " Thấp hơn "+ yourname1)
except ValueError: 
    print('Số bạn không hợp lệ vui lòng nhập số nguyên')
except: 
    print("Không hợp lệ")

  
 
