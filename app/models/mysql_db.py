import pymysql

def get_ai_data():
    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='elie',
        db='myprojectdb',
        cursorclass=pymysql.cursors.DictCursor
    )
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT id, name, description FROM ai_experiments")
            return cursor.fetchall()
    finally:
        connection.close()




        