width = float(input("輸入產品寬度"))
height = float(input("輸入產品高度"))
depth = float(input("輸入產品深度"))

if width <= 300 and height <=200 and depth <= 250:
    print("可以列印")
else:
    print("超出列印範圍")

print("尺寸檢查完成")