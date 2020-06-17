class ContactDb:
    def __init__(self,db):
        self.db=db
        pass

    def add(self,name, number):
        cur=self.db.cursor()
        cur.execute('insert into contacts values(?,?)', (name,number))
        pass
    
    def update(self, name, number):
        cur=self.db.cursor()
        cur.execute('update contacts set number=? where name=?', (number,name))

        pass
  
    
    def delete(self, name):
        cur=self.db.cursor()
        cur.execute('delete from contacts where name=?', (name,))
        pass

    def view(self):
        cur = self.db.cursor()
        cur.execute('select * from contacts')
        cts = cur.fetchall()
        return cts
        pass

    def search(self, name):
        cur=self.db.cursor()
        cur.execute('select name  from contacts where name=?',(name,))
        cts=cur.fetchall()
        if not cts:
            return False
        else:
            return True
        pass

    def find(self,name):
        cur=self.db.cursor()
        cur.execute('select number from contacts from where name=?',(name,))
        number = cur.fetchall()
        return number
        pass

    pass