width = float(input("產品寬度"))
height = float(input("產品高度"))

if width >= 300 and height >= 200:
    print("可上貨運")
elif width >= 300 or height >= 200:
    print("需要尺寸檢查")
else:
    print("不可上貨運")

print("尺寸檢查完畢")