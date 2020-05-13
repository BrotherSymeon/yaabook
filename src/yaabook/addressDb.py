from tinydb import TinyDB, Query

class AddressDB(object):
    def __init__(self, filename="addressDB.json"):
        self.dbfilename = filename

    def add_record(self, name='', email='', tags='', addressLine1='', addressLine2='', city='', state='', zip_code=''):
        db = TinyDB(self.dbfilename)
        return db.insert({'name': name, 'email': email, 'tags': tags, 'addressLine1': addressLine1, 'addressLine2': addressLine2, 'city': city, 'state': state, 'zip_code': zip_code})
    def get_record(self, id):
        db = TinyDB(self.dbfilename)
        return db.get(doc_id=id)

    def update_record(self, id, name='', email='', tags='', addressLine1='', addressLine2='', city='', state='', zip_code=''):
        db = TinyDB( self.dbfilename )
        return db.update({'name': name, 'email': email, 'tags': tags, 'addressLine1': addressLine1, 'addressLine2': addressLine2, 'city': city, 'state': state, 'zip_code': zip_code}, doc_ids=[id])

    def delete_record( self, id ):
        db = TinyDB( self.dbfilename )
        return db.remove( doc_ids=[id] )

    def search(self, text):
        Address = Query()
        db = TinyDB( self.dbfilename )
        return db.search( Address.email.search(text) | Address.tags.search(text) | Address.name.search(text))

    def all(self):
        db = TinyDB( self.dbfilename )
        return db.all()
