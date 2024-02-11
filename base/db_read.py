from os import listdir
from os.path import isfile, join
import logging

logger = logging.getLogger('main_script')

def readData(fileName:str):
    '''
    READ DATA FROM CSV FILE
    '''
    logger.info('Reading file ' + fileName)
    res : list[str] = list()
    count = 0
    try:
        with open(fileName,'r') as f:
            listRead = f.readlines()[1:]
            for lineX in listRead:
                res.append(lineX.split(',')[0])
                count=count+1
        logger.info(str(count) + ' entries read')
    except:
        logger.warning('Data fetch failed')
    else:
        return res

def readDBFolder(folderPath:str):
    '''
    READ DATA FROM FOLDER CONTAINING CSV FILES
    '''
    mypath = folderPath
    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    res : list[str] = list()
    
    logger.info('Path : ' + mypath)
    logger.info('Files collected : ' + str(len(onlyfiles)))

    for fileX in onlyfiles:
        if(fileX.endswith('.csv') or fileX.endswith('.dat') or fileX.endswith('.txt')):
            res.extend(readData(mypath + '/' + fileX))
    return res
