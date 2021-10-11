import json
from Scraper import Scraper
from os.path import exists
import getopt
import sys

# process arguments
(OPT, _) = getopt.getopt(sys.argv[1:], "cdu:p:", [
    "cache", "debug", "username", "password"])
OPT = dict(OPT)

DEBUG = '-d' in OPT or '--debug' in OPT
USE_CACHE = '-c' in OPT or '--cache' in OPT
USERNAME = OPT['-u'] if OPT['-u'] != '' else OPT['--username']
PASSWORD = OPT['-p'] if OPT['-p'] != '' else OPT['--password']


def get_data(scraper) -> dict:
    data = {}

    if not USE_CACHE or not exists('./data.json'):
        # refetch data
        data = scraper.fetch_data(USERNAME, PASSWORD)

        if USE_CACHE:
            # cache data
            data_json = json.dumps(data, indent=4)

            with open('data.json', 'w') as f:
                f.write(data_json)
    else:
        # get catched data
        with open('data.json', 'r') as f:
            data = json.load(f)

    return data


def main():
    scraper = Scraper(DEBUG)  # TODO : run this in background thread
    data = get_data(scraper)  # TODO : await until scraper has been initalized
    print("data", data)


if __name__ == '__main__':
    main()
