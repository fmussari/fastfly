from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import create_engine

from dotenv import load_dotenv
import os

# To get host in WSL run `grep nameserver /etc/resolv.conf | awk '{print $2}'`
# And follow these intructions: https://stackoverflow.com/a/67596486
# And host was set in ~/.bashrc as wslwinhost


load_dotenv()
RENDER_PG_HOST = os.environ.get('RENDER_PG_HOST')
RENDER_PG_USER = os.environ.get('RENDER_PG_USER')
RENDER_PG_PSWD = os.environ.get('RENDER_PG_PSWD')
RENDER_PG_DB = os.environ.get('RENDER_PG_DB')

local_engine = create_engine(
    "postgresql://postgres:10042076@wslwinhost/fastfly_db", 
    echo = True
)

DB_CONNECTION = f"postgresql://{RENDER_PG_USER}:{RENDER_PG_PSWD}@{RENDER_PG_HOST}:5432/{RENDER_PG_DB}"

engine = create_engine(
    DB_CONNECTION, 
    echo = True
)

Base = declarative_base()
Session = sessionmaker(bind=engine)
SessionLocal = sessionmaker(bind=local_engine)