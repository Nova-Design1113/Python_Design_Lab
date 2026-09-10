width = float(input("輸入產品寬度"))
height = float(input("輸入產品高度"))

if width < 200 and height < 150:
    print("Compact")
elif width < 400 and height < 300:
    print("Standard")
else:
    print("Large")

print("規格分類完成")