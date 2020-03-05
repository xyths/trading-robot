#!/usr/bin/python3

import sys
import getopt
import configparser


def main(argv):
    configfile = ''
    try:
        opts, args = getopt.getopt(argv, "hc:", ["configfile="])
    except getopt.GetoptError:
        print('ma_across.py -c <configfile>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('ma_across.py -c <configfile>')
            sys.exit()
        elif opt == "-c":
            configfile = arg
    print('Config file is ', configfile)
    config = configparser.ConfigParser()
    config.read(configfile)
    print("config sections:", config.sections())
    key = config["gate"]["key"]
    secret = config["gate"]["secret"]
    print("key: {}, secret: {}".format(key, secret))


if __name__ == "__main__":
    main(sys.argv[1:])
