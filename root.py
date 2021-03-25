import os

def open_dir(root, valueList):
    for file in os.listdir(root):
        path = os.path.join(root, file)
        if os.path.isdir(path):
            valueList = open_dir(path, valueList)
        if file.split('.')[-1] == 'txt':
            valueList.append(file.split('.')[0])
    return valueList

valueList = []
valueList = open_dir('./root', valueList)
print(valueList)