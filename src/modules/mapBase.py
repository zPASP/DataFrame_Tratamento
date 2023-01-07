import os

def allFiles (folder):
    try:
        listFiles = os.listdir (fr'./{folder}')
        return listFiles
    except:
        return False

def specificFile (folder, format):
    try:
        listFiles = []
        for x in (allFiles(folder)):
            if x.endswith (f'.{format}'):
                listFiles.append(x)
        return listFiles
    except:
        return False


