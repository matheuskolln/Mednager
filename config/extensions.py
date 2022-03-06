from typing import Any
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm.session import sessionmaker

DB_URI = "mysql://root:root@db:3306/backend"

db_engine = create_engine(DB_URI)
db_session = sessionmaker(bind=db_engine)()

Base: Any = declarative_base()
