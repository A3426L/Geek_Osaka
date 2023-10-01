import psycopg2
def connect_database():
    connection = psycopg2.connect(
    host="localhost",
    database="osaka",
    user="aru"
    )
    return connection
def create_schema(connection,schema_name):
    create_schema_query = "CREATE SCHEMA IF NOT EXISTS {}".format(schema_name)
    print(create_schema_query)
    cursor = connection.cursor()
    cursor.execute(create_schema_query)
    connection.commit()

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
    print(date)
    print(time)
    cursor = connection.cursor()
    cursor.execute(insert_query, (date, time, count,))
    connection.commit()

def read_table(connection,schema,table_name,element):
    read_query = "SELECT {} FROM {}.{}".format(element,schema,table_name)
    print(read_query)
    cursor = connection.cursor()
    cursor.execute(read_query)
    result = cursor.fetchall()
    return result



connection = connect_database()
# create_schema(connection,"toilet3")
# insert_table(connection,"toilet1","b","2023-10-01","21:57",1)
# result = read_table(connection,"toilet1","b","*")
# print(result)



connection.close()