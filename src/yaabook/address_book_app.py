

import logging
import npyscreen


from .record_list_display import RecordListDisplay
from .edit_record import EditRecord
from .addressDb import AddressDB
from .app_config import AppConfig


class AddressBookApplication(npyscreen.NPSAppManaged):
    def __init__(self, *args, **keywords):
        super(AddressBookApplication, self).__init__(*args, **keywords)
        for name, value in keywords.items():
            logging.debug(name + ' ' + value)
    def onStart(self):
        config = AppConfig('yaabook')
        self.config = config
        self.myDatabase = AddressDB(config.get(section='default', key='dbfile'))
        self.addForm("MAIN", RecordListDisplay)
        self.addForm("EDITRECORDFM", EditRecord)
