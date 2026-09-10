weight = float(input("請輸入產品重量(公斤)"))

if weight >= 10:
    print("需要兩人搬運")
elif weight < 10:
    print("可由一人搬運")

print("重量檢查完成")