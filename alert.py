# ### alert.py
# Author: Theunkn0wn1
# function: provide means of setting customizable alerts for ratsignals
#   such as for specific platforms / languages
# ###

import logging
import sys
from configparser import ConfigParser
from utils.playground.shared_resources import Parser, Case

# setup log

logging.basicConfig(format="%(levelname)s :%(message)s", level=logging.WARNING)

#create a stream handler
streamHandle = logging.StreamHandler(sys.stdout)
# create a file handler
fileHandle = logging.FileHandler("logs/alerts.log", 'w')
# create formatter
formatter = logging.Formatter('%(levelname)s\t [%(name)s]: %(message)s')

#set the stream and file formatters
streamHandle.setFormatter(formatter)
fileHandle.setFormatter(formatter)
# get the log
log = logging.getLogger('alerts')
log.setLevel(logging.DEBUG)
# add handlers to our logger
log.addHandler(streamHandle)
log.addHandler(fileHandle)


log.error("HO")
log.log(logging.INFO, "potato")
print(log)
log.info("log setup done.")
# logging.basicConfig(level=logging.WARNING)



def init()->None:
    """
    Module init
    :return: None
    """
    log.debug("Init: creating config parser....")
    config_parser = ConfigParser()
    log.info("Init: reading config file...")
    config = config_parser.read('config.ini')
    log.warning(config)

if __name__ == "__main__":
    pass

# import time
#
# while 1:
#     where = file.tell()
#     line = file.readline()
#     if not line:
#         time.sleep(1)
#         file.seek(where)
#     else:
#         print line, # already has newline
