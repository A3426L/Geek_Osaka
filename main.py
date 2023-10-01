import psycopg2
def connect_database():
    connection = psycopg2.connect(
    host="localhost",
    database="osaka",
    user="aru"
    )
    return connection

def create_table(connection,name):
    query = '''
          CREATE TABLE {}(
            date    date,
            time    time,
            count   int
          );
          '''.format(name)
    print(query)
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()

connection=connect_database()
cursor = connection.cursor()
create_table(connection,"toilet2")


#データベースの情報
#print(connection.get_dsn_parameters(),"\n")

#挿入
insert_query = "INSERT INTO toilet1.a (date, time,count) VALUES (%s, %s, %s)"
date = "2023-10-01"
time = "10:01"
count = 1
cursor.execute(insert_query, (date,time,count))

#全取り出し
cursor.execute('SELECT * FROM toilet1.a')
row = cursor.fetchall()
print("row = ")
print(row)

#項目取り出し
select_query = "SELECT date,time FROM toilet1.a"
cursor.execute(select_query)
row2 = cursor.fetchall()
print("row2 = ")
print(row2)

#フィルタリいんぐ
# select_query = "SELECT date FROM toilet1.a WHERE condition = %s"
# condition_value = "2023-10-01"
# cursor.execute(select_query, (condition_value,))
# row3 = cursor.fetchall()
# print("row3 = ")
# print(row3)


connection.commit()
cursor.close()
connection.close()





