import psycopg2
def connect_database():
    connection = psycopg2.connect(
    host="localhost",
    database="osaka",
    user="aru"
    )
    return connection

def create_table(connection,schema,table_name):
    query = '''
          CREATE TABLE {}.{}(
            date    date,
            time    time,
            count   int
          );
          '''.format(schema,table_name)
    print(query)
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()

def insert_table(connection,schema,table_name,date,time,count):
    insert_query = "INSERT INTO {}.{}(date,time,count)VALUES (%s, %s, %s)".format(schema,table_name)
    print(insert_query)
    cursor = connection.cursor()
    cursor.execute(insert_query, (date, time, count))
    connection.commit()



connection = connect_database()

insert_table(connection,"toilet1","b","2023-10-01","21:32",1)