import os
from datetime import datetime








year = str(datetime.now().year)
if len(str(datetime.now().month)) == 1 :
    month = "0" + str(datetime.now().month)
else:
    month = str(datetime.now().month)
dir_name = year + month + "照片"

if dir_name not in os.listdir("./"):
    os.mkdir(dir_name)