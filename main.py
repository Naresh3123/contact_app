# add ,delete, view ,edit and search contact by name or number and use modules and classes

import sqlite3
from contacts_db import ContactDb
db=sqlite3.connect('contacts.db')
c=ContactDb(db)
cmd = ''
print('contact app is opened:')
print('operation is : ')
while cmd != 'exit':
    cmd = input('>>> ')
    tokens = cmd.split()
    cmd = tokens[0]

    if cmd == 'add':
        name = input('enter contact name: ')
        if c.search(name)==False:
            number= input('enter contact number : ')
            c.add(name,number)
            print('contact added')
        else:
            print('contact is available ')

    elif cmd == 'view':
        cts=c.view()
        print('contact list is :')
        for contact in cts:
            name,number = contact
            print(name, ':', number)

    elif cmd == 'delete':
        name = input('enter contact name: ')
        if c.search(name)==True:
            c.delete(name)
            print('contact deleted')
        else:
            print('contact is not available ')

    elif cmd == 'update':
        name = input('enter contact name: ')
        if c.search(name)==True:
            number=input('enter contact number :')
            c.update(name,number)
            print('contact updated ')
        else:
            print('contact is not available')

    elif cmd == 'search':
        name=input('enter contact name :')
        if c.search(name)!=True:
            print('contact is not available')
        else:
            number=c.find(name)
            print('seached contact number is :',number)

    elif cmd != 'exit':
        print('option is not avilable ')
    elif cmd=='exit':
        print('contact app closed')

db.commit()
db.close()