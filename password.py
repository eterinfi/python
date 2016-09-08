import hashlib, json, re

def calc_md5(password):
    digest = hashlib.md5()
    digest.update(password)
    return digest.hexdigest()

def get_md5(username, password):
    return calc_md5(password + username + 'the-Salt')

def login(user, password):
    global db, current_user
    if user in db:
        if get_md5(user, password) == db[user]:
            print 'User %s login successful!' % user
            current_user = user
            return True
        else:
            print 'User %s password error!' % user
            return False
    else:
        print 'User %s doesn\'t exist!' % user
        return None

def logout():
    global current_user
    if current_user:
        print 'User %s logout successful!' % current_user
        current_user = None
        return True
    else:
        print 'Current user doesn\'t exist!'
        return False

def signup(user, password):
    global db
    if user in db:
        print 'User %s has already existed!' % user
        return False
    else:
        db[user] = get_md5(user, password)
        print 'User %s has signed up successfully!' % user
        return True

def change_password(user, current_password, new_password):
    global db
    if user in db:
        if get_md5(user, current_password) == db[user]:
            db[user] = get_md5(user, new_password)
            print 'User %s has changed password successfully!' % user
            return True
        else:
            print 'User %s password error!' % user
            return False
    else:
        print 'User %s doesn\'t exist!' % user
        return None

def remove_user(user, password):
    global db, current_user
    if user in db:
        if get_md5(user, password) == db[user]:
            db.pop(user)
            print 'User %s has been removed successfully!' % user
            if current_user == user:
                current_user = None
            return True
        else:
            print 'User %s password error!' % user
            return False
    else:
        print 'User %s doesn\'t exist!' % user
        return None    
    
def input_user():
    while True:
        user = raw_input('Username: ')
        if len(user) > 0 and re.match(r'^[\w\_]+$', user):
            break
    return user
            
def input_password(double_check = False):
    while True:
        password = raw_input('Password: ')
        if len(password) > 0:
            if double_check:
                reenter = raw_input('Re-enter password: ')
                if reenter == password:
                    break
                else:
                    print 'You must enter the same password twice!'
            else:
                break
    return password

filename = 'website.json'
current_user = None

print 'Loading %s...' % filename

try:
    f = open(filename, 'r')
    db = json.load(f)
except:
    db = {}

while True:
    if current_user:
        print '\nCurrent user: %s' % current_user,
    select = raw_input('1)Signup; 2)Login; 3)Logout; 4)Change Password; 5)Remove user; 9)List all users; 0)Exit? ')
    if select == '0':
        break
    elif select == '1':
        if current_user:
            print '\nCurrent user %s has logged in!' % current_user
            continue
        signup(input_user(), input_password(True))
    elif select == '2':
        if current_user:
            print '\nCurrent user %s has logged in!' % current_user
            continue
        login(input_user(), input_password())        
    elif select == '3':
        logout()
    elif select == '4':
        if current_user:
            user = current_user
            print '\nUser: %s' % user
        else:
            user = input_user()
        print '\nInput current password:'
        old = input_password()
        print '\nInput new password:'
        new = input_password(True)
        change_password(user, old, new)
    elif select == '5':
        remove_user(input_user(), input_password(True))
    elif select == '9':
        print '\nCurrent registered users: ', ' & '.join([user for user in db])
        print '\nTotal user(s): %d' % len(db)
        
print '\nSaving %s...' % filename
f = open(filename, 'w')
json.dump(db, f)
f.close()