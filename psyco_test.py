# http://localhost:8888/notebooks/2023-04_data_analysis_sqlite_pycon/SQLAlchemy-Tests.ipynb

# To get host in WSL run `grep nameserver /etc/resolv.conf | awk '{print $2}'`
# And follow these intructions: https://stackoverflow.com/a/67596486
# And host was set in ~/.bashrc as wslwinhost


import psycopg2

conn = psycopg2.connect(
    database="Adventureworks",
    host="172.29.48.1",
    user="postgres",
    password="10042076",
    port="5432"
)

cursor = conn.cursor()
cursor.execute('SELECT * FROM "Dimensions".dim_address')

print(cursor.fetchone())


import platform
print(platform.node())


from dotenv import load_dotenv
import os

load_dotenv()
print(os.environ.get('RENDER_PG_HOST'))
print(os.environ.get('RENDER_PG_USER'))
print(os.environ.get('RENDER_PG_PSWD'))