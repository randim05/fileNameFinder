import sys, os
trable = open('trable.txt', 'w')
needName = open("needFileName.txt").readlines()
needName = [i.rstrip() for i in needName]
filelist = os.listdir(path='.')

for i in range(len(filelist)):
    filelist[i] = filelist[i][10:-4]

for i in needName:
    if i not in filelist:
        print(i, file=trable)

trable.close()
