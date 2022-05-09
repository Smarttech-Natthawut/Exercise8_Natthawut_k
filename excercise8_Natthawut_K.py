Book = int(30)
Pen = int(10)
Pencil = int(5)
Eraser = int(5)


usernameInput = input("กรุณาใส่ Username :")
passwordInput = input("กรุณาใส่ Password :")
if usernameInput  == "admin"  and passwordInput == "1234":
    print("-----ยินดีให้บริการครับ----")
    print("-------- iShop --------")

    print ("-------กรุณาเลือกรายการสินค้า-----")
    print (("1. Book-------"),(Book),("THB/เล่ม"))
    print (("2. Pen--------") ,(Pen),("THB/ด้าม"))
    print (("3. Pencil-----"),(Pencil),("THB/แท่ง"))
    print (("4. Eraser-----"),(Eraser),("THB/ก้อน"))

    userSelected = int(input("กรุณาเลือก 1 หรือ 2 หรือ 3 หรือ 4 >>>  "))

    if userSelected == 1:
        print ("กรุณาเลือกจำนวนสินค้า  :")
        quatity = int((input("เลือกจำนวนที่ต้องการ 1 ,2 ,3 ...10  >>>>  ")))
        price = quatity * Book
        print (("ราคารวม"),price , ("THB"))
        print ("--------ขอบคุณที่ใช้บริการ--------")

    elif userSelected == 2:
        print ("กรุณาเลือกจำนวนสินค้า  :")
        quatity = int((input("เลือกจำนวนที่ต้องการ 1 ,2 ,3 ...10  >>>>  ")))
        price = quatity * Pen
        print (("ราคารวม"),price , ("THB"))
        print ("--------ขอบคุณที่ใช้บริการ--------")

    elif userSelected == 3:
        print ("กรุณาเลือกจำนวนสินค้า  :")
        quatity = int((input("เลือกจำนวนที่ต้องการ 1 ,2 ,3 ...10  >>>>  ")))
        price = quatity * Pencil
        print (("ราคารวม"),price , ("THB"))
        print ("--------ขอบคุณที่ใช้บริการ--------")

    elif userSelected == 4:
        print ("กรุณาเลือกจำนวนสินค้า  :")
        quatity = int((input("เลือกจำนวนที่ต้องการ 1 ,2 ,3 ...10  >>>>  ")))
        price = quatity * Eraser
        print (("ราคารวม"),price , ("THB"))
        print ("--------ขอบคุณที่ใช้บริการ--------")

    elif userSelected > 4:
        print ("ขออภัย!!!  กรุณาทำรายการใหม่")
        print ("ขอบคุณที่ใช้บริการ โอกาสหน้าเชิญใหม่คร้าบบบบ")

else:
    print ("ขออภัยข้อมูลไม่ถูกต้อง กรุณาทำรายการใหม่อีกครั้ง")
    print ("-------------ขอบตุณที่ใช้บริการ-----------")