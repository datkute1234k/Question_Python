# Xuất file output trên 1 dòng từ chuỗi input bất kỳ nhập vào từ nhiều dòng 

with open ('inputy.txt', 'r', encoding='utf-8') as Dauvo: 
    Xuly = Dauvo.readlines() # đọc nhiều dòng đang ở dạng list 
    StringJoin = ' '.join(Xuly).replace('\n', '') # xử lý dạng list and xử lý kí tự \n 

Mofloder = open('Mofile', 'wb') 
Mofloder.write(StringJoin.encode('utf8')) 





    



