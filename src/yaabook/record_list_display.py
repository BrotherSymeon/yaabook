import logging
import npyscreen
import sys

from yaabook.action_controller_search import ActionControllerSearch
from yaabook.record_list import RecordList



class RecordListDisplay(npyscreen.FormMuttActiveTraditional):
    MAIN_WIDGET_CLASS = RecordList
    ACTION_CONTROLLER = ActionControllerSearch

    def beforeEditing(self):
        self.wStatus1.value = "YaAbook - v0.0.1 - Python" + str( sys.version_info[0] )
        self.wStatus2.value = f"count {len(self.parentApp.myDatabase.all())} "
        self.update_list()


    def update_list(self):
        self.wMain.values = self.parentApp.myDatabase.all()
        self.wMain.display()
