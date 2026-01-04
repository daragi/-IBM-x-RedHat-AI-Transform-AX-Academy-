# pip install cx_Oracle pandas

import cx_Oracle
import pandas as pd
from sqlalchemy import create_engine
from fastapi import FastAPI, Depends, Path, HTTPException  
from pydantic import BaseModel

app = FastAPI()


@app.get('/')
async def first_get():
    cx_Oracle.init_oracle_client(lib_dir="C:/oraclexe/instantclient_11_2")
    oracle_connection_string = 'oracle+cx_oracle://{username}:{password}@{hostname}:{port}'

    engine = create_engine(
        oracle_connection_string.format(
            username='hr',
            password='hr',
            hostname='localhost',
            port='1521',
            database='xe',
        )
    )

    data = pd.read_sql("SELECT * FROM Employees", engine, index_col="employee_id")
    print(data)
# return data
# 조회한 결과를 데이터프레임으로 저장할 경우