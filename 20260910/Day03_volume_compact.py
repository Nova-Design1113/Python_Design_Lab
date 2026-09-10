width = float(input("輸入產品寬度"))
height = float(input("輸入產品高度"))
depth = float(input("輸入產品深度"))

volume = width * height * depth

print(f"產品體積：{volume}")

if volume < 1000000:
    print("Small")
elif volume < 5000000:
    print("Medium")
else:
    print("Large")

print("體積分類完成")