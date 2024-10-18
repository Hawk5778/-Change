n = int(input("いくら投入しますか？（1円硬貨は使えません）"))
x = int(input("いくらの商品を購入しますか？（10円単位です）"))
y = n - x

x500yen = 0
x100yen = 0
x50yen = 0
x10yen = 0

while True:
    if y - 500 >= 0:
        x500yen += 1
        y -= 500
        continue
    elif y - 100 >= 0:
        x100yen += 1
        y -= 100
        continue
    elif y - 50 >= 0:
        x50yen += 1
        y -= 50
        continue
    elif y - 10 >= 0:
        x10yen += 1 
        y -= 10
        continue
    elif n - x <= 0:
        print("お金が足りません！")
        break
    else:
        break

print("おつり\n500円が",x500yen,"枚\n100円が",x100yen,"枚\n50円が",x50yen,"枚\n10円が",x10yen,"枚です。")


        

