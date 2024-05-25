import pyodbc
# Database connection

conn_str = (
    "Driver={ODBC Driver 18 for SQL Server};"
    "Server=DESKTOP-EU57KO2;"
    "Database=TestingDb;"
    "Trusted_Connection=yes;"
    "TrustServerCertificate=yes;"  # Bypass SSL certificate verification
)

#connection = pyodbc.connect(conn_str)
#print("Connected successfully")
#connection.close()