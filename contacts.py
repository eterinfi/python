# Filename: contacts.py

import re
try:
    import cPickle as p
except ImportError:
    import pickle as p

class Contact():
    def __init__(self, name, ref, email, phone1, phone2=None):
        self.name = name
        self.ref = ref
        self.email = email
        self.phone1 = phone1
        self.phone2 = phone2
    def info(self):
        return [self.ref, self.email, self.phone1, self.phone2]

class Address_Book():
    def __init__(self, contacts):
        self.contacts = contacts
    
    def __len__(self):
        print 'Total Contact(s): %d' % self.contacts.__len__()
        
    def create(self, contact):
        if contact.name in self.contacts:
            print '%s has already existed!' % contact.name
            self.__len__()
            return 0 # Create Failed
        else:
            print 'CREATING NEW CONTACT: %s' % contact.name
            print '  Ref:%s     Email:%s     Phone:%s' % (contact.ref, contact.email, ' & '.join([str(contact.phone1), str(contact.phone2)]))
            self.contacts[contact.name] = contact.info()
            self.__len__()
            return 1 # Create Successful

    def delete(self, n):
        if n in self.contacts:
            print 'DELETING EXISTING CONTACT: %s' % n
            del self.contacts[n]
            self.__len__()
            return 1 # Delete Successful
        else:
            print "%s doesn't exist!" % n
            self.__len__()
            return 0 # Delete Failed

    def search(self, n=None):
        if n:
            if n in self.contacts:
                ref, email, phone1, phone2 = self.contacts[n]
                print '%s (%s)     Email: %s;     Phone: %s' % (n, ref, email, ' & '.join([str(phone1), str(phone2)]))
                self.__len__()
                return 1 # Search Successful
            else:
                print "%s doesn't exist!" % n
                self.__len__()
                return 0 # Search Failed
        else: # Output Everything
            print '\nCURRENT ADDRESS BOOK:'
            for name, [ref, email, phone1, phone2] in sorted(self.contacts.items()):
                print '  %s (%s)     Email: %s;     Phone: %s' % (name, ref, email, ' & '.join([str(phone1), str(phone2)]))
            self.__len__()
            return -1

    def update(self, n):
        if n in self.contacts:
            cont = True
            while cont:
                v = raw_input('Update: [0]Ref; [1]Email; [2]Phone1; [3]Phone2; [8]Name; Others to return?')
                if len(v) > 0:
                    v0 = v[0]
                else:
                    v0 = '9'
                if v0 == '0': # Update Ref
                    print 'Current Ref:%s' % self.contacts[n][0]
                    ref = raw_input('New Ref:')
                    print 'UPDATING REF'
                    self.contacts[n][0] = ref
                elif v0 == '1': # Update Email
                    print 'Current Email:%s' % self.contacts[n][1]
                    while True:
                        email = raw_input('Email:')
                        regex = r'[0-9a-zA-Z\.\_]+@[0-9a-zA-Z]+(\.[0-9a-zA-Z]+)+'
                        if re.match(regex, email):
                            break
                        print('Invalid Email address!')
                    print 'UPDATING EMAIL'
                    self.contacts[n][1] = email
                elif v0 == '2': # Update Phone1
                    print 'Current Phone1:%s' % self.contacts[n][2]
                    phone1 = raw_input('New Phone1:')
                    print 'UPDATING PHONE1'
                    self.contacts[n][2] = phone1
                elif v0 == '3': # Update Phone2
                    print 'Current Phone2:%s' % self.contacts[n][3]
                    phone2 = raw_input('New Phone2:')
                    print 'UPDATING PHONE2'
                    self.contacts[n][3] = phone2
                elif v0 == '8': # Rename
                    print 'Current Name:%s' % n
                    while True:
                        nn = raw_input('New Name:')
                        if len(nn)>0:
                            break
                    if n != nn:
                        print 'RENAMING FROM %s TO %s' % (n, nn)
                        cn = Contact(nn, self.contacts[n][0], self.contacts[n][1], self.contacts[n][2], self.contacts[n][3])
                        del self.contacts[n]
                        self.contacts[cn.name] = cn.info()
                        n = nn
                    else:
                        print 'Name not changed!'
                else: # Done
                    cont = False
                if cont:
                    self.search(n)
            return 1 # Update Successful
        else:
            print "%s doesn't exist!" % n
            self.__len__()
            return 0 # Update Failed

# Begin
abfile = 'add_book.data'

# Import from Address Book File
print 'Loading %s' % abfile
f = open(abfile, 'r')
c = p.load(f)
f.close()
ab = Address_Book({})
for cn in c:
    ab.create(cn)

# Console
running = True
while running:
    ab.search
    k = raw_input('(C)reate; (D)elete; (S)earch; (U)pdate; (Q)uit?')
    if len(k) > 0:
        k0 = k[0].upper()
    else:
        k0 = 'Q'
    if k0 == 'C': # Create new contact
        print '***** CREATE NEW CONTACT *****'
        while True:
            name = raw_input('Name:')
            if len(name) > 0:
                break
        ref = raw_input('Ref:')
        while True:
            email = raw_input('Email:')
            regex = r'[0-9a-zA-Z\.\_]+@[0-9a-zA-Z]+(\.[0-9a-zA-Z]+)+'
            if re.match(regex, email):
                break
            print('Invalid Email address!')
        phone1 = raw_input('Phone1:')
        phone2 = raw_input('Phone2:')
        cn = Contact(name, ref, email, phone1, phone2)
        ab.create(cn)
    elif k0 == 'D': # Delete existing contact
        print '***** DELETE EXISTING CONTACT *****'
        name = raw_input('Name:')
        ab.delete(name)      
    elif k0 == 'S': # Search existing contact
        print '***** SEARCH EXISTING CONTACT *****'
        name = raw_input('Name:')
        ab.search(name)
    elif k0 == 'U': # Update existing contact
        print '***** UPDATE EXISTING CONTACT *****'
        name = raw_input('Name:')
        ab.update(name)
    elif k0 == 'Q': # Quit
        running = False

# Export to Address Book File

ab.__len__()
c = []
for name, [ref, email, phone1, phone2] in ab.contacts.items():
    cn = Contact(name, ref, email, phone1, phone2)
    c.append(cn)
print 'Saving %s' % abfile    
f = open(abfile, 'w')
p.dump(c, f) # Save the Contacts to File
f.close()