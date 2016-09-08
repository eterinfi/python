# Filename: init_adb.py

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

# Begin

abfile = 'add_book.data'

c1 = Contact('Robin Thomas', 'Chicago Landlord', 'robin.thomas.lmt@gmail.com', '+1-8479023832')
c2 = Contact('Song Shanshan', 'Subleaser', 'shanshansong723@163.com', '+1-3128048203')
c3 = Contact('Su Ye', 'Minnesota', '+1-6512426872', '+1-6512016384', '+1-9524746778')
c4 = Contact('Shen Shilin', 'UIC Fellow', 'shilin_shen@hotmail.com', '+86-13391322767', '+1-5305740829')
c5 = Contact('Rachel Chen Qiuyue', 'Bank of China NY', 'qchen@bocusa.com', '+1-6462313096')
c6 = Contact('Sophia Wang', 'Stranger', 'Unknown', '+86-15019432875')

c = [c1, c2, c3, c4, c5, c6]

# Initiate the Address Book File

f = file(abfile, 'w')
p.dump(c, f) # Save the Contacts to File
f.close()