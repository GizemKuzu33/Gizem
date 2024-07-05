import json 

# myDict = {"adi":"Python","yasi":45,"renkliMi": False, " hayattaMi": True,"sevdiği meyve":None}

# print(myDict["hayattaMi"])
# for key,val in myDict.items():
#     print(key,val)

# print(myDict)
# print(type(myDict))
# jsonStr = json.dumps(myDict)
# print(jsonStr)
# print(type(jsonStr))

""""""""""""
# try:
#     myJsonStr = '{"adi": "Python", "yasi": 45, "renkliMi": False, " hayattaMi": true, "sevdi\u011fi meyve": null}'
#     newDict = json.loads(myJsonStr)
# except Exception as e:
#     print(str(e))
#     print("JSON String Donusum Hatası")
# else:
#     print(type(newDict))
#     print(newDict) 

""""""""""""

# myDict = {"adi":"Python","yasi":45,"renkliMi": False, " hayattaMi": True,"sevdiği meyve":None}

# jsonStr = json.dumps(myDict,indent=4,sort_keys=True)
# print(jsonStr)
# print(type(jsonStr))

""""""""""""
# DOSYA AÇMA ve deger değistirme

path = "C:\\Gizem\\JSON\some (1).json"

with open(path) as jFile:
    data = json.load(jFile)
    print(type(data))
    print(data)

jString = json.dumps(data,indent=4)
##print(jString)

### print(data["cars"][1]["hacim"])

for keys,vals in data["cars"][1].items():
    print(keys,vals)