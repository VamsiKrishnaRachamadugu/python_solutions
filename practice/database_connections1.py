import mysql as m
import mysql.connector

def connection(dbtype, dbname, type_of_query):
    mydb = m.connector.connect(host='localhost', user='root', password='root', database=dbname)
    cursor = mydb.cursor()
    if type_of_query.lower() == 'select':
        cursor.execute('select * from emp')
        result = cursor.fetchall()
        for data in result:
            print(data)
    elif type_of_query.lower() == 'insert':
        empid = int(input('Enter employee id:'))
        emp_name = input('Enter employee name:')
        emp_salary = float(input('Enter employee salary:'))
        depid = int(input('Enter department id:'))
        col_list = [empid, emp_name, emp_salary, depid]
        query = 'insert into emp values (%s,%s,%s,%s)'
        cursor.execute(query, col_list)
        mydb.commit()
        print(cursor.rowcount, "was inserted.")

    cursor.close()
    mydb.close()


database_type = input('Enter database type which is using: ')
database_name = input('Enter database name: ')
query_type = input("Use select or insert for query validations: ")
connection(database_type, database_name, query_type)