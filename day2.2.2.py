import dattt as dat
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
f = logging.Formatter('%(asctime)s-%(levelname)s-%(message)s')
fh = logging.FileHandler("employee.log",mode='w')
fh.setFormatter(f)
logger.addHandler(fh)

name =input("enter the employee name")
age = int(input("enter the employee age"))
email = input("enter the emailId")

if dat.cheackname(name) is True:
    dat.savedata(name,age,email)
else:
    logger.critical("employee check failer")

logger.debug('end of employee program')
