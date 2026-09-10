width = float(input("輸入產品寬度"))
height = float(input("輸入產品高度"))
material_price = float(input("輸入材料價格"))

area = width * height
cost = area * material_price

size_ok = width <= 300 and height <=200
cost_ok = cost <=3000

print(f"產品面積：{area}")
print(f"材料成本：{cost}")

if size_ok and cost_ok:
    print("可以製作")
elif size_ok and not cost_ok:
    print("尺寸合格，但成本過高")
else:
    print("尺寸超出製作範圍")

print("製造評估完成")