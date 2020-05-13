from .action_controller_search import ActionControllerSearch
from .record_list import RecordList
import logging
import npyscreen
import sys



class RecordListDisplay(npyscreen.FormMuttActiveTraditional):
    MAIN_WIDGET_CLASS = RecordList
    ACTION_CONTROLLER = ActionControllerSearch

    def beforeEditing(self):
        self.wStatus1.value = "YaAbook - v0.0.1 - Python" + str( sys.version_info[0] )
        self.wStatus2.value = "count (105)"
        self.update_list()


    def update_list(self):
        self.wMain.values = self.parentApp.myDatabase.all()
        self.wMain.display()
