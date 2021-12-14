import os
import json
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

SECRET_FILE = os.path.join(BASE_DIR, 'secrets.json')
screts = json.loads(open(SECRET_FILE).read())
DB = screts["DB"]

DATABASE_URL =  f"mysql+pymysql://{DB['user']}:{DB['password']}@{DB['host']}:{DB['port']}/{DB['database']}?charset=utf8"
# DATABASE_URL = "mysql+pymysql://root:yejoon135!@localhost:3306/db?charset=utf8"


engine = create_engine(DATABASE_URL, encoding='utf-8')
Session = sessionmaker(bind=engine, autocommit=False, autoflush=False)


