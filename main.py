__version__ = “1.0”

import json
from Scraper import Scraper
from Plot import Plot
from os.path import exists
from os import environ

# prevent kivy from parsing command line args
environ["KIVY_NO_ARGS"] = "1"  # nopep8

import getopt
import sys
from kivy.app import App
import kivy
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.lang import Builder

# process arguments
(OPT, _) = getopt.getopt(sys.argv[1:], "cdu:p:", [
    "cache", "debug", "username", "password"])
OPT = dict(OPT)

DEBUG = '-d' in OPT or '--debug' in OPT
USE_CACHE = '-c' in OPT or '--cache' in OPT
USERNAME = OPT['-u'] if OPT['-u'] != '' else OPT['--username']
PASSWORD = OPT['-p'] if OPT['-p'] != '' else OPT['--password']


class Plotter(App):
    def build(self):

        # get data which is a list of dictionaries, sorted by entry date
        scraper = Scraper(DEBUG)  # TODO : run this in background thread
        # TODO : await until scraper has been initalized
        data = self.get_data(scraper)
        print("data", data)

        Builder.load_file("app.kv")

        return Plot(data)

    def get_data(self, scraper) -> dict:
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


if __name__ == '__main__':
    app = Plotter()
    app.run()
