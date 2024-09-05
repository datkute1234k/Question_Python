try: 

    with open ('Xulynhieudong.txt', 'r', encoding='utf-8') as Input: 
        Docfile = Input.readlines() # đọc file 
        XulyList = ' '.join(Docfile).replace('\n', '')  

        Cacdong = XulyList.split() 
        XulyList = ' '.join(Cacdong)  

    Inra = open ('Xulyxong', 'wb') 
    Inra.write(XulyList.encode('utf8')) 

except FileNotFoundError:
    print('File không tồn tại')

except: 
    print("Lỗi không hợp lệ") 




