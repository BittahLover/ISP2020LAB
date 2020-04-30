import os
import re
import sys


def sortStrings(arr):
    newArr = []
    for s in arr:
        newArr.append(re.split(split, s))
        newArr[-2].append(s)
    newArr.sort(reverse=reverseSort)
    arr = []
    for s in newArr:
        arr.append(s.pop())
    return arr


def sortNums(arr):
    newArr = []
    for s in arr:
        newArr.append(re.split(split, s))
        newArr.append([int(x) for x in newArr.pop()])
        newArr[-2].append(s)
    newArr.sort(reverse=reverseSort)
    arr = []
    for s in newArr:
        arr.append(s.pop())
    return arr


def sortFile(fileName):
    file = open(fileName, 'r')

    lines = []

    for s in file.readlines():
        lines.append(s)
    file.close()

    if numsSort:
        lines = sortNums(lines)
    else:
        lines = sortStrings(lines)

    file = open(fileName, 'w')
    for i in lines:
        file.write(str(i))
    file.close()


def check_str(file_name):
    with open(file_name, 'r') as f:
        notEnd = True
        while notEnd:

            arrPart = f.readlines(20000)
            if len(arrPart) == 0:
                break

            try:
                for i in arrPart:
                    for j in re.split(split, i):
                        int(j)
            except ValueError:
                print("ValueError ")
                return False
            except MemoryError:
                print("MemoryError")
                return False

            if len(arrPart) == 0:
                notEnd = False
    return True


def readFile(f, size):
    part = []

    while sys.getsizeof(part) < size:
        s = f.readline()
        if s == '':
            break
        part.append(s)

    return part


def splitFile(name, partSize):
    partsNames = []

    f = open(name, 'r')

    not_end = True

    while not_end:

        part = readFile(f, partSize)

        if len(part) == 0:
            break

        partName = 'part' + str(len(partsNames))

        part_file = open(partName, 'w')

        for i in part:
            part_file.write(i)

        part_file.close()

        partsNames.append(partName)

        if (f.tell() == os.fstat(f.fileno()).st_size):
            not_end = False

    f.close()
    return partsNames


def mergeSort(partNames, outName):
    outFile = open(outName, 'w')
    mass = []
    for i in partNames:
        part = open(i, 'r')
        mass.append(part)

    parts = []
    for i in mass:
        parts.append(i.readline())

    while parts != [''] * len(parts):
        idx = None

        for i, v in enumerate(parts):
            if v == '':
                continue

            if not reverseSort:
                if idx is None or v < parts[idx]:
                    idx = i
            else:
                if idx is None or v > parts[idx]:
                    idx = i

        outFile.write(str(parts[idx]))

        parts[idx] = mass[idx].readline()

    for i in mass:
        i.close()

    outFile.close()


print("Reverse sort? (y/N)", end=' ')
st = input()
reverseSort = "Y" == st.upper()

split = re.compile(" ")

fileName = "numbers.txt"
print('Memory limit to temp files (in bytes):', end=' ')
partsSize = int(input())

numsSort = check_str(fileName)

partsNames = splitFile(fileName, partsSize)
for f in partsNames:
    sortFile(f)

mergeSort(partsNames, 'sorted.txt')


def deleteFiles():
    dir = os.getcwd()
    dirs = os.listdir(dir)
    for d in dirs:
        if re.match(r"part\d+", d) is not None:
            os.remove(d)


deleteFiles()
