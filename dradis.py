#!/usr/bin/env python3

# Dradis Contact!!!
# This tool is meant to make my life easier

# What this tool does?:
# Allocate & Deploy that live in some MAAS host
# List all of my systems in MAAS
# Get the machine IPv4 address

# The following 3 steps I do quite often and frankly sick of navigating through
# the MAAS UI :-)


import yaml
import sys
import argparse
import logging

logging.basicConfig(level=logging.INFO)


def loadyaml(yamlfile):

    '''
    Load a yaml file & Return it"s values
    '''
    with open(yamlfile, "r") as f:
        a = yaml.load(f)
    return a


def get_labinfo(yamlfile, labsite):
    '''
    Get the lab info for loaded yaml
    '''
    try:
        labinfo = yamlfile['Labs']['{}'.format(labsite)]
        return labinfo
    except KeyError as e:
        logging.info('Error, Invalid Site: {}'.format(e))


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument('-l', '--lab',
                        help="This is the labs available and MAAS clouds \
                        as defined in data.yaml",
                        type=str,
                        required=False)
#    parser.add_argument('-p', '--port',
#                        help="Select the internal port you wish to bind to",
#                        required=True, type=int)
    args = parser.parse_args()

    lab = get_labinfo(loadyaml('data.yaml'), args.lab)
    apikey = lab['api_key']
    maas_url = lab['maas_url']

if __name__ == "__main__":
    sys.exit(main())
