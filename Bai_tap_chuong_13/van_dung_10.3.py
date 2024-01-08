ten_tap_tin=input("nhập tên tập tin:")
with open("Rain.txt",'w',encoding='utf-8') as f:
    print("nhập nội dung")
    f.write("Rain rain, go away; Come again another day...\n")
f=open("Rain.txt",'r')
noi_dung=f.read()
print(noi_dung)
print("đã ghi nội dung vào tập tin Rain.txt")
print("Rain rain, go away; Come again another day...")
f.close 
