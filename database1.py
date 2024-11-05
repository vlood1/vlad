import pymysql
connection = pymysql.connect(
    host='localhost', 
    user='root', 
    password='root', 
    database='employees')

def print_fetch_result(result):
  for x in result:
    print(x)

print("done")


with connection.cursor() as cursor:
  sql="""
SHOW DATABASES;
  """
  cursor.execute(sql)
  result = cursor.fetchall()
  print_fetch_result(result)