# Viết chương trình nhập vào từ file input {Tên}, {Tuổi hiện tại} 
# và xuất ra file output theo mẫu sau: 
# “Vao 20 nam nua, tuoi cua {Tên} se la {Tuổi cần tìm}”. 
with open('inputyy.txt', 'r') as Fileinput: 
    ten = Fileinput.readline().rstrip() 
    tuoi = int(Fileinput.readline().rstrip()) 

with open('output.txt', 'w') as Fileoutput: 
    Fileoutput.write('Vào 20 năm nua, {} se la {} tuoi'.format(ten, tuoi + 20))

  