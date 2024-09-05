# Viết chương trình nhập vào từ file input {Tên}, {Tuổi hiện tại} 
# và xuất ra file output theo mẫu sau: 
# “Vao 20 nam nua, tuoi cua {Tên} se la {Tuổi cần tìm}”. 
# có sử lý ngoại lệ 
try: 
    with open('inputy.txt', 'r', encoding=('utf-8')) as FileInput: # đọc file tiếng việt
        ten = FileInput.readline().rstrip('\n') 
        tuoi = int(FileInput.readline().rstrip('\n')) 

    with open('Outputt', 'wb') as FileOutput: # lam viec voi du lieu nhi phan, bi unicode 
        Unicode = 'Vao 40 năm nữa, tuổi của {} sẽ là {}'.format(ten, tuoi + 40)
        FileOutput.write(Unicode.encode('utf8'))
except FileNotFoundError: 
    print('File không tồn tại')
except: 
    print("Dữ liệu của bạn không hợp lệ") 

