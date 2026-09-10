material_price = float(input("輸入材料單價"))
width = float(input("輸入產品寬度"))
height = float(input("輸入產品高度"))

area = width * height
cost = area * material_price

print(f"產品面積：{area}")
print(f"材料成本：{cost}")

if cost < 1000:
    print("低成本")
elif cost < 3000:
    print("中等成本")
else:
    print("高成本")

print("成本計算完成")