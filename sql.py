import sqlite3
from data import playgolf

dbname = 'test.db'
tbname = 'playgolf'

def openDB(db):
    try:
        conn = sqlite3.connect(db)
        print "Database %s opened." % db
        return conn
    except:
        print "ERROR OPENING DATABASE %s!" % db
        return None

def newCursor(conn):
    if isinstance(conn, sqlite3.Connection):
        cursor = conn.cursor()
        return cursor
    else:
        print "INVALID ARGUMENT TYPE!"
        return None

def closeDB(conn):
    if isinstance(conn, sqlite3.Connection):
        conn.cursor().close()
        conn.commit()
        conn.close()
        return True
    else:
        print "INVALID ARGUMENT TYPE!"
        return False

def dropTable(cursor, tb):
    try:
        cursor.execute('drop table %s' % tb)
        print "Table %s dropped!" % tb
        return True
    except:
        print "Table %s doesn't exist!" % tb
        return False

tmap = {
  str:   'varchar(255)',
  int:   'int',
  long:  'bigint',
  float: 'float',
  bool:  'tinyint(1)'
}
  
def migrate(s):
    if not isinstance(s, list):
        print "INVALID ARGUMENT TYPE!"
        return None
    m = {}
    s0 = s[0] if s else {}
    for key in s0:
        col = str(key)
        value = s0[key]
        if type(value) in tmap.keys():
            m[col] = tmap[type(value)]
        else:
            print "INVALID SEGMENT TYPE!"
            print key, ": ", type(value)
            return None
    return m

def createTable(cursor, tb, m):
    if not isinstance(m, dict):
        print "INVALID ARGUMENT DATA TYPE!"
        return None
    if not m:
        print "ERROR: NO SEGMENT!"
        return None
    idFlag = False
    d = ""
    for col in m:
        ctype = m[col]
        if not isinstance(col, str):
            print "INVALID SEGMENT NAME!"
            return None
        if not isinstance(ctype, str) or ctype not in tmap.values():
            print "INVALID SEGMENT TYPE!"
            return None
        d += col + " " + ctype
        if col.upper() == 'ID':
            d += " primary key"
            idFlag = True
        d += ","
    d = d[:-1]
    if not idFlag:
        d = "ID int primary key autoincrement," + d
    sql = 'create table %s (%s)' % (tb, d)
    try:
        cursor.execute(sql)
        print "Table %s created." % tb
        return True
    except:
        print "Error creating table %s!" % tb
        return False

try:
    cursor.execute('insert into       %s (ID, OUTLOOK, TEMPERATURE, HUMIDITY, WIND, PLAY)\
                                  select   1, "sunny",          85,       85,    0,    0\
                        union all select   2, "sunny",          80,       90,    1,    0\
                        union all select   3, "overcast",       83,       78,    0,    1\
                        union all select   4, "rain",           70,       96,    0,    1\
                        union all select   5, "rain",           68,       80,    0,    1\
                        union all select   6, "rain",           65,       70,    1,    0\
                        union all select   7, "overcast",       64,       65,    1,    1\
                        union all select   8, "sunny",          72,       95,    0,    0\
                        union all select   9, "sunny",          69,       70,    0,    1\
                        union all select  10, "rain",           75,       80,    0,    1\
                        union all select  11, "sunny",          75,       70,    1,    1\
                        union all select  12, "overcast",       72,       90,    1,    1\
                        union all select  13, "overcast",       81,       75,    0,    1\
                        union all select  14, "rain",           71,       80,    1,    0\
    ' % tb)
except:
    cursor.close()
    conn.close()
    print "ERROR INSERTING DATA INTO %s!" % tb
    raise

print "%d row(s) inserted." % cursor.rowcount

try:
    cursor.execute('delete from %s where id=10' % tb)
    print "%d row(s) deleted. " % cursor.rowcount
except:
    cursor.close()
    conn.close()
    print "ERROR DELETING DATA FROM %s!" % tb
    raise

try:
    cursor.execute('select * from %s' % tb)
except:
    cursor.close()
    conn.close()
    print "ERROR SELECTING DATA FROM %s!" % tb
    raise
recordset = cursor.fetchall()
print "%d row(s) selected." % len(recordset)
for record in recordset:
    print record

cursor.close()
conn.commit()
conn.close()