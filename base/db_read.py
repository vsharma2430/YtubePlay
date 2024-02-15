from os import listdir,walk,path
from os.path import isfile, join
import logging

logger = logging.getLogger('main_script')

def readData(file_name:str):
    '''
    READ DATA FROM CSV FILE
    '''
    logger.info('Reading file ' + file_name)
    res : list[str] = list()
    count = 0
    try:
        if(file_name.endswith('.csv') or file_name.endswith('.dat') or file_name.endswith('.txt')):
            with open(file_name,'r',encoding="utf8",errors='ignore') as f:
                listRead = f.readlines()[1:]
                for lineX in listRead:
                    res.append(lineX.split(',')[0])
                    count=count+1
            logger.info(str(count) + ' entries read')
    except Exception as error:
        logger.warning('Data fetch failed : ', error)
        return res
    else:
        logger.warning('Data fetch successful')
        return res

def readDBFolder(folder_path:str):
    '''
    READ DATA FROM FOLDER CONTAINING CSV FILES
    '''
    mypath = folder_path
    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    res : list[str] = list()
    
    logger.info('Path : ' + mypath)
    logger.info('Files collected : ' + str(len(onlyfiles)))

    for fileX in onlyfiles:
        if(fileX.endswith('.csv') or fileX.endswith('.dat') or fileX.endswith('.txt')):
            res.extend(readData(mypath + '/' + fileX))
    return res

def readDir(user_path:str):
    logger.info('Path : ' + user_path)

    fname = []
    if(path.isdir(user_path)):
        for root,d_names,f_names in walk(user_path):
            for f in f_names:
                file_path = join(root,f)
                fname.append(file_path)
                logger.info('File found : ' + file_path)
    elif(path.isfile(user_path)):
        fname.append(user_path)

    res : list[str] = list()
    logger.info('Total files collected : ' + str(len(fname)))

    for fileX in fname:
        res.extend(readData(fileX))
    return res
    