import csv

path = "C:\\Gizem\\JSON\\sinif.csv"
# with open(path,encoding="utf-8") as file:
#     metin = csv.reader(file,delimiter=",")
#     for line in metin :
#         print(line)

    ##### metin = file.read()
    # for line in file:
    #     print(line)

############################################################
# lines = []
# with open(path,encoding="utf-8") as file:
#     for line in file:
#         lines.append(line.strip().split(","))

# for i in lines:
#     print(i)
#############################################################
lines = []
path2 = "C:\\Gizem\\JSON\\sinif2.csv"
with open(path,encoding="utf-8") as file:
    metin = csv.reader(file)
    with open(path2,"w") as file2:
        toWrite = csv.writer(file2)

        for line in metin:
            lines.append(line)

print(lines)
for i in range(len(lines)):
    for j in range(len(lines[0])):
        print(lines[i][j],end="\t")
    print(i)
            # toWrite.writerow(line)