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


class InvalidConfigurationException(Exception):
    """
    generic config error
    """
    pass


def init()->None:
    """
    Module init
    :return: None
    """
    # log.debug("Init: creating config parser....")
    # config_parser = ConfigParser()
    # log.info("Init: reading config file...")


def make_default_config_file(parser:ConfigParser=None, filename ='config.ini', filemode = 'w')->None:
    """
    Generates a default config filename
    :param parser: config parser instance
    :param filename: config filename by name to write to
    :param filemode: mode to open file, must be capable of writing
    :return: None
    """
    if not parser:
        log.debug("no parser provided, creating new instance")
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
        raise InvalidConfigurationException("Error opening/writing config filename")


def worker(parser:ConfigParser, config_file:str = "config.ini"):
    import time
    log.debug("entering worker")
    filename = None
    try:
        log.debug("opening logfile for reading...")
        parser.read(config_file)
        filename = parser.get('files','channel_fuelrats')
        log.debug("filename is {}".format(filename))
        with open(filename,'r', encoding='cp850'):
            log.info("successfully opened logfile")
    except FileNotFoundError as ex:
        log.error("unable to find file {}. please check the config and try again.".format(filename))
        return -2

    except Exception as ex:
        log.error(ex)
        raise ex

    log.debug("attempting to open file object from configs for reading...")
    try:
        with open(filename, encoding='cp850') as file:
            eol_reached =False
            while 1:
                where = file.tell()
                line = file.readline()
                if not line:
                    eol_reached=True
                    time.sleep(1)
                    file.seek(where)
                else:
                    if eol_reached:
                        log.debug(line)  # already has newline
    except TypeError as ex:
        log.error("type error occured, probably misconfigured filename?\n{}".format(ex))
    except KeyboardInterrupt:
        log.info("Keyboard interrupt. shutting down...")
        sys.exit(1)



if __name__ == "__main__":
    args = sys.argv
    log.debug("(MAIN) creating new ConfigParser instance")
    parser = ConfigParser()
    log.debug("reading CLI arguments...")
    if len(args)-1 >=1:
        # we have CLI arguments
        log.debug("got CLI arguments, arguments are {}".format(args[1:]))
        log.debug(args)
        if "-make" in args:
            log.info("making default configs...")
            make_default_config_file(parser=parser)
            import sys
            sys.exit(0)
        elif "-work" in args:
            log.info("Running worker....")
            worker(parser=parser)

    else:
        log.debug("No CLI arguments")
        print("No arguments. using runtime configs...")
    # init()
