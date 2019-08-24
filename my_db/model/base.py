from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#https://auth0.com/blog/sqlalchemy-orm-tutorial-for-python-developers/
#127.0.0.1 = localhost

engine = create_engine("mysql+pymysql://root:root@localhost:3306/my_movie_db?charset=utf8&use_unicode=0", pool_recycle=3600)
Session = sessionmaker(bind=engine)
Base = declarative_base()

