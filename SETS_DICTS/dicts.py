# dersin konusu: dictionary yapısı

# arabam ={
#     "marka":"mercedes",
#     "model":"e200",
#     "yılı": 2023,
#     "yakıtı":"lpg",
#     "rengi":"siyah"
# }

# arabam2=dict(marka="doğan",model="slx",yılı=1993,yakıtı="lpg",rengi="gri")

# print(arabam)
# print()
# print(arabam2)

# print(arabam2["marka"])

# print(len(arabam))

# benimmarkam=arabam.get("marka")
# print(benimmarkam)

# print(arabam.keys())
# print(type(arabam.keys()))
# print(type(arabam.values()))

# arabam["yılı"]=2024
# print(arabam)

# items=arabam.items()
# print(items)

# if"mercedes" in arabam:
#     print("buldum")
# else:
#     print("yok gardas...")

# arabam.update({"jant":25})
# print(arabam)

# arabam.popitem()
# print(arabam)

# del arabam["rengi"]
# print(arabam)

# arabam.clear()
# print(arabam)

# for i in arabam:
#     print(i)

# for i in arabam:
#     print(arabam[i])

# for anahtar,deger in arabam.items():
#     print(anahtar + ":"+str(deger))

# degişkenin yeni kopyasını olusturmak için
# seninaraban = arabam.copy()
# seninaraban["marka"] = "skoda"
# seninaraban["marka"] = "fabia"
# seninaraban["yılı"] = 2012

# print(arabam)
# print(seninaraban)

# iç içe dictionary
# ailem = {
#     "anne":{
#         "adı":"rahime","yası":28
#         },
#     "baba":{
#         "adı":"cabbar","yası":35
#         },
#     "kardes":{
#         "adı":"aydan","yası":28
#         }
# }

# for anahtar, degerler in ailem.items():
#     print(anahtar)
#     for deger in degerler:
#         print(deger + ":",degerler[deger])

# liste içinde liste

# listem = [[1,5,7],
#           [10,15,18],
#           [30,37,39]
        #   ]

# for i in listem:
#     for j in i:
#         print(j,end=" ")
#     print()



