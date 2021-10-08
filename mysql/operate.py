import pymysql

host='127.0.0.1'
port=3306
user='root'
password='964939451'
database='qqrobot'



# Add message: Equal to add quest and reply to database
def addInfo(quest, reply):
    # Connect to database
