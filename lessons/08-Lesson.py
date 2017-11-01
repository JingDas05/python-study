import pandas.io.sql
import pyodbc

DB = {
    'drivername': 'mssql+pyodbc',
    'servername': 'DAVID-THINK',
    #'port': '5432',
    #'username': 'lynn',
    #'password': '',
    'database': 'BizIntel',
    'driver': 'SQL Server Native Client 11.0',
    'trusted_connection': 'yes',
    'legacy_schema_aliasing': False
}
# Parameters
server = 'DAVID-THINK'
db = 'BizIntel'

# Create the connection
conn = pyodbc.connect('DRIVER='+DB['drivername']+';SERVER=' + DB['servername'] + ';DATABASE=' + DB['database'] + ';Trusted_Connection=yes')

# query db
sql = """
SELECT top 5 *
FROM data
"""
df = pandas.io.sql.read_sql(sql, conn)
df.head()
