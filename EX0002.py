# Project : show me the code
# Author : puorc
import MySQLdb
import EX0001


def init_db(db):
    cursor = db.cursor()
    if init_db.flag == 0:
        cursor.execute("""SELECT COUNT(*) FROM information_schema.tables
WHERE table_name = 'DISCOUNTCODE'""")
        if_table_exists_bit = cursor.fetchone()
        if if_table_exists_bit[0] == 1:
            insert_data.flag = 1
        else:
            sql = """CREATE TABLE DISCOUNTCODE (
         CODE CHAR(40) NOT NULL,
         GDATE INT)"""
            cursor.execute(sql)
            insert_data.flag = 1
    else:
        pass


init_db.flag = 0


def insert_data(db, content, date):
    cursor = db.cursor()
    sql = "INSERT INTO DISCOUNTCODE(CODE, GDATE) \
       VALUES ('%s', '%d' )" % \
          (content, date)
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()


def get_time():
    time = ""
    for i in EX0001.get_sequence()[-4:]:
        time += i
    return int(time)


address = raw_input("Database address\n")
username = raw_input("Database username\n")
password = raw_input("Database password\n")
dbname = raw_input("Database dbname\n")
try:
    db = MySQLdb.connect(address, username, password, dbname)
except MySQLdb.DatabaseError:
    print "connection failed"
else:
    print "connection succeeded"
init_db(db)
for item in EX0001.result:
    insert_data(db, item, get_time())
print "Completed."