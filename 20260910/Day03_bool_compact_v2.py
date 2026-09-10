width = float(input("輸入產品寬度"))
height = float(input("輸入產品高度"))
material_price = float(input("輸入材料價格"))
material = input("輸入材料")

area = width * height
cost = area * material_price

print(f"產品尺寸：{area}")
print(f"產品成本：{cost}")
print(f"產品材料：{material_price}")

size_ok = width <= 300 and height <=200
cost_ok = cost <=3000
material_ok = material == "塑膠"

if size_ok and cost_ok and material_ok:
    print("可以製作")
elif size_ok and material_ok:
    print("尺寸和材料合格，但成本不合格")
elif size_ok and cost_ok:
    print("尺寸和成本合格，但材料不合格")
elif cost_ok and material_ok:
    print("成本和材料合格，但尺寸不合格")
elif size_ok:
    print("尺寸合格，但成本和材料不合格")
elif cost_ok:
    print("成本合格，但尺寸和材料不合格")
elif material_ok:
    print("材料合格，但尺寸和成本不合格")
else:
    print("無法製作")

print("製造評估完成")