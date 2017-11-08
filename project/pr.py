# coding=cp1251
from shutil import copyfile
from pathlib import Path

# читает названия файлов и записывает в список словарей
def readFromFile(filename):
    file = open(filename, 'rt', encoding='cp1251')
    elems = []
    for elem in file:
        my_file = Path(elem.strip())
        if my_file.is_file():
            # file exists
            tmpElem = {}
            tmp = elem.strip()
            tmpElem['path'] = tmp
            tmp = tmp.split('\\')
            tmpElem['name'] = tmp.pop()
            tmpElem['folder'] = tmp.pop()
            elems.append(tmpElem)
    return elems

# копирует файлы в указанную папку
def copyFiles(files, destination):
    for file in files:
        newName = file['folder'] + '_' + file['name']
        copyfile(file['path'], destination + '\\' + newName)


# читаем файлы
items = readFromFile('files.txt')
# Копируем в указанную папку
copyFiles(items, 'C:\\Python34\\projects\\project\\backups')
