


import logging
import npyscreen

class ActionControllerSearch(npyscreen.ActionControllerSimple):
    def create(self):
        self.add_action('^/.*', self.set_search, True)

    def set_search(self, command_line, widget_proxy, live):
        logging.debug('searching for %s' % command_line[1:])
        self.parent.value.set_filter(command_line[1:])
        self.parent.wMain.values = self.parent.parentApp.myDatabase.search(command_line[1:])
        self.parent.wMain.display()
