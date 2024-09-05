# tính chiều cao
print('Vui lòng nhập tên or chiều cao vào:') 

yourname1, tall1 = input().split() 
yourname2, tall2 = input().split() 

tall11 = int(tall1) 
tall11 = int(tall2)


if tall1 > tall2: 
    print(yourname1 + " Cao hơn "+ yourname2) 

elif tall1 ==  tall2: 
    print(yourname1 + " Bằng " + yourname2)

else: 
    print(yourname2 + " Thấp hơn "+ yourname1) 
 
 
