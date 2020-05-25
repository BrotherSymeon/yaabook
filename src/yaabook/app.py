#!/usr/bin/env python3

from yaabook.addressDb import AddressDB
from yaabook.address_book_app import AddressBookApplication
from yaabook.app_config import AppConfig


from pathlib import Path
import logging
import time
import argparse
import fileinput
import sys
import select
import configparser
import re
from os.path import join, isdir, isfile, expanduser
from os import mkdir

app_db_file_path = ''
APP_NAME = 'yaabook'


def init_config():
    """ this sets the default values that we want for the app """
    global APP_NAME
    app_path = str(Path(__file__).parent.absolute())
    app_db_file = 'yaabook.json'
    config = AppConfig(APP_NAME, {'default':{'dbfile': join(app_path, app_db_file)}})


def setup_logging():
    app_path = Path(__file__).parent.absolute()
    logfile = join(app_path, 'yaabook.log')
    logging.basicConfig(filename=logfile, filemode='a', format='%(asctime)s %(levelname)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.DEBUG)


def add_email_to_db(data):
    """ data should be a two tuple """
    global APP_NAME
    config = AppConfig(APP_NAME)
    db = AddressDB(config.get('default', 'dbfile'))
    db.add_record(name=data[0], email=data[1])


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
        logging.debug(f'matching data attempt matching {text}')
        from_data = from_matcher.match(text)
        if from_data:
            logging.debug("from_data true")
            data = from_data.group()
            logging.debug(f'data = {data}')
            email_match = email_matcher.match(data)
            name = email_match.group(1).replace('"', '').replace('From: ', '')
            email = email_match.group(2).replace('<', '').replace('>', '')

            logging.debug(f"matched email = {email} name = {name}")
            return (name, email)
        else:
            logging.debug('there was no match')

    except AttributeError as error:
        logging.debug("attribute Error: {}".format(error))


def get_stdin():
    if select.select([sys.stdin,],[],[],0.0)[0]:
        logging.debug('stdin has data')
        added = ''
        for line in fileinput.input():
            if line.strip().startswith('From:'):
                added = line
                break

        logging.debug( 'added item= ' + added )
        add_email_to_db( extract_name_and_email( added ) )
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
