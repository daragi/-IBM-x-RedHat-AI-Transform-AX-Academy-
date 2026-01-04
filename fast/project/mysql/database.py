from sqlalchemy import *
from sqlalchemy.orm import sessionmaker

DB_URL =  'mysql+pymysql://hr:hr@localhost:3306/erpdb'

class engineconn:
    
    def __init__(self):
        self.engine = create_engine(DB_URL,pool_recycle=500)
        
    def sessionmaker(self):
        Session = sessionmaker(bind=self.engine)
        session = Session() # 상속받아서 오버라이드
        return session

    def connection(self):
        conn = self.engine.connect()
        return conn