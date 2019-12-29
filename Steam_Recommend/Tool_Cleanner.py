import os
import glob
def cleanAll():
    for infile in glob.glob(os.path.join(str(os.getcwd()), '*.jpg')):
        os.remove(infile)

def cleanimg():
    try:
        cleanAll()
    except:
        pass

if __name__ == '__main__':
    cleanimg()
