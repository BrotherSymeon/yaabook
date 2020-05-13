import logging
import npyscreen



class EditRecord(npyscreen.ActionForm):
    def create(self):
        self.value = None
        self.wgName     = self.add(npyscreen.TitleText, name = "Name:")
        self.wgEmail    = self.add(npyscreen.TitleText, name = "Email:")
        self.wgTags     = self.add(npyscreen.TitleText, name = "Tags:")
        self.nextrely   += 1
        self.wgAddress1 = self.add(npyscreen.TitleText, name = "Address Line1:", begin_entry_at=18)
        self.wgAddress2 = self.add(npyscreen.TitleText, name = "Address Line2:", begin_entry_at=18)
        self.wgCity     = self.add(npyscreen.TitleText, name = "City:")
        self.wgState    = self.add(npyscreen.TitleText, name = "State:")
        self.wgZip      = self.add(npyscreen.TitleText, name = "Zip:")

    def beforeEditing(self):
        if self.value:
            record = self.parentApp.myDatabase.get_record(self.value)
            self.name = "Record id : %s" % record.doc_id
            self.record_id          = record.doc_id
            self.wgName.value   = record['name']
            self.wgTags.value = record['tags']
            self.wgEmail.value      = record['email']
            self.wgAddress1.value      = record['addressLine1']
            self.wgAddress2.value      = record['addressLine2']
            self.wgCity.value      = record['city']
            self.wgState.value      = record['state']
            self.wgZip.value      = record['zip_code']
        else:
            self.name = "New Record"
            self.record_id          = ''
            self.wgName.value   = ''
            self.wgTags.value = ''
            self.wgEmail.value      = ''
            self.wgAddress1.value      = ''
            self.wgAddress2.value      = ''
            self.wgCity.value      = ''
            self.wgState.value      = ''
            self.wgZip.value      = ''

    def on_ok(self):
        if self.record_id: # We are editing an existing record
            self.parentApp.myDatabase.update_record(self.record_id,
                    name=self.wgName.value,
                    tags = self.wgTags.value,
                    email = self.wgEmail.value,
                    addressLine1= self.wgAddress1.value,
                    addressLine2= self.wgAddress2.value,
                    city= self.wgCity.value,
                    state= self.wgState.value,
                    zip_code= self.wgZip.value
                    )
        else: # We are adding a new record.
            self.parentApp.myDatabase.add_record(name=self.wgName.value,
                    tags = self.wgTags.value,
                    email = self.wgEmail.value,
                    )
        self.parentApp.switchFormPrevious()

    def on_cancel(self):
        self.parentApp.switchFormPrevious()

