import logging
import os

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
f = logging.Formatter('%(asctime)s-%(levelname)s-%(message)s')
fh = logging.FileHandler("debugging.log",mode='w')
fh.setFormatter(f)
logger.addHandler(fh)

def cheackname(name):
    logger.debug(f'checking name "{name}" ...')
    if os.path.exists('data.txt'):
        with open('data.txt','r') as file1:
            for i in file1:
                if i.lower().startswith(f'name: {name.lower()}'):
                    logger.error(f'Name:"{name}" already exists')
                    return False
            if len(name) == 0 :
                logger.critical("name cannot be blank")
                return False
            elif not name.isalpha():
                logger.critical("name must be alphabet")
                return False
            else:
                logger.error(f'check ssuccessfully')
                return True
    else:
        logger.debug(" no data found")
        return True
    
def savedata(name,age,email):
    logger.debug("saving details of {name}...")
    with open('data.txt','a') as file2:
        file2.write(f'Name: {name} - Age: {age} - Email: {email}\n')
        logger.info(f'Details saved successfully')
        print("save successfully")



