x=int(input(" Nhập vào một năm bất kì x:"))
if ((x%4==0) and (x%100!=0)) or (x%400==0):
    print("Đây là năm nhuận")
else:
    print("Đây không phải là năm nhuận")

