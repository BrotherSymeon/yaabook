

import npyscreen
import logging



class RecordList(npyscreen.MultiLineAction):
    def __init__(self, *args, **keywords):
        super(RecordList, self).__init__(*args, **keywords)
        self.add_handlers({
            "^A": self.when_add_record,
            "^D": self.when_delete_record,
            "q": self.when_exit,
            "^H": self.show_help
            })

    def display_value(self, vl):
        return "  %s\t %s\t %s" % (vl['name'], vl['email'], vl['tags'])

    def show_help(self, *args):
        help_message = """
        This is the help message
        so you can read it"""
        message_to_display = 'You have a choice, to Cancel and return false, or Ok and return true.'
        notify_result = npyscreen.notify_ok_cancel(message_to_display, title= 'popup')

    def when_exit(self, *args):
        self.parent.parentApp.switchForm( None )

    def actionHighlighted(self, act_on_this, keypress):
        self.parent.parentApp.getForm('EDITRECORDFM').value =act_on_this.doc_id
        self.parent.parentApp.switchForm('EDITRECORDFM')

    def when_add_record(self, *args, **keywords):
        self.parent.parentApp.getForm('EDITRECORDFM').value = None
        self.parent.parentApp.switchForm('EDITRECORDFM')

    def when_delete_record(self, *args, **keywords):
        self.parent.parentApp.myDatabase.delete_record(self.values[self.cursor_line].doc_id)
        self.parent.update_list()
