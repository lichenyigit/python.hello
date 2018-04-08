

fo = open("../fo.txt", "r");
#fo = open("../README.md", "r");
print("文件名为：", fo.name);
print(fo.fileno())

for index in range(2):
    line = next(fo);
    print("第 %d 行 - %s "%( index, line));

#关闭文件
fo.close();