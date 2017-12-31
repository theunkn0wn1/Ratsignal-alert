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

logging.basicConfig(format="%(levelname)s :%(message)s", level=logging.ERROR)

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

log.info("log setup done.")
# logging.basicConfig(level=logging.WARNING)

class config_error(Exception):
    """
    generic config error
    """
    pass

def init()->None:
    """
    Module init
    :return: None
    """
    log.debug("Init: creating config parser....")
    config_parser = ConfigParser()
    log.info("Init: reading config file...")
    # config = config_parser.read('config.ini')
    # if config == [] :
    #     log.warning("Config file not found. generating defaults...")
    #     with open('config.ini', 'w'):
    #         log.warning("config file was not found or blank. writing new...")
    #         # config was null, first run ?
    #         section = 'files'
    #         config_parser.add_section(section)
    #         config_parser.set(section=section, option='channel_fuelrats', value='/path/to/#fuelrats')
    #         config_parser.write('config.ini')
    # try:
    #     log.debug("fetching log data....")
    #     logfile = config_parser.get('files', 'channel_fuelrats')
    #     log.info("got logfile data, path is {}".format(logfile))
    # except Exception as ex:
    #     log.critical("Unable to find log file configuration.")
    #     with open('config.ini', 'w') as file:
    #         log.warning("config file was not found or blank. writing new...")
    #         # config was null, first run ?
    #         section = 'files'
    #         config_parser.add_section(section)
    #         config_parser.set(section=section, option='channel_fuelrats', value='/path/to/#fuelrats')
    #         config_parser.write(file)
    # log.warning(config)


def make_default_config_file(parser:ConfigParser=None, filename ='config.ini', filemode = 'w')->None:
    """
    Generates a default config filename
    :param parser: config parser instance
    :param filename: config filename by name to write to
    :param filemode: mode to open file, must be capable of writing
    :return: None
    """
    if not parser:
        parser = ConfigParser()
    # make filename configs
    section = 'files'
    log.info("making {} configs....".format(section))
    parser.add_section(section)
    parser.set(section, 'channel_fuelrats', "/path/to/#fuelrats.txt")
    parser.set(section, "alarm_sound", "/path/to/alarms/")

    # make options configs
    section = 'options'
    log.info("making {} configs....".format(section))
    parser.add_section(section)
    parser.set(section, 'onPlatform', "0")
    parser.set(section, "platform", str(['pc','xb','ps']))
    parser.set(section, "onLanguage", "0")
    parser.set(section, "language", "en")
    parser.set(section, "onCodeRed", "0")
    log.info("done initializing new configs, writing to disk.")
    # write to config filename
    try:
        with open(filename,filemode) as file:
            parser.write(file)
    except Exception as ex:
        log.fatal("Unable to write config filename, error is as follows:")
        log.error(str(ex))
        raise config_error("Error opening/writing config filename")


if __name__ == "__main__":
    args = sys.argv
    if len(args)-1 >=1:
        # we have CLI arguments
        log.debug("got CLI arguments, arguments are {}".format(args[1:]))
        log.debug(args)
        if "-make" in args:
            make_default_config_file()
        pass
    else:
        log.debug("No CLI arguments")

    init()

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
