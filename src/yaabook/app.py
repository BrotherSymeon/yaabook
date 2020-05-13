#!/usr/bin/env python3

from .addressDb import AddressDB
from .address_book_app import AddressBookApplication
from .app_config import AppConfig


from pathlib import Path
import logging
import time
import argparse
import fileinput
import sys
import select
import configparser
import re
from os.path import join, isdir,isfile, expanduser

from os import mkdir



app_db_file_path = ''
APP_NAME = 'yaabook'

def init_config():
    """ this sets the default values that we want for the app """
    global APP_NAME
    app_path = str(Path(__file__).parent.absolute())
    app_db_file = 'yaabook.json'
    config = AppConfig(APP_NAME, {'default':
        {'dbfile': join(app_path, app_db_file) }
    })


def setup_logging():
    app_path = Path(__file__).parent.absolute()
    logfile = join(app_path, 'yaabook.log')
    logging.basicConfig(filename=logfile, filemode='a', format='%(asctime)s %(levelname)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.DEBUG)

def output_matching_contacts(search_string=''):
    #pdb.set_trace()
    global APP_NAME
    config = AppConfig(APP_NAME)
    db = AddressDB(config.get('default', 'dbfile'))
    items = db.search(search_string)
    logging.debug(items)
    for item in items:
        sys.stdout.write('\n' + item['email'] + '\t' + item['name'])
        #print( item['email'] + '\t' + item['name'] )

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--query", help="Use this flag for query_command")
    args = parser.parse_args()
    logging.debug(args)
    if args.query:
        logging.debug(args.query)
        output_matching_contacts(search_string=args.query )
        return False
    else:
        return True

def extract_name_and_email(text):
    # email regex - '([^<]+)\s<(.*)>'
    # from regex - 'From:(.*)'
    try:
        from_matcher = re.compile('From:(.*)')
        email_matcher = re.compile('([^<]+)\s<(.*)>')
        logging.debug('matching data attempt')
        from_data = from_matcher.match(text)
        if from_data:
            data = from_data.goup()
            logging.debug(f"matched {data}")
        else:
            logging.debug('there was no match')

    except AttributeError as error:
        logging.debug("attribute Error: {}".format(error))

def get_stdin():
    if select.select([sys.stdin,],[],[],0.0)[0]:
        logging.debug('stdin has data')
        added = ''
        for line in fileinput.input():
            added += line

        #logging.debug( 'added item= ' + added )
        extract_name_and_email(added)
        sys.exit()
    else:
        logging.debug('stdin has no data')

def run():
    init_config()
    setup_logging()
    get_stdin()

    if get_args():
        show_ui()

def show_ui():
    myApp = AddressBookApplication()
    myApp.run()

if __name__ == "__main__":
  run()
